import { createRouter, createWebHistory } from 'vue-router'
// import AboutView from '../views/AboutView.vue'

import LandingPage from '../views/LandingPage.vue'
import AboutPage from '../views/AboutPage.vue'
import ContactPage from '../views/ContactPage.vue'
import ShopPage from '../views/ShopPage.vue'
import ShopProductPage from '../views/ShopProductPage.vue'
import CartPage from '../views/CartPage.vue'
import CartCheckoutPage from '../views/CartCheckoutPage.vue'
import PaymentSuccessPage from '../views/PaymentSuccessPage.vue'
import StaffLoginPage from '../views/StaffLoginPage.vue'
import ProfilePage from '../views/ProfilePage.vue'
import StaffLandingPage from '../views/StaffLandingPage.vue'
import StaffSettingPageAdd from '../views/StaffSettingPageAdd.vue'
import UserLogin from '../views/UserLogin.vue'


import Register from '../views/Register.vue'



import navBar from "../components/pageNavBar.vue"

const routes = [
  {
    path: "/",
    component: navBar,
    children: [
      {
        path: '/',
        name: 'Home',
        component: LandingPage,
        meta: {requiredAuthorization: false}
      }, 
      {
        path: '/shop',
        name: 'Shop',
        component: ShopPage,
        meta: {requiredAuthorization: false}
      },
      {
        path: '/about',
        name: 'About',
        component: AboutPage,
        meta: {requiredAuthorization: false}
      },
      {
        path: '/contact',
        name: 'Contact Us',
        component: ContactPage,
        meta: {requiredAuthorization: false}
      },
      {
        path: '/cart',
        name: 'Cart',
        component: CartPage,
        meta: {requiredAuthorization: false}
      },
      {
        path: '/login',
        name: 'Login',
        component: StaffLoginPage,
        meta: {requiredAuthorization: false}
      },
      {
        path: '/profile',
        name: 'Profile',
        component: ProfilePage,
        meta: {requiredAuthorization: false}
      },
      {
        path: '/shopProduct',
        name: 'Shop Product',
        component: ShopProductPage,
        meta: {requiredAuthorization: false}
      },
      {
        path: '/cartCheckout',
        name: 'Cart Checkout',
        component: CartCheckoutPage,
        meta: {requiredAuthorization: false}
      },
      {
        path: '/paymentSuccess',
        name: "Payment Success",
        component: PaymentSuccessPage,
        meta: {requiredAuthorization: false}
      },
      {
        path: '/StaffLandingPage',
        name: "Staff Landing Page",
        component: StaffLandingPage,
        meta: {requiredAuthorization: false}
      },
      {
        path: '/Register',
        name: "Register",
        component: Register,
        meta: {requiredAuthorization: false}
      },
      {
        path: '/StaffSettingPageAdd',
        name: "Staff Setting Page Add",
        component: StaffSettingPageAdd,
        meta: {requiredAuthorization: false}
      },
      {
        path: '/UserLogin',
        name: "User Login",
        component: UserLogin,
        meta: {requiredAuthorization: false}
      }
    ]
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
