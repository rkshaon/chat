<template>
    <nav class="bg-gray-800 text-white p-4 flex justify-between items-center px-12">
        <router-link to="/">
            <div class="flex items-center space-x-4">
                <img src="https://scontent.fdac45-1.fna.fbcdn.net/v/t39.30808-1/397921081_24931385069794398_4597236671743006825_n.jpg?stp=c0.67.200.200a_dst-jpg_p200x200&_nc_cat=100&ccb=1-7&_nc_sid=50d2ac&_nc_eui2=AeGdZRfswEAo8CtzRUMiZBzSlpLCKWbPnJ2WksIpZs-cnfZ6wzzITCgq0k4iBprX9xC66cx61hTD1boHLtqIY6TL&_nc_ohc=PWUauD4D7tkQ7kNvgGuFMmc&_nc_ht=scontent.fdac45-1.fna&oh=00_AYAX6-q75NZSHsLWG-RBzcYncbviuNUtbz3qz6hqXAIi-A&oe=669A0FC2"
                    alt="Company Logo" class="w-10 h-10 rounded-full" />
                <span class="text-xl font-bold">Chat</span>
            </div>
        </router-link>
        <div class="flex items-center space-x-4 relative">
            <router-link to="/profile">
                <img src="https://avatars.githubusercontent.com/u/20625263?v=4" alt="User Avatar"
                    class="w-10 h-10 rounded-full" />
            </router-link>
            <div @click="toggleDropdown" class="cursor-pointer">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                    xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M12 6h.01M12 12h.01M12 18h.01"></path>
                </svg>
            </div>
            <div v-if="dropdownOpen" class="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg py-1 z-20">
                <router-link to="/profile"
                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Profile</router-link>
                <router-link to="/settings"
                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Settings</router-link>
                <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Logout</a>
            </div>
        </div>
        <LogOutModalComponent v-if="showLogoutModal" title="Confirm Logout" message="Are you sure you want to logout?"
            @confirm="logout" @cancel="showLogoutModal = false" />
    </nav>
</template>

<script>
import LogOutModalComponent from "@/components/LogOutModalComponent.vue";

export default {
    name: 'NavBar',
    components: {
        LogOutModalComponent,
    },
    data() {
        return {
            dropdownOpen: false,
            showLogoutModal: false
        };
    },
    methods: {
        toggleDropdown() {
            this.dropdownOpen = !this.dropdownOpen;
        },
        handleClickOutside(event) {
            if (!this.$el.contains(event.target)) {
                this.dropdownOpen = false;
            }
        },
        logout() {
            this.showLogoutModal = false;
            this.$router.push('/logout');
        }
    },
    mounted() {
        document.addEventListener('click', this.handleClickOutside);
    },
    beforeUnmount() {
        document.removeEventListener('click', this.handleClickOutside);
    }
};
</script>

<style scoped>
/* Add any additional scoped styles here if necessary */
</style>
