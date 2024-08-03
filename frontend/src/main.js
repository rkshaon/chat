import { createApp } from 'vue'
import App from './App.vue'
import router from '@/router';
import store from '@/store';
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";
import '@/assets/tailwind.css';

const app = createApp(App);

app.use(router);
app.use(store);
app.use(Toast, {
  duration: 1000,
  position: "top-right",
});
app.mount("#app");
