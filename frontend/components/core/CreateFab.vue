<template>
  <v-tooltip right>
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        fixed
        color="blue darken-2"
        fab
        dark
        bottom
        left
        v-bind="attrs"
        v-on="on"
        @click="$router.push('/new')"
      >
        <v-icon>
          mdi-plus
        </v-icon>
      </v-btn>
    </template>
    <span>Создать лот</span>
  </v-tooltip>
</template>

<script>
export default {
  name: 'CreateFab'
}
</script>

<style scoped>

</style>
