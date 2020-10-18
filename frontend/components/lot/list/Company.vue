<template>
  <v-card
    v-if="company"
    class="v-sheet--offset mx-auto"
    :color="$auth.loggedIn && company.id === $auth.user.id ? 'blue darken-2' : 'green'"
    elevation="12"
    width="calc(100% - 32px)"
    height="80px"
  >
    <v-list-item-avatar
      color="grey lighten-2"
      class="ml-2 mt-1"
    >
      <v-img
        v-if="company.image"
        :src="company.image"
      />
      <v-icon v-else>
        mdi-camera
      </v-icon>
    </v-list-item-avatar>
    <v-rating
      :value="3"
      color="amber"
      :background-color="'white'"
      dense
      half-increments
      readonly
      size="14"
      class="float-right"
      small
    />
    <v-row>
      <span :class="`ml-4 white--text`">
        {{ $auth.loggedIn && $auth.user.id === company.id ? 'Ваш лот' : company.name }}
      </span>
    </v-row>
    <v-list-item
      v-if="company"
      three-line
      class="mb-2"
    />
  </v-card>
</template>

<script>
export default {
  name: 'Company',
  props: {
    company: {
      type: Object,
      default: () => ({})
    }
  }
}
</script>

<style scoped>

</style>
