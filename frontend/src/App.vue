<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <header class="relative">
    <!-- Include NavBar component for navigation -->
    <div class="fixed top-0 left-0 right-0">
      <NavBar />
    </div>
  </header>

  <main class="pt-[48px]">
    <!-- RouterView for rendering routed components -->
    <RouterView />
    <!-- Main content goes here -->
  </main>

  <footer>
    <!-- Footer content goes here -->
  </footer>

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
