<template>
    <div @click="selectChat(user)"
        class="flex items-center p-2 cursor-pointer rounded-lg hover:rounded-2xl transition duration-200 ease-in-out shadow-lg hover:shadow-2xl transform hover:-translate-y-1 hover:bg-gray-200">
        <img :src="user.avatar" alt="User Avatar" class="w-12 h-12 rounded-lg mr-4" />
        <div class="flex-1">
            <div class="flex justify-between items-center">
                <h5 class="text-base font-semibold">{{ user.name }}</h5>
                <span v-if="user.isOnline" class="w-3 h-3 bg-green-500 rounded-full"></span>
                <span v-else class="text-xs text-gray-500">{{ user.lastMessageTime }}</span>
            </div>
            <p class="italic text-sm">{{ user.lastMessage }}</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ChatUserCard',
    props: {
        user: {
            type: Object,
            required: true
        },
        selectChat: {
            type: Function,
            required: true
        }
    }
}
</script>

<style scoped>
/* Add any additional scoped styles here if necessary */
</style>
