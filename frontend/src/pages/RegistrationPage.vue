<template>
    <div class="min-h-screen flex items-center justify-center bg-gray-100">
        <div class="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
            <h2 class="text-2xl font-bold mb-6 text-center">Registration</h2>
            <form @submit.prevent="login">
                <div class="mb-4">
                    <label for="name" class="block text-gray-700">Full Name</label>
                    <input type="text" id="name" v-model="name" class="mt-2 p-2 w-full border rounded" required />
                </div>
                <div class="mb-4">
                    <label for="email" class="block text-gray-700">Email</label>
                    <input type="email" id="email" v-model="email" class="mt-2 p-2 w-full border rounded" required />
                </div>
                <div class="mb-4">
                    <label for="username" class="block text-gray-700">Username</label>
                    <input type="text" id="username" v-model="username" class="mt-2 p-2 w-full border rounded"
                        required />
                </div>
                <div class="mb-6">
                    <label for="password" class="block text-gray-700">Password</label>
                    <input type="password" id="password" v-model="password" class="mt-2 p-2 w-full border rounded"
                        required />
                </div>
                <button type="submit" class="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600"
                    @click="register">
                    Sign Up
                </button>
            </form>
        </div>
    </div>
</template>

<script>
import { registration } from '@/services/userAPIService';
import { useToast } from "vue-toastification";

export default {
    name: 'RegistrationPage',
    data() {
        return {
            name: '',
            email: '',
            username: '',
            password: '',
        };
    },
    methods: {
        async register() {
            const userData = {
                name: this.name,
                email: this.email,
                username: this.username,
                password: this.password,
            };
            const toast = useToast();
            console.log('User Data:', userData);
            console.log('Ok');
            toast.info('Hello...');
            try {
                const response = await registration(userData);
                console.log(response.data);
            } catch (error) {
                console.log(error.response);
                console.log(error.response.status);
                console.log(error.response.data);
                toast.error('Failed.');
            }
            
            // console.log(response);
            // console.log('Registration successful:', response.data);
            // await this.register(userData);
            // if (!this.registrationError) {
            //     // Handle successful registration (e.g., navigate to another page)
            // }
        },
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