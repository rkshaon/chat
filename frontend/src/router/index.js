import { createRouter, createWebHistory } from "vue-router";

import BaseLayout from "@/BaseLayout";
import LoginPage from "@/pages/LoginPage.vue";
import RegistrationPage from "@/pages/RegistrationPage.vue";
import HomePage from "@/pages/HomePage.vue";
import ProfilePage from "@/pages/ProfilePage.vue";
import SettingsPage from "@/pages/SettingsPage.vue";

const routes = [
  {
    path: "/",
    component: BaseLayout,
    children: [
      {
        path: "login",
        name: "login",
        component: LoginPage,
      },
      {
        path: "registration",
        name: "registration",
        component: RegistrationPage,
      },
      {
        path: "",
        name: "home",
        component: HomePage,
      },
      {
        path: "profile",
        name: "profile",
        component: ProfilePage,
      },
      {
        path: "settings",
        name: "settings",
        component: SettingsPage,
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;