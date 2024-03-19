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
const chatbot = reactive(new Chatbot(domainOrigin))


</script>

<template>
  <div>
    <header class="relative">
      <!-- Include NavBar component for navigation -->
      <div class="fixed top-0 left-0 right-0">
        <NavBar :user="user" />
      </div>
    </header>
    <main class="pt-[48px] h-screen">
      <RouterView :user="user" :chatbot="chatbot" />
    </main>
    <footer>
      <!-- Footer content goes here -->
      <!-- <h1>Footer</h1> -->
    </footer>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'

export default {
  components: {
    NavBar,
  },
  data() {
    return {
      darkMode: false,
    }
  },
  methods: {

  },
}
</script>

<!-- Scoped styles for this component -->
<style scoped>
/* Add styles for header, main, and footer if needed */
</style>
