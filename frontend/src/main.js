// import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './index.css'

import { OhVueIcon, addIcons } from 'oh-vue-icons'
import { IoSend } from 'oh-vue-icons/icons'

import VueChatScroll from 'vue3-chat-scroll'

addIcons(IoSend)

const app = createApp(App)

app.use(router)
app.use(VueChatScroll)

app.component('v-icon', OhVueIcon)

app.mount('#app')
