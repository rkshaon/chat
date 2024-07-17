<template>
    <div class="flex items-center justify-center h-full">
        <div class="text-center p-6 bg-white shadow-md rounded-lg border border-gray-200">
            <svg class="w-16 h-16 text-gray-400 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M15 12h2m4 0h-6m6 0H3m4 0h6m-6 0H9m0 0a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"></path>
            </svg>
            <h2 class="text-2xl font-semibold text-gray-700">No Chat Selected</h2>
            <p class="text-gray-500 mt-2">Please select a chat to start messaging.</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'NoChatSelected',
};
</script>

<style scoped>
/* Add any additional scoped styles here if necessary */
</style>
