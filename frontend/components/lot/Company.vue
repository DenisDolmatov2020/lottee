<template>
  <v-card
    v-if="company"
    class="v-sheet--offset mx-auto"
    :color="$auth.loggedIn && company.id === $auth.user.id ? 'blue lighten-1' : 'green'"
    elevation="12"
    width="calc(100% - 32px)"
    height="80px"
  >
    <v-card-title
      v-if="company"
      three-line
      class="mb-2"
      :class="`mx-1 white--text`"
    >
      <v-list-item-avatar
        color="grey lighten-2"
        class="ml-1 mt-1"
      >
        <v-img
          v-if="company.image"
          :src="company.image"
        />
        <v-icon v-else>
          mdi-camera
        </v-icon>
      </v-list-item-avatar>
      <v-spacer />
      {{ $auth.loggedIn && $auth.user.id === company.id ? 'Ваш лот' : company.name }}
    </v-card-title>
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
.v-sheet--offset {
  top: -24px;
  margin-top: 24px;
}
</style>
