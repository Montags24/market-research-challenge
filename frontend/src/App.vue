<script setup>
import { RouterView } from 'vue-router'
import { reactive } from 'vue';

import User from './js/User';

const user = reactive(new User())
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
      <RouterView :user="user" />
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
