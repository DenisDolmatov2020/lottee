<template>
  <v-hover>
    <template #default="{ hover }">
      <v-card
        class="my-12 mx-auto"
        width="400"
        :elevation="hover ? 24 : 3"
        @click="lotDetail(lot)"
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
              <v-img v-if="lot.image" :src="lot.image" />
              <v-icon v-else>
                mdi-camera
              </v-icon>
            </v-avatar>
          </div>
          <v-divider :class="['my-2', $auth.user.numbers[lot.id] ? 'red lighten-1' : '']" />
          <v-row>
            <span
              v-if="$auth.user.numbers[lot.id]"
              class="text-h6 ml-4 red--text text--lighten-1"
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
  },
  methods: {
    async lotDetail (lot) {
      await this.$store.dispatch('lot/lotDetail', lot)
      this.$nuxt.$emit('drawer', 'Card')
      // await this.$store.commit('lot/SET_LOT', lot)
      // await this.$nuxt.$emit('drawer', 'Detail')
    }
  }
}
</script>

<style scoped>

</style>
