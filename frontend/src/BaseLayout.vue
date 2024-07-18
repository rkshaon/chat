<template>
    <div>
        <NavBar />
        <router-view></router-view>
    </div>
</template>

<script>
import NavBar from '@/components/layout/NavBar.vue';
// import router from './router';
// import HomeComponent from '@/pages/HomeComponent.vue';

export default {
    name: 'BaseLayout',
    components: {
        NavBar,
    }
}
</script>