<template>
  <v-col class="receiver" :xs="24" :sm="24" :md="24" :lg="12">
    <h1>{{ name }}</h1>
    <br/>
    <v-row class="block_message">
      <v-col span="3">
      </v-col>
      <v-col span="8">
        <div class="explain_panel">Step 1. Connect</div>
      </v-col>
      <v-col span="2">
        <v-button class="line_button" type="primary" shape="circle" icon="link" v-on:click="connectToOasis"></v-button>
      </v-col>
      <v-col span="2">
        <div v-if="flag_connect" class="lines-horizontal">
        </div>
      </v-col>
      <v-col span="8">
        <v-alert v-if="flag_connect" type="success" show-icon>
          Connected to <u>{{ local_gateway }}</u>
        </v-alert>
      </v-col>
      
    </v-row>

    <v-row class="block_message">
      <v-col span="3">
      </v-col>
      <v-col span="8">
        <div class="explain_panel">Step 2. Load<v-input v-model="block_address" type="text" placeholder="Please input the address"></v-input></div>
      </v-col>
      <v-col span="2">
        <v-button class="line_button" type="primary" shape="circle" icon="reload" v-on:click="loadService"></v-button>
      </v-col>
      <v-col span="2">
        <div v-if="flag_load" class="lines-horizontal">
        </div>
      </v-col>
      <v-col span="8">
        <v-alert v-if="flag_load" type="success" show-icon>
          Load at <u>{{ block_address }}</u>
        </v-alert>
      </v-col>
      
    </v-row>

    <v-row class="block_message">
      <v-col span="3">        
      </v-col>
      <v-col span="8">
        <div class="explain_panel">Step 3. Fetch<v-input v-model="public_value" type="text" placeholder="Please input the public value"></v-input></div>
      </v-col>
      <v-col span="2">
        <v-button class="line_button" type="primary" shape="circle" icon="download" v-on:click="fetch"></v-button>
      </v-col>
      <v-col span="2">
        <div v-if="fetch_result" class="lines-horizontal">
        </div>
      </v-col>      
      <v-col span="8">
        <v-alert v-if="fetch_result" type="success" show-icon>
          Result is <u>{{ fetch_result }}</u>
        </v-alert>
      </v-col>
    </v-row>

    <br/>
    
  </v-col>
</template>

<script>

import oasis from '@oasislabs/client';

export default {
  name: 'receiver',
  props: {
    name: String,
  },
  data () {
    return {
      sk: null,
      pk: null,
      flag_connect: false,
      flag_load: false,
      flag_upload: false,
      fetch_result: false,
      deployLocally: process.env.NODE_ENV === 'development',
      blackbox: null,
      secret: 'no secret',
      address: null,
      local_gateway: 'ws://10.20.9.237:8546'
    }
  },
  methods: {
    async connectToOasis() {
      let gateway = new oasis.gateways.Web3Gateway(
        this.local_gateway,
        oasis.Wallet.fromMnemonic('range drive remove bleak mule satisfy mandate east lion minimum unfold ready'));
      oasis.setGateway(gateway);
      this.flag_connect = true;
    },    

    async loadService() {
      // 还是需要先连接
      if(!this.flag_connect){
        await this.connectToOasis();
      }
      const blackbox = await oasis.Service.at(new oasis.Address(this.block_address));
      this.blackbox = blackbox;
      this.flag_load = true;
    },

    async fetch(){
      // this.secret = await this.blackbox.fetch();
      const sss = require('shamirs-secret-sharing');
      const temp_buff = await this.blackbox.fetch();
      this.fetch_result= sss.combine([new Buffer(this.public_value, 'hex'), new Buffer(temp_buff, 'hex')]);
    }

  }
}
</script>