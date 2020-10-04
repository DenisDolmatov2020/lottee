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
      <v-toolbar dense :color="components[component].color" :dark="components[component].dark">
        <v-btn icon @click="drawer = false">
          <v-icon>mdi-arrow-left</v-icon>
        </v-btn>

        <v-toolbar-title>{{ components[component].title }}</v-toolbar-title>

        <v-spacer />
        <Modal v-if="component === 'Profile'" />
      </v-toolbar>
    </v-card>
    <component :is="component" />
  </v-navigation-drawer>
</template>

<script>
import Profile from '@/components/user/Profile'
import Wins from '@/components/user/Wins'
import Card from '@/components/lot/detail/Card'

export default {
  name: 'Drawer',
  components: { Profile, Wins, Card },
  data () {
    return {
      components: {
        Profile: { title: 'Профиль', color: 'blue', dark: true },
        Wins: { title: 'Подарки', color: 'pink', dark: true },
        Card: { title: 'Лот', color: 'white', dark: false }
      },
      component: 'Profile',
      drawer: false
    }
  },
  created () {
    this.$nuxt.$on('drawer', (component) => {
      this.component = component
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
