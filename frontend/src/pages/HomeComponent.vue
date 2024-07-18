<template>
  <div class="flex flex-col">
    
    <div class="flex bg-gray-100 rounded-lg shadow-lg">
      <ChatList :chatList="chatList" @selectedChat="selectChat" />
      <ChatBox :chat="selectedChat" />
    </div>
  </div>
</template>

<script>
// import NavBar from '@/components/layout/NavBar.vue';
import ChatList from '@/components/layout/ChatList.vue';
import ChatBox from '@/components/layout/ChatBox.vue';

import { formatDateTime } from '@/helpers/dateTimeFormat.js';

export default {
  name: 'HomeComponent',
  components: {
    // NavBar,
    ChatList,
    ChatBox,
  },
  data() {
    return {
      chatList: [
        {
          name: 'Rezaul Karim Shaon',
          avatar: 'https://avatars.githubusercontent.com/u/20625263?v=4',
          messages: [{ sender: 'User 1', text: 'Hello!' }, { sender: 'You', text: 'Hi!' }],
          isOnline: true,
          lastMessage: 'I am leaving...',
        },
        {
          name: 'Nesaruddin Sikdar Nishad',
          avatar: 'https://scontent.fdac45-1.fna.fbcdn.net/v/t39.30808-6/398146330_3592757867713068_6544141103770666760_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=a5f93a&_nc_eui2=AeGiiB06KWYdWP54aU1BBM4eIuvETosTIzYi68ROixMjNvM86vcXfL2IYJDMbVjTfqjG9W3ARY-qdlwL-PE4yJXK&_nc_ohc=OpaeKQ3vPKkQ7kNvgG8iDNZ&_nc_ht=scontent.fdac45-1.fna&oh=00_AYCRMyZkoKL9aA8vZKnvKnIDWiUeOWRV1_QA-ATbBg1IHw&oe=6699FA34',
          messages: [{ sender: 'User 2', text: 'How are you?' }, { sender: 'You', text: 'I am good, thanks!' }],
          isOnline: true,
          lastMessageTime: formatDateTime(new Date('2024-07-19T10:30:00')),
          lastMessage: 'I am leaving...',
        },
        {
          name: 'Rifat Hossain',
          avatar: 'https://avatars.githubusercontent.com/u/35008232?v=4',
          messages: [{ sender: 'User 3', text: 'How are you?' }, { sender: 'You', text: 'I am good, thanks!' }],
          isOnline: false,
          lastMessageTime: formatDateTime(new Date('2024-07-19T10:30:00')),
          lastMessage: 'I am leaving...',
        },
        {
          name: 'Jahidul Islam',
          avatar: 'https://scontent.fdac45-1.fna.fbcdn.net/v/t39.30808-1/428710199_2726229160867998_2141775386788764673_n.jpg?stp=dst-jpg_p200x200&_nc_cat=106&ccb=1-7&_nc_sid=0ecb9b&_nc_eui2=AeGF7kSFd1jhZXNZUA9DiBOWoAFxiCHCpD2gAXGIIcKkPfgi-MDa1y3WmKPLqGrEzm-tpXEhIB3-in1VMHMTvN7E&_nc_ohc=8viBawBmIuwQ7kNvgFDO_F-&_nc_ht=scontent.fdac45-1.fna&oh=00_AYDzeL3pPl2W1vdC4kGLKT7Bb8pSpDn6JPijHNs0i4qyHA&oe=669A1C27',
          messages: [{ sender: 'User 4', text: 'Are you looking for me?' }, { sender: 'You', text: 'Not at all.' }],
          isOnline: true,
          lastMessage: 'I am leaving...',
        },
        {
          name: 'Rakib Hasan',
          avatar: 'https://avatars.githubusercontent.com/u/33759162?v=4',
          messages: [{ sender: 'User 5', text: 'Where are you?' }, { sender: 'You', text: 'At home, why?' }],
          isOnline: false,
          lastMessageTime: formatDateTime(new Date('2024-07-19T10:30:00')),
          lastMessage: 'I am leaving...',
        },
        {
          name: 'Hasib Ahmed',
          avatar: 'https://avatars.githubusercontent.com/u/30392450?v=4',
          messages: [{ sender: 'User 6', text: 'I wanted to lost in heaven.' }, { sender: 'You', text: 'You are always in heaven.' }],
          isOnline: true,
          lastMessage: 'I am leaving...',
        },
        {
          name: 'Anwar Hosain',
          avatar: 'https://scontent.fdac45-1.fna.fbcdn.net/v/t39.30808-1/379564045_2676582715823287_8141496378084479658_n.jpg?stp=dst-jpg_s200x200&_nc_cat=100&ccb=1-7&_nc_sid=0ecb9b&_nc_eui2=AeEielzL_U1lHTkUVAFt9I72IdE_TjDsaN4h0T9OMOxo3kDVxgHwrOibTAe0WLA_iLR5cfaWkaiz_kmlu60YyPQt&_nc_ohc=c3Zn0-MLcLcQ7kNvgHnkpyO&_nc_ht=scontent.fdac45-1.fna&oh=00_AYBo4td7LZ7w3MWpNCm5tyEzSSFGrkYoJUqlvYEltWyXwg&oe=6699F233',
          messages: [{ sender: 'User 7', text: 'I am in pain...' }, { sender: 'You', text: 'Part of life.' }],
          isOnline: true,
          lastMessage: 'I am leaving...',
        },
        {
          name: 'Zamil Akhondo',
          avatar: 'https://scontent.fdac45-1.fna.fbcdn.net/v/t39.30808-1/335382131_1355086355063182_838815564895351162_n.jpg?stp=dst-jpg_p200x200&_nc_cat=111&ccb=1-7&_nc_sid=50d2ac&_nc_eui2=AeH4Xf3R0ZTg8eFeQ_twOe3E-w3Xzw8mhN_7DdfPDyaE3zf6SodTPoGKDp1Pj2wmZXPiQg56vtWOrWP79KyZxCbh&_nc_ohc=w-S0Zu3S4wUQ7kNvgGgERAv&_nc_ht=scontent.fdac45-1.fna&oh=00_AYDjSdIMA8EApQGpLmOHSFX6qBB2vJ71e7xbLR8seJWL3g&oe=669A0C3C',
          messages: [{ sender: 'User 8', text: 'Text me bro!!!' }, { sender: 'You', text: 'Ok, I will...' }],
          isOnline: false,
          lastMessageTime: formatDateTime(new Date('2024-07-19T10:30:00')),
          lastMessage: 'I am leaving...',
        },
        {
          name: 'Rezaul Karim Shaon',
          avatar: 'https://avatars.githubusercontent.com/u/20625263?v=4',
          messages: [{ sender: 'User 1', text: 'Hello!' }, { sender: 'You', text: 'Hi!' }],
          isOnline: true,
          lastMessage: 'I am leaving...',
        },
        {
          name: 'Nesaruddin Sikdar Nishad',
          avatar: 'https://scontent.fdac45-1.fna.fbcdn.net/v/t39.30808-6/398146330_3592757867713068_6544141103770666760_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=a5f93a&_nc_eui2=AeGiiB06KWYdWP54aU1BBM4eIuvETosTIzYi68ROixMjNvM86vcXfL2IYJDMbVjTfqjG9W3ARY-qdlwL-PE4yJXK&_nc_ohc=OpaeKQ3vPKkQ7kNvgG8iDNZ&_nc_ht=scontent.fdac45-1.fna&oh=00_AYCRMyZkoKL9aA8vZKnvKnIDWiUeOWRV1_QA-ATbBg1IHw&oe=6699FA34',
          messages: [{ sender: 'User 2', text: 'How are you?' }, { sender: 'You', text: 'I am good, thanks!' }],
          isOnline: true,
          lastMessage: 'I am leaving...',
        },
        {
          name: 'Rifat Hossain',
          avatar: 'https://avatars.githubusercontent.com/u/35008232?v=4',
          messages: [{ sender: 'User 3', text: 'How are you?' }, { sender: 'You', text: 'I am good, thanks!' }],
          isOnline: true,
          lastMessage: 'I am leaving...',
        },
        {
          name: 'Jahidul Islam',
          avatar: 'https://scontent.fdac45-1.fna.fbcdn.net/v/t39.30808-1/428710199_2726229160867998_2141775386788764673_n.jpg?stp=dst-jpg_p200x200&_nc_cat=106&ccb=1-7&_nc_sid=0ecb9b&_nc_eui2=AeGF7kSFd1jhZXNZUA9DiBOWoAFxiCHCpD2gAXGIIcKkPfgi-MDa1y3WmKPLqGrEzm-tpXEhIB3-in1VMHMTvN7E&_nc_ohc=8viBawBmIuwQ7kNvgFDO_F-&_nc_ht=scontent.fdac45-1.fna&oh=00_AYDzeL3pPl2W1vdC4kGLKT7Bb8pSpDn6JPijHNs0i4qyHA&oe=669A1C27',
          messages: [{ sender: 'User 4', text: 'Are you looking for me?' }, { sender: 'You', text: 'Not at all.' }],
          isOnline: true,
          lastMessage: 'I am leaving...',
        },
        {
          name: 'Rakib Hasan',
          avatar: 'https://avatars.githubusercontent.com/u/33759162?v=4',
          messages: [{ sender: 'User 5', text: 'Where are you?' }, { sender: 'You', text: 'At home, why?' }],
          isOnline: true,
          lastMessage: 'I am leaving...',
        },
        {
          name: 'Hasib Ahmed',
          avatar: 'https://avatars.githubusercontent.com/u/30392450?v=4',
          messages: [{ sender: 'User 6', text: 'I wanted to lost in heaven.' }, { sender: 'You', text: 'You are always in heaven.' }],
          isOnline: false,
          lastMessage: 'I am leaving...',
          lastMessageTime: formatDateTime(new Date('2024-07-19T10:30:00'))
        },
        {
          name: 'Anwar Hosain',
          avatar: 'https://scontent.fdac45-1.fna.fbcdn.net/v/t39.30808-1/379564045_2676582715823287_8141496378084479658_n.jpg?stp=dst-jpg_s200x200&_nc_cat=100&ccb=1-7&_nc_sid=0ecb9b&_nc_eui2=AeEielzL_U1lHTkUVAFt9I72IdE_TjDsaN4h0T9OMOxo3kDVxgHwrOibTAe0WLA_iLR5cfaWkaiz_kmlu60YyPQt&_nc_ohc=c3Zn0-MLcLcQ7kNvgHnkpyO&_nc_ht=scontent.fdac45-1.fna&oh=00_AYBo4td7LZ7w3MWpNCm5tyEzSSFGrkYoJUqlvYEltWyXwg&oe=6699F233',
          messages: [{ sender: 'User 7', text: 'I am in pain...' }, { sender: 'You', text: 'Part of life.' }],
          isOnline: false,
          lastMessageTime: formatDateTime(new Date('2024-07-19T10:30:00')),
          lastMessage: 'I am leaving...',
        },
        {
          name: 'Zamil Akhondo',
          avatar: 'https://scontent.fdac45-1.fna.fbcdn.net/v/t39.30808-1/335382131_1355086355063182_838815564895351162_n.jpg?stp=dst-jpg_p200x200&_nc_cat=111&ccb=1-7&_nc_sid=50d2ac&_nc_eui2=AeH4Xf3R0ZTg8eFeQ_twOe3E-w3Xzw8mhN_7DdfPDyaE3zf6SodTPoGKDp1Pj2wmZXPiQg56vtWOrWP79KyZxCbh&_nc_ohc=w-S0Zu3S4wUQ7kNvgGgERAv&_nc_ht=scontent.fdac45-1.fna&oh=00_AYDjSdIMA8EApQGpLmOHSFX6qBB2vJ71e7xbLR8seJWL3g&oe=669A0C3C',
          messages: [{ sender: 'User 8', text: 'Text me bro!!!' }, { sender: 'You', text: 'Ok, I will...' }],
          isOnline: false,
          lastMessageTime: formatDateTime(new Date('2024-07-19T10:30:00')),
          lastMessage: 'I am leaving...',
        },
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
</style>
