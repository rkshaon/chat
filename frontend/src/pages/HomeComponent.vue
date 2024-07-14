<template>
  <div class="flex flex-col h-screen">
    <NavBar />
    <div class="flex h-full bg-gray-100 rounded-lg shadow-lg">
      <ChatList />
      <ChatBox />
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/layout/NavBar.vue';
import ChatList from '@/components/layout/ChatList.vue';
import ChatBox from '@/components/layout/ChatBox.vue';

export default {
  name: 'HomeComponent',
  props: {},
  components: {
    NavBar,
    ChatList,
    ChatBox,
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
