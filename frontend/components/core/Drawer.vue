<template>
  <v-navigation-drawer
    :value="drawer"
    right
    fixed
    temporary
    width="480"
    floating
    permanent
  >
    <nuxt />
  </v-navigation-drawer>
</template>

<script>

export default {
  name: 'Drawer',
  data () {
    return {
      pages: {
        new: { title: 'Подарки', color: 'pink', dark: true }
      }
    }
  },
  computed: {
    drawer () {
      return this.$route.name !== 'index'
    }
  }
}
</script>

<style scoped>

</style>
