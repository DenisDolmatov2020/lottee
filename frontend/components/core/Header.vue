<template>
  <v-card
    color="grey lighten-4"
    flat
    tile
  >
    <v-toolbar dense :color="page.color" :dark="page.dark">
      <v-btn icon @click="$router.push('/')">
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>
      <v-toolbar-title>{{ page.title }}</v-toolbar-title>
      <v-spacer />
      <Modal v-if="page.update" />
    </v-toolbar>
  </v-card>
</template>

<script>
export default {
  props: {
    page: {
      type: Object,
      default: () => ({})
    }
  }
}
</script>

<style scoped>

</style>
