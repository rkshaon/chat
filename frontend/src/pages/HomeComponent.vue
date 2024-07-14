<template>
  <div class="flex flex-col h-screen">
    <NavBar />
  </div>
</template>

<script>
import NavBar from '@/components/layout/NavBar.vue';

export default {
  name: 'HomeComponent',
  props: {},
  components: {
    NavBar,
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
