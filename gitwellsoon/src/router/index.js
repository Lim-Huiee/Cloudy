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
import LoginPage from '../views/LoginPage.vue'

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
        component: LoginPage,
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
      }
    ]
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
