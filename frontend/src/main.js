import axios from 'axios';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import vuetify from './plugins/vuetify';


Vue.config.productionTip = false

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:80/';  // the FastAPI backend

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app');
