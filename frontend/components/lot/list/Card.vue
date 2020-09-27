<template>
  <div class="d-flex flex-no-wrap justify-space-between">
    <div class="title font-weight-light mb-2">
      <v-card-title
        class="headline"
        v-text="lot.title"
      />

      <v-card-subtitle
        class="subheading font-weight-light grey--text"
        v-text="lot.description"
      />
    </div>

    <v-avatar
      class="ma-3"
      size="80"
      tile
      color="grey lighten-1"
    >
      <v-img v-if="lot.image" :src="lot.image" />
      <v-icon v-else>
        mdi-camera
      </v-icon>
    </v-avatar>
  </div>
</template>

<script>
export default {
  name: 'Card',
  props: {
    lot: {
      type: Object,
      default: () => ({})
    }
  }
}
</script>

<style scoped>

</style>
