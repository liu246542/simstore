<template>
  <v-col class="sender" :xs="24" :sm="12" :md="12" :lg="12">
    <h2>{{ name }}</h2>
    <br/>
    <v-row class="block_message">
      <v-col span="1">        
      </v-col>
      <v-col span="8">
        <v-alert type="success" show-icon>
          Here is some Info
        </v-alert>
      </v-col>
      <v-col span="2">
        <div class="lines-horizontal">
        </div>
      </v-col>
      <v-col span="2">
        <v-button class="line_button" type="primary" shape="circle" icon="link" v-on:click="connectToOasis"></v-button>
      </v-col>
      <v-col span="8">
        <div class="explain_panel">Step 1. Connect</div>
      </v-col>
    </v-row>

    <v-row class="block_message">
      <v-col span="1">        
            </v-col>
            <v-col span="8">
              <v-alert type="success" show-icon>
                Here is some Info
              </v-alert>
            </v-col>
            <v-col span="2">
              <div class="lines-horizontal">
              </div>
            </v-col>
      <v-col span="2">
        <v-button class="line_button" type="primary" shape="circle" icon="cloud-upload-o" v-on:click="deployService"></v-button>
      </v-col>
      <v-col span="8">
        <div class="explain_panel">Step 2. Deploy</div>
      </v-col>
    </v-row>

    <v-row class="block_message">
      <v-col span="1">        
            </v-col>
            <v-col span="8">
              <v-alert type="success" show-icon>
                Here is some Info
              </v-alert>
            </v-col>
            <v-col span="2">
              <div class="lines-horizontal">
              </div>
            </v-col>
      <v-col span="2">
        <v-button class="line_button" type="primary" shape="circle" icon="save" v-on:click="store"></v-button>
      </v-col>
      <v-col span="8">
        <div class="explain_panel">Step 3. Store</div>
      </v-col>
    </v-row>

    <v-row class="block_message">
      <v-col span="1">        
            </v-col>
            <v-col span="8">
              <v-alert type="success" show-icon>
                Here is some Info
              </v-alert>
            </v-col>
            <v-col span="2">
              <div class="lines-horizontal">
              </div>
            </v-col>
      <v-col span="2">
        <v-button class="line_button" type="primary" shape="circle" icon="download" v-on:click="fetch"></v-button>
      </v-col>
      <v-col span="8">
        <div class="explain_panel">Step 4. Fetch</div>
      </v-col>
    </v-row>

    <br/>
    
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
.explain_panel:before {
    border-bottom: 10px solid transparent;
    border-left: 0px solid #ccc;
    border-right: 10px solid #ccc;
    border-top: 10px solid transparent;
    content: " ";
    display: inline-block;
    position: absolute;
    left: -10px;
    right: auto;
    top: 10px;
}
.explain_panel:after {
    border-bottom: 9px solid transparent;
    border-left: 0 solid #fff;
    border-right: 9px solid #fff;
    border-top: 9px solid transparent;
    content: " ";
    display: inline-block;
    position: absolute;
    left: -9px;
    right: auto;
    top: 11px;
}

.line_button {
  position: relative;
  top: 15px;
}
.block_message {
  margin-bottom: 10px;
}

.lines-horizontal {
  position: relative;
  top: 25px;
  border-top: 1px dashed black;
  left: 10px;
}

</style>