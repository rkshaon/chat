<template>
    <div class="min-h-screen flex items-center justify-center bg-gray-100">
        <div class="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
            <h2 class="text-2xl font-bold mb-6 text-center">Login</h2>
            <form @submit.prevent="login">
                <div class="mb-4">
                    <label for="email" class="block text-gray-700">Email</label>
                    <input type="email" id="email" v-model="email" class="mt-2 p-2 w-full border rounded" required />
                </div>
                <div class="mb-6">
                    <label for="password" class="block text-gray-700">Password</label>
                    <input type="password" id="password" v-model="password" class="mt-2 p-2 w-full border rounded"
                        required />
                </div>
                <button type="submit" class="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600">
                    Login
                </button>
            </form>
            <div class="text-center mt-4">
                <p class="text-gray-700">
                    Don't have an account?
                    <router-link to="/registration" class="text-blue-500 hover:underline">Register here.</router-link>
                </p>
            </div>

        </div>
    </div>
</template>

<script>

export default {
    name: 'LoginPage',
    data() {
        return {
        };
    },
    methods: {
    }
}
</script>

<style scoped>
#login-container {
    width: 100%;
    height: 100vh;
    background-color: #092f1e;
}

#login-deep-container {
    width: 150vh;
    padding-top: 10vh;
    padding-bottom: 10vh;
    background-color: #0A3622;
}
</style>