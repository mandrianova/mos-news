import axios from 'axios';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import vuetify from './plugins/vuetify';


Vue.config.productionTip = false;

axios.defaults.withCredentials = false;
axios.defaults.baseURL = 'http://217.28.231.202/';  // the FastAPI backend

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app');
