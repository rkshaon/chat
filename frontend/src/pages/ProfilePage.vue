<template>
    <div class="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl">
        <div class="md:flex">
            <div class="md:flex-shrink-0">
                <img class="h-48 w-full object-cover md:w-48" src="https://avatars.githubusercontent.com/u/20625263?v=4"
                    alt="User Avatar">
            </div>
            <div class="p-8">
                <div class="uppercase tracking-wide text-sm text-indigo-500 font-semibold">Profile</div>
                <h1 class="block mt-1 text-lg leading-tight font-medium text-black">Rezaul Karim Shaon</h1>
                <p class="mt-2 text-gray-500">rezaulkarimshaon@example.com</p>
                <p class="mt-2 text-gray-500">A passionate software developer with expertise in web development and a
                    love for creating interactive and dynamic user experiences.</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ProfilePage',
    props: {
        user: {
            type: Object,
            default: () => ({
                name: 'Rezaul Karim Shaon',
                avatar: 'https://avatars.githubusercontent.com/u/20625263?v=4',
                email: 'rezaulkarimshaon@example.com',
                bio: 'A passionate software developer with expertise in web development and a love for creating interactive and dynamic user experiences.'
            })
        }
    }
};
</script>

<style scoped>
/* Add any additional scoped styles here if necessary */
</style>
