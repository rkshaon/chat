<template>
    <div class="w-4/5 p-4 overflow-y-auto">
        <h2 class="text-lg font-semibold mb-4">Chat History</h2>
        <div v-if="chat">
            <div v-for="(message, index) in chat.messages" :key="index" class="mb-2">
                <div
                    :class="{ 'bg-gray-200 p-2 rounded': message.sender !== 'You', 'bg-blue-200 p-2 rounded': message.sender === 'You' }">
                    <strong>{{ message.sender }}:</strong> {{ message.text }}
                </div>
            </div>
        </div>
        <div v-else>
            <p>Select a chat to view history.</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ChatBox',
    props: {
        chat: {
            type: Object,
            default: null,
        }
    }
}
</script>

<style scoped>
</style>
