import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import awsConfig from "./aws-exports.js"
import Auth from "@aws-amplify/auth"
// import Auth from "aws-amplify"
import "@aws-amplify/ui-vue/styles.css"
import '../node_modules/bootstrap/dist/css/bootstrap.min.css'
import '../node_modules/bootstrap/dist/js/bootstrap.bundle.min.js'
import 'bootstrap'
import './assets/css/templatemo.css'
import "bootstrap-icons/font/bootstrap-icons.json"

Auth.configure(awsConfig);

createApp(App)
    .provide('$fetch', fetch)
    .use(store)
    .use(router)
    .mount('#app')
