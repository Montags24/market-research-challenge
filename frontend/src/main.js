// import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './index.css'

import { OhVueIcon, addIcons } from 'oh-vue-icons'
import { IoSend, RiChatVoiceFill } from 'oh-vue-icons/icons'

addIcons(IoSend, RiChatVoiceFill)

const app = createApp(App)

app.use(router)

app.component('v-icon', OhVueIcon)

app.mount('#app')
