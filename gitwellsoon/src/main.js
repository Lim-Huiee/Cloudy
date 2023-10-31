import './assets/main.css'
import './assets/css/bootstrap.min.css'
import './assets/css/templatemo.css'
import './assets/css/custom.css'


import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import awsConfig from "../aws-exports"
import Auth from "@aws-amplify/auth"
// import Auth from "aws-amplify"
import "@aws-amplify/ui-vue/styles.css"

Auth.configure(awsConfig);

const app = createApp(App)

app.use(router)

app.mount('#app')
