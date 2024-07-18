<template>
    <div>
        <NavBar />
        <router-view></router-view>
    </div>
</template>

<script>
import NavBar from '@/components/layout/NavBar.vue';

export default {
    name: 'BaseLayout',
    components: {
        NavBar,
    }
}
</script>