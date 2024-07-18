import { createRouter, createWebHistory } from "vue-router";

import BaseLayout from "@/BaseLayout";
import HomeComponent from "@/pages/HomeComponent.vue";
import ProfileComponent from "@/pages/ProfileComponent.vue";

const routes = [
    {
        path: "/",
        component: BaseLayout,
        children: [
            {
                path: "",
                component: HomeComponent,
            },
            {
                path: "profile",
                component: ProfileComponent,
            }
        ]
    },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;