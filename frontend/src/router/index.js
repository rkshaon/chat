import { createRouter, createWebHistory } from "vue-router";

import BaseLayout from "@/BaseLayout";
import HomeComponent from "@/pages/HomeComponent.vue";
import ProfileComponent from "@/pages/ProfileComponent.vue";
import SettingsComponent from "@/pages/SettingsComponent.vue";

const routes = [
    {
        path: "/",
        component: BaseLayout,
        children: [
            {
                path: "",
                name: "home",
                component: HomeComponent,
            },
            {
                path: "profile",
                name: "profile",
                component: ProfileComponent,
            },
            {
                path: "settings",
                name: "settings",
                component: SettingsComponent,
            }
        ]
    },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;