<template>
  <v-app>
    <v-main>
      <Wordament/>
    </v-main>
  </v-app>
</template>

<script>
import Wordament from './components/WordamentComponent.vue'

export default {
  name: 'App',

  components: {
    Wordament,
  },

  data: () => ({
    //
  }),
}
</script>
