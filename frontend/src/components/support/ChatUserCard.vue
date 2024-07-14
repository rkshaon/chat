<template>
    <div @click="selectChat(user)" class="p-2 cursor-pointer hover:bg-gray-200 rounded-lg">
        <h3 class="text-lg font-semibold">{{ user.name }}</h3>
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
