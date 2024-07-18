<template>
  <div class="h-screen flex flex-col h-full">
    <NavBar />
    <HomeComponent />
  </div>
</template>

<script>
import HomeComponent from '@/pages/HomeComponent.vue';
import NavBar from '@/components/layout/NavBar.vue';

export default {
  name: 'App',
  components: {
    NavBar,
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
