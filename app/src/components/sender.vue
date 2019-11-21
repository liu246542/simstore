<template>
  <v-col class="sender" :xs="24" :sm="12" :md="12" :lg="12">
    <h2>{{ name }}</h2>
    <!-- :xs="24" :sm="12" :md="12" :lg="12" -->
    <!-- <h3>Sender</h3> -->
    <!-- <v-icon type="user" slot="before"> </v-icon> -->
    <br/>
    <v-row class="block_message">
      <v-col span="2" offset="4">
        <v-button class="line_button" type="primary" shape="circle" icon="link" v-on:click="connectToOasis"></v-button>
      </v-col>
      <v-col span="14">
        <div class="explain_panel">Step 1. Click and establish a connection to local block chain</div>
      </v-col>
    </v-row>

    <v-row>
      <v-col span="2" offset="4">
        <v-button class="line_button" type="primary" shape="circle" icon="cloud-upload-o" v-on:click="deployService"></v-button>
      </v-col>
      <v-col span="14">
        <div class="explain_panel">Step 2. Deploy your smart contract</div>
      </v-col>
    </v-row>

    <v-row>
      <v-col span="2" offset="4">
        <v-button class="line_button" type="primary" shape="circle" icon="save" v-on:click="store"></v-button>
      </v-col>
      <v-col span="14">
        <div class="explain_panel">Step 3. Store</div>
      </v-col>
    </v-row>

    <v-row>
      <v-col span="2" offset="4">
        <v-button class="line_button" type="primary" shape="circle" icon="download" v-on:click="fetch"></v-button>
      </v-col>
      <v-col span="14">
        <div class="explain_panel">Step 3. Fetch</div>
      </v-col>
    </v-row>


    <br/>

    




    <!-- <v-form direction="horizontal">
      <v-form-item label="Address" :label-col="labelCol" :wrapper-col="wrapperCol">
        <span class="ant-form-text">{{ address }}</span>
      </v-form-item>
      <v-form-item label="Secret" :label-col="labelCol" :wrapper-col="wrapperCol">
        <v-input type="textarea" placeholder="please input your secret" :wrapper-col="wrapperCol"></v-input>
      </v-form-item>

      <v-form-item :label-col="labelCol" :wrapper-col="{offset:6, span:10}">
        <v-button type="primary" style="margin-right:6px;" v-on:click="connectToOasis">
          Connect
        </v-button>
        <v-button type="default" style="margin-right:6px;" v-on:click="deployService">
          Deploy
        </v-button>
      </v-form-item>

      <v-form-item :label-col="labelCol" :wrapper-col="{offset:6, span:10}">
        <v-button type="default" style="margin-right:6px;" v-on:click="store" >
          Store
        </v-button>
        <v-button type="primary" style="margin-right:6px;" v-on:click="fetch" >
          Fetch
        </v-button>
      </v-form-item>
    </v-form> -->



    <!-- <span>私钥：</span>
    <input v-model="sk">
    <v-button v-on:click="connectToOasis">Connect</v-button>
    <v-button v-on:click="deployService">Deploy</v-button>
    <hr>
    <v-button v-on:click="store">Store</v-button>
    <v-button v-on:click="fetch">Fetch</v-button>
    <p> {{ secret }} </p>
    <p class="danger-region" >It works? {{ sk }}</p>


    <span>公钥：</span>
    <input v-model="pk">
    <p class="danger-region">It works? {{ pk }}</p>

    <span>SECRET:</span> -->
    
  </v-col>
</template>

<script>

import oasis from '@oasislabs/client';

export default {
  name: 'sender',
  props: {
    name: String,
  },
  data () {
    return {
      labelCol: {
        span: 6
      },
      wrapperCol: {
        span: 10
      },
      sk: null,
      pk: null,
      bytecode: 'simstore.wasm',
      flag_connect: null,
      deployLocally: process.env.NODE_ENV === 'development',
      blackbox: null,
      secret: 'no secret',
      address: null,
    }
  },
  methods: {
    async connectToOasis() {
      let gateway = new oasis.gateways.Web3Gateway('ws://localhost:8546', oasis.Wallet.fromMnemonic('range drive remove bleak mule satisfy mandate east lion minimum unfold ready'));
      oasis.setGateway(gateway);
      this.flag_connect = true;
    },

    async deployService() {
      if(!this.flag_connect){
        await this.connectToOasis();
      }
      const bytecode = await fetch(this.bytecode).then((response) => response.body)
      .then((stream) => new Response(stream))
      .then(async (response) => {
        const serviceBinary = await response.arrayBuffer();
        return new Uint8Array(serviceBinary);
      });

      const blackbox =  await oasis.deploy('hello world!',{
        bytecode,
        header: { confidential: !this.deployLocally },
        gasLimit: '0xf42400'
      });

      this.blackbox = blackbox;
      this.address = blackbox.address.hex;
    },

    async loadService(address) {
      // 还是需要先连接
      if(!this.flag_connect){
        await this.connectToOasis();
      }
      const blackbox = await oasis.Service.at(new oasis.Address(address));
      this.blackbox = blackbox;
    },

    async store(){
      this.blackbox.store('this works!@@@');
    },

    async fetch(){
      this.secret = await this.blackbox.fetch();
    }

  }
}
</script>

<style>
.explain_panel {
  font-size: 14px;
  border: 2px;
  border: 1px solid #d4d4d4;
  /*margin-left: 100px;*/
  padding: 20px;
  position: relative;
}
.line_button {
  position: relative;
  top: 15px;
}
.block_message {
  margin-bottom: 10px;
}
</style>