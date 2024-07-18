<template>
    <div class="max-w-2xl mx-auto bg-white p-8 rounded-lg shadow-md">
        <h1 class="text-2xl font-semibold mb-6">Settings</h1>
        <form @submit.prevent="saveSettings">
            <div class="mb-4">
                <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
                <input v-model="user.name" type="text" id="name"
                    class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2" required>
            </div>
            <div class="mb-4">
                <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
                <input v-model="user.email" type="email" id="email"
                    class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2" required>
            </div>
            <div class="mb-4">
                <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
                <input v-model="user.password" type="password" id="password"
                    class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2">
            </div>
            <div class="flex justify-end">
                <button type="submit"
                    class="bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600">Save</button>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    name: 'SettingsComponent',
    data() {
        return {
            user: {
                name: 'Rezaul Karim Shaon',
                email: 'rezaulkarimshaon@example.com',
                password: ''
            }
        };
    },
    methods: {
        saveSettings() {
            // Implement your save logic here
            console.log('Settings saved', this.user);
            alert('Settings saved!');
        }
    }
};
</script>

<style scoped>
/* Add any additional scoped styles here if necessary */
</style>
