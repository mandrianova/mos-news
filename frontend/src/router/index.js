import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Recommendations from '../views/Recommendations.vue'
import Markup from '../views/Markup.vue'
import Documentation from '../views/Documentation.vue'
import About from '../views/About.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: About
  },
  {
    path: '/recommendations',
    name: 'recommendations',
    component: Recommendations
  },
  {
    path: '/markup',
    name: 'markup',
    component: Markup
  },
  {
    path: '/documentation',
    name: 'documentation',
    component: Documentation
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;
