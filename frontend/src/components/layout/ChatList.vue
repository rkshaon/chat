<template>
    <div class="w-1/5 bg-white p-4 border-r overflow-y-auto">
        <div class="mb-4">
            <div class="relative">
                <input type="text" v-model="searchQuery" placeholder="Search..."
                    class="w-full p-2 pl-10 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500" />
                <svg class="w-5 h-5 absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" fill="none"
                    stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M21 21l-4.35-4.35m1.75-5.4a7.5 7.5 0 11-15 0 7.5 7.5 0 0115 0z"></path>
                </svg>
            </div>
        </div>
        <ul>
            <li v-for="(chat, index) in chatList" :key="index" class="p-2 cursor-pointer hover:bg-gray-200">
                <ChatUserCard :user="chat" :selectChat="selectChat" />
            </li>
        </ul>
    </div>
</template>

<script>
import ChatUserCard from '@/components/support/ChatUserCard.vue';

export default {
    name: 'ChatList',
    components: {
        ChatUserCard,
    },
    props: {
        chatList: {
            type: Array,
            required: true,
        },
    },
    methods: {
        selectChat(chat) {
            this.$emit('selectedChat', chat);
        }
    }
}
</script>

<style scoped>
</style>
