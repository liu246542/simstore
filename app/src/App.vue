<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <simstore quto="Test Case #1" name="张三"/>
    <simstore quto="Test Case #2" name="李四"/>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import simstore from './components/simstore.vue'

export default {
  name: 'app',
  components: {
    simstore
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

.qutos {
  width: 400px;
  float: left;
  padding: 5px;
}

.danger-region {
  color: red;
}
</style>
