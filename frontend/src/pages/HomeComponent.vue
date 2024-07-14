<template>
  <div class="flex flex-col h-screen">
    <NavBar />
    <div class="flex h-full bg-gray-100 rounded-lg shadow-lg">
      <ChatList :chatList="chatList" @selectedChat="selectChat" />
      <ChatBox :chat="selectedChat" />
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/layout/NavBar.vue';
import ChatList from '@/components/layout/ChatList.vue';
import ChatBox from '@/components/layout/ChatBox.vue';

export default {
  name: 'HomeComponent',
  components: {
    NavBar,
    ChatList,
    ChatBox,
  },
  data() {
    return {
      chatList: [
        { name: 'Rezaul Karim Shaon', messages: [{ sender: 'User 1', text: 'Hello!' }, { sender: 'You', text: 'Hi!' }] },
        { name: 'Nesaruddin Sikdar Nishad', messages: [{ sender: 'User 2', text: 'How are you?' }, { sender: 'You', text: 'I am good, thanks!' }] },
        { name: 'Rifat Hossain', messages: [{ sender: 'User 2', text: 'How are you?' }, { sender: 'You', text: 'I am good, thanks!' }] },
        { name: 'Jahidul Islam', messages: [{ sender: 'User 2', text: 'How are you?' }, { sender: 'You', text: 'I am good, thanks!' }] },
        { name: 'Rakib Hasan', messages: [{ sender: 'User 2', text: 'How are you?' }, { sender: 'You', text: 'I am good, thanks!' }] },
        { name: 'Hasib Ahmed', messages: [{ sender: 'User 2', text: 'How are you?' }, { sender: 'You', text: 'I am good, thanks!' }] },
        { name: 'Anwar Hosain', messages: [{ sender: 'User 2', text: 'How are you?' }, { sender: 'You', text: 'I am good, thanks!' }] },
        { name: 'Zamil Akhondo', messages: [{ sender: 'User 2', text: 'How are you?' }, { sender: 'You', text: 'I am good, thanks!' }] },
        // Add more chat data as needed
      ],
      selectedChat: null
    };
  },
  methods: {
    selectChat(chat) {
      this.selectedChat = chat;
    }
  }
}
</script>

<style scoped>
/* Add any additional scoped styles here if necessary */
</style>
