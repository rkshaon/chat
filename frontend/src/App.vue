<template>
  <div class="h-screen flex flex-col h-full">
    <HomeComponent />
  </div>
</template>

<script>
import HomeComponent from '@/pages/HomeComponent.vue';

export default {
  name: 'App',
  components: {
    HomeComponent
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
