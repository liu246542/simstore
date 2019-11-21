<template>
  <div id="app">
    <h1>垃圾代码代工厂</h1>
    <center>专注生产垃圾一百年</center>
    <br/>
    <hr/>
    <br/>

    <sender name="Sender"/>
    <sender name="Receiver"/>

  </div>
</template>

<script>

import sender from './components/sender.vue'

export default {
  name: 'app',
  components: {
    sender,
  }  
}

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
</style>
