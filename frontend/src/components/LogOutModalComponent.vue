<template>
    <div class="fixed inset-0 flex items-center justify-center bg-gray-900 bg-opacity-50 z-50">
        <div class="bg-white rounded-lg overflow-hidden shadow-xl max-w-md w-full">
            <div class="p-6">
                <h2 class="text-xl font-semibold mb-4">{{ title }}</h2>
                <p class="text-gray-600 mb-6">{{ message }}</p>
                <div class="flex justify-end">
                    <button @click="$emit('cancel')"
                        class="bg-gray-500 text-white py-2 px-4 rounded-md mr-2 hover:bg-gray-600">Cancel</button>
                    <button @click="$emit('confirm')"
                        class="bg-red-500 text-white py-2 px-4 rounded-md hover:bg-red-600">Confirm</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'LogOutModalComponent',
    props: {
        title: {
            type: String,
            required: true
        },
        message: {
            type: String,
            required: true
        }
    }
};
</script>

<style scoped>
/* Add any additional scoped styles here if necessary */
</style>
