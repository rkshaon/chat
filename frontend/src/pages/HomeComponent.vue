<template>
  <div class="flex flex-col h-screen">
    <NavBar />
    <div class="flex h-full bg-gray-100 rounded-lg shadow-lg">
      <ChatList />
      <!-- Chat History -->
      <div class="w-4/5 p-4 overflow-y-auto">
        <h2 class="text-lg font-semibold mb-4">Chat History</h2>
        <div v-if="selectedChat">
          <div v-for="(message, index) in selectedChat.messages" :key="index" class="mb-2">
            <div class="bg-gray-200 p-2 rounded">
              <strong>{{ message.sender }}:</strong> {{ message.text }}
            </div>
          </div>
        </div>
        <div v-else>
          <p>Select a chat to view history.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/layout/NavBar.vue';
import ChatList from '@/components/layout/ChatList.vue';

export default {
  name: 'HomeComponent',
  props: {},
  components: {
    NavBar,
    ChatList,
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
