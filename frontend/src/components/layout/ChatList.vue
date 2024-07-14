<template>
    <div class="w-1/5 bg-white p-4 border-r overflow-y-auto">
        <h2 class="text-lg font-semibold mb-4">Chat List</h2>
        <ul>
            <li v-for="(chat, index) in chatList" :key="index" @click="selectChat(chat)"
                class="p-2 cursor-pointer hover:bg-gray-200">
                {{ chat.name }}
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'ChatList',
    props: {},
}
</script>