<template>
  <v-hover>
    <template #default="{ hover }">
      <v-card
        class="my-12 mx-auto"
        width="400"
        :elevation="hover ? 24 : 3"
        @click="$router.push({ name: `id`, params: {id: lot.id}})"
      >
        <Company :company="lot.user" />
        <v-card-text class="pt-0">
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
              <v-img v-if="lot.images.length" :src="lot.images[0].url" />
              <v-icon v-else>
                mdi-camera
              </v-icon>
            </v-avatar>
          </div>
          <v-divider :class="['my-2', $auth.loggedIn && $auth.user.numbers[lot.id] ? 'blue' : '']" />
          <v-row>
            <span
              v-if="$auth.loggedIn && $auth.user.numbers[lot.id]"
              class="text-h6 ml-4 blue--text text--lighten-1"
            >
              {{ `#${$auth.user.numbers[lot.id]}` }}
            </span>
            <icons :lot="lot" />
          </v-row>
        </v-card-text>
      </v-card>
    </template>
  </v-hover>
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
