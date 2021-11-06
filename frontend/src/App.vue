<template>
  <v-app>
<!--    <router-view />-->
    <rec-input />
  </v-app>
</template>

<script>
import RecInput from '@/components/RecInput'

export default {
  components: {
    RecInput
    // Recommendations,
    // Markup, 
    // Documentation,
    // About
    },
  name: 'App',
  data: () => ({}),
}
</script>


<style>
#app {
  font-family: 'Red Hat mono', monospace, Roboto, sans-serif, 'Zen Antique', serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
