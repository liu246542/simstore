<template>
  <div class="qutos">
    <h1>{{ quto }}</h1>
    <p>User {{ name }}</p>
    <span>私钥：</span>
    <input v-model="sk">
    <p class="danger-region" >It works? {{ sk }}</p>

    <span>公钥：</span>
    <input v-model="pk">
    <p class="danger-region">It works? {{ pk }}</p>

    <span>SECRET:</span>
    
  </div>
</template>

<script>
  export default {
    name: 'simstore',
    props: {
      quto: String,
      name: String
    },
    data () {
      return {
        sk: null,
        pk: null
      }
    }
  }
</script>