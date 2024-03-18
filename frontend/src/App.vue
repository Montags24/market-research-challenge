<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <header>
    <!-- Include NavBar component for navigation -->
    <NavBar />
  </header>

  <main>
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
