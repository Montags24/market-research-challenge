<script setup>
import { RouterView } from 'vue-router'
import { reactive } from 'vue';

import User from './js/User';
import Chatbot from './js/Chatbot';

// when we are developing using localhost on port 5173 (vue's default port),
// to integrate with the flask backend, we need to modify the port to 5000 (flask default port)
let domainOrigin = window.location.origin
if (domainOrigin.slice(-5) == ":5173") {
  domainOrigin = domainOrigin.replace(":5173", ":5000")
}

const user = reactive(new User(domainOrigin))
const chatbot = reactive(new Chatbot(domainOrigin, user))


</script>

<template>
  <div>
    <!-- Dark overlay -->
    <div class="fixed inset-0 bg-black opacity-50 z-20" v-show="darkOverlay"></div>

    <!-- Header -->
    <header class="relative z-30">
      <!-- Include NavBar component for navigation -->
      <div class="fixed top-0 left-0 right-0">
        <NavBar :user="user" @toggleModalVisibility="toggleModal" />
        <LoginModal :visible="modalVisible" :user="user" @toggleModalVisibility="toggleModal"
          @toggleRegisterModal="toggleRegisterModal">
        </LoginModal>
        <RegisterModal :user :registerModalVisible="registerModalVisible"
          @toggleRegisterModalVisibility="toggleRegisterModal">
        </RegisterModal>
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

export default {
  components: {
    NavBar,
    LoginModal,
    RegisterModal
  },
  data() {
    return {
      modalVisible: false,
      registerModalVisible: false,
    }
  },
  methods: {
    toggleModal() {
      this.modalVisible = !this.modalVisible
    },
    toggleRegisterModal() {
      this.modalVisible = false
      this.registerModalVisible = !this.registerModalVisible
    }
  },
  computed: {
    darkOverlay() {
      return this.modalVisible || this.registerModalVisible
    }
  },
}
</script>

<!-- Scoped styles for this component -->
<style scoped>
/* Add styles for header, main, and footer if needed */
</style>
