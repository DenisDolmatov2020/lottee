<template>
  <v-row
    align="center"
    justify="end"
    class="mr-4"
  >
    <v-icon class="mr-1" color="pink">
      mdi-gift-outline
    </v-icon>
    <span class="subheading mr-2 font-weight-bold pink--text">
      {{ lot.winners }}
    </span>
    <v-icon color="indigo">
      mdi-flash
    </v-icon>
    <span class="subheading mr-2 font-weight-bold indigo--text">
      {{ lot.energy }}
    </span>
    <v-icon class="mr-1" color="green">
      mdi-table-account
    </v-icon>
    <span class="subheading font-weight-bold green--text">
      <span v-if="lot.free_numbers">
        {{ lot.free_numbers }}/
      </span>
      {{ lot.players }}
    </span>
  </v-row>
</template>

<script>
export default {
  name: 'Icons',
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
