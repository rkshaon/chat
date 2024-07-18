<template>
  <div class="h-screen flex flex-col h-full">
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: { },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
