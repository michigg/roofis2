<template>
  <div id="app">
    <roofis2/>
  </div>
</template>

<script>
import Roofis2 from "./components/Roofis2";

export default {
  name: 'App',
  components: {
    Roofis2,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
