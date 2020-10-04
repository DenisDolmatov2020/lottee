<template>
  <v-app id="main" :style="{background: $vuetify.theme.themes[theme].background}">
    <Menu />
    <Speed3 />
    <v-main>
      <v-container>
        <nuxt />
      </v-container>
    </v-main>
    <Drawer />
    <CreateFab />
    <Snackbar />
  </v-app>
</template>

<script>
export default {
  computed: {
    theme () {
      return (this.$vuetify.theme.dark) ? 'dark' : 'light'
    }
  }
}
</script>
