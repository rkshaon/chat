<template>
    <div @click="selectChat(user)"
        class="flex items-center p-2 cursor-pointer hover:bg-gray-200 rounded-lg transition duration-200 ease-in-out shadow-lg">
        <img :src="user.avatar" alt="User Avatar" class="w-12 h-12 rounded-lg mr-4" />
        <div>
            <h5 class="text-base font-semibold">{{ user.name }}</h5>
            <p class="italic text-sm">Last message in Italic form.</p>
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
