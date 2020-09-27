<template>
  <v-navigation-drawer
    v-model="drawer"
    right
    fixed
    temporary
    width="480"
    floating
  >
    <component :is="component" />
  </v-navigation-drawer>
</template>

<script>
import Profile from '@/components/user/Profile'
import Notifications from '@/components/user/Notifications'
import Card from '@/components/lot/detail/Card'

export default {
  name: 'Drawer',
  components: { Profile, Notifications, Card },
  data () {
    return {
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
