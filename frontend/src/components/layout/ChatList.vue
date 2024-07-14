<template>
    <div class="w-1/5 bg-white p-4 border-r overflow-y-auto">
        <h2 class="text-lg font-semibold mb-4">Chat List</h2>
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
