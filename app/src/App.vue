<template>
  <div id="app">
    <h1>DEMO</h1>

    <!-- <v-row>
      <v-col class="sender" :xs="24" :sm="12" :md="12" :lg="12">
        <h3> Sender </h3>
      </v-col>

      <v-col class="sender" :xs="24" :sm="12" :md="12" :lg="12">
        <h3> Receiver </h3>
      </v-col>

    </v-row> -->

    

      <sender name="Sender"/>
      <sender name="Receiver"/>
      
    
    
    
    <!-- <simstore quto="Test Case #2" name="李四"/> -->
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
// import simstore from './components/simstore.vue'
import sender from './components/sender.vue'

export default {
  name: 'app',
  components: {
    // simstore
    sender,
  }  
}

// import oasis from '@oasislabs/client';
// let gateway = oasis.gateway.Gateway(
//   'ws://localhost:8546',
//   oasis.Wallet.fromMnemonic('range drive remove bleak mule satisfy mandate east lion minimum unfold ready'),
//   );
// oasis.setGateway(gateway);


</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.qutos {
  width: 400px;
  float: left;
  padding: 5px;
}

.danger-region {
  color: red;
}
</style>
