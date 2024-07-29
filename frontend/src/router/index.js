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
        meta: {
          title: "Login | Chat",
        },
      },
      {
        path: "registration",
        name: "registration",
        component: RegistrationPage,
        meta: {
          title: "Registration | Chat",
        },
      },
      {
        path: "",
        name: "home",
        component: HomePage,
        meta: {
          title: "Home | Chat",
        },
      },
      {
        path: "profile",
        name: "profile",
        component: ProfilePage,
        meta: {
          title: "Profile | Chat",
        },
      },
      {
        path: "settings",
        name: "settings",
        component: SettingsPage,
        meta: {
          title: "Setting | Chat",
        },
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// This navigation guard runs before each route change
router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'Default Title';
  next();
});

export default router;