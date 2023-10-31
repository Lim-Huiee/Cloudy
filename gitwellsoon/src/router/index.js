import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '../views/LoginPage.vue'
// import AboutView from '../views/AboutView.vue'

import LandingPage from '../views/LandingPage.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: LandingPage,
    meta: {requiredAuthorization: false}
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage,
    meta: {requiredAuthorization: false}
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
