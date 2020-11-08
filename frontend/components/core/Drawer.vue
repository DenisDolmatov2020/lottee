<template>
  <v-navigation-drawer
    v-model="drawer"
    right
    fixed
    temporary
    width="480"
    floating
  >
    <v-card
      color="grey lighten-4"
      flat
      tile
    >
      <v-toolbar dense :color="pages[$route.name].color" :dark="pages[$route.name].dark">
        <v-btn icon @click="drawer = false">
          <v-icon>mdi-arrow-left</v-icon>
        </v-btn>

        <v-toolbar-title>{{ pages[$route.name].title }}</v-toolbar-title>

        <v-spacer />
        <Modal v-if="$route.name === 'profile'" />
      </v-toolbar>
    </v-card>
    <nuxt />
  </v-navigation-drawer>
</template>

<script>

export default {
  name: 'Drawer',
  fetch () {
    this.drawer = true
  },
  data () {
    return {
      drawer: false,
      pages: {
        login: { title: 'Логин', color: 'blue', dark: true },
        profile: { title: 'Профиль', color: 'blue lighten-1', dark: true },
        victories: { title: 'Подарки', color: 'pink', dark: true },
        'lot-id': { title: 'Лот', color: 'white', dark: false }
      }
    }
  },
  watch: {
    drawer (value) {
      console.log('WATCH : ' + value)
      if (!value) { this.$router.push('/') }
    }
  },
  created () {
    this.$nuxt.$on('drawer-open', () => {
      this.drawer = true
    })
    this.$nuxt.$on('drawer-close', () => {
      this.drawer = false
    })
  }
}
</script>

<style scoped>

</style>
