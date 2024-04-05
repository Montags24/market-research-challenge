<script setup>
import { RouterView } from 'vue-router'
import { reactive } from 'vue';
import Nango from '@nangohq/frontend';

import User from './js/User';
import Chatbot from './js/Chatbot';
import TwitchService from './js/TwitchService'
import TiktokService from './js/TiktokService'
import GoogleService from './js/GoogleService'

// when we are developing using localhost on port 5173 (vue's default port),
// to integrate with the flask backend, we need to modify the port to 5000 (flask default port)
let domainOrigin = window.location.origin
if (domainOrigin.slice(-5) == ":5173") {
  domainOrigin = domainOrigin.replace(":5173", ":5000")
}

let nango = new Nango({ publicKey: '0b4ae80f-ff4b-4a9a-abc8-8bd314e2dbf7' });
const user = reactive(new User(domainOrigin))
const chatbot = reactive(new Chatbot(domainOrigin, user))
const twitchService = reactive(new TwitchService(nango, user))
const googleService = reactive(new GoogleService(domainOrigin, user))
const tiktokService = reactive(new TiktokService(nango, user))


</script>

<template>
  <div>
    <!-- Dark overlay for modals-->
    <div class="fixed inset-0 bg-black opacity-50 z-20" v-show="darkOverlay"></div>

    <!-- Header -->
    <header class="relative z-30">
      <!-- Include NavBar component for navigation -->
      <div class="fixed top-0 left-0 right-0">
        <NavBar :user="user" @toggleModalVisibility="toggleModal" @togglePrizeModalVisibility="togglePrizeModal" />
        <LoginModal :visible="modalVisible" :user="user" :twitchService="twitchService" :googleService="googleService"
          :tiktokService="tiktokService" @toggleModalVisibility="toggleModal"
          @toggleRegisterModal="toggleRegisterModal">
        </LoginModal>
        <RegisterModal :user="user" :registerModalVisible="registerModalVisible"
          @toggleRegisterModalVisibility="toggleRegisterModal">
        </RegisterModal>
        <PrizeModal :user="user" :visible="prizeModalVisibility" @toggleModalVisibility="togglePrizeModal"></PrizeModal>
      </div>
    </header>

    <!-- Main content -->
    <main class="pt-[48px] h-screen z-10">
      <RouterView :user="user" :chatbot="chatbot" />
    </main>

    <!-- Footer -->
    <footer class="z-20">
      <!-- Footer content goes here -->
      <!-- <h1>Footer</h1> -->
    </footer>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'
import LoginModal from '@/components/LoginModal.vue';
import RegisterModal from '@/components/RegisterModal.vue';
import PrizeModal from './components/PrizeModal.vue';

export default {
  components: {
    NavBar,
    LoginModal,
    RegisterModal,
    PrizeModal
  },
  data() {
    return {
      modalVisible: false,
      registerModalVisible: false,
      prizeModalVisibility: false
    }
  },
  methods: {
    toggleModal() {
      this.modalVisible = !this.modalVisible
    },
    toggleRegisterModal() {
      this.modalVisible = false
      this.registerModalVisible = !this.registerModalVisible
    },
    togglePrizeModal() {
      this.modalVisible = false
      this.prizeModalVisibility = !this.prizeModalVisibility
    }
  },
  computed: {
    darkOverlay() {
      return this.modalVisible || this.registerModalVisible || this.prizeModalVisibility
    }
  },
}
</script>

<!-- Scoped styles for this component -->
<style scoped>
/* Add styles for header, main, and footer if needed */
</style>
