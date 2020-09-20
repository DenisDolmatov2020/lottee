<template>
  <v-navigation-drawer
    v-model="drawer"
    right
    absolute
    temporary
    width="480"
  >
    <div>X</div>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: 'Drawer',
  data () {
    return {
      drawer: false
    }
  }
}
</script>

<style scoped>

</style>
