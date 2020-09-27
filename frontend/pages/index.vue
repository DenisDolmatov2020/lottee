<template>
  <v-row>
    <v-col
      v-for="(lot, i) in l"
      :key="i"
      lg="4"
      md="6"
      cols="12"
    >
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
              <v-divider class="my-2" />
              <icons :lot="lot" />
            </v-card-text>
          </v-card>
        </template>
      </v-hover>
    </v-col>
  </v-row>
</template>

<script>
// import { mapGetters } from 'vuex'

export default {
  name: 'Lot',
  async fetch ({ store }) {
    await store.dispatch('lot/fetchLots')
  },
  data: () => ({
    visible: false,
    lot: {},
    lot_paid: false,
    lots: [],
    hover: null,
    my_number: null
  }),
  computed: {
    l () {
      // NEED switch
      let lots = this.$store.getters['lot/lots']
      if (this.$store.getters['lot/filter'] === 'active') {
        lots = lots.filter(lot => lot.active === true)
      } else if (this.$store.getters['lot/filter'] === 'have') {
        lots = lots.filter(lot => this.numbers[lot.id])
      } else if (this.$store.getters['lot/filter'] === 'my') {
        lots = lots.filter(lot => lot.user.id === this.$store.getters['user/user'].id)
      }
      return lots
    }
  },
  methods: {
    async lotDetail (lot) {
      await this.$store.dispatch('lot/lotDetail', lot)
      this.$nuxt.$emit('drawer', 'Card')
      // await this.$store.commit('lot/SET_LOT', lot)
      // await this.$nuxt.$emit('drawer', 'Detail')
    },
    async takeNumber (lot) {
      if (this.user.energy >= lot.energy) {
        try {
          const response = await this.$axios({
            url: `/api/lots/number/${lot.id}/`,
            method: 'POST'
          })
          if (response.status === 200) {
            this.my_number = lot.id
            this.$store.commit('user/SET_NUMBER', response.data.number)
            await this.$store.commit('user/SET_ENERGY', response.data.user_energy)
            await this.$store.dispatch(
              'notification/set_notification',
              { title: `Ваш номер ${response.data.number.num}`, class: 'success' }
            )
            setInterval(this.my_number = null, 3000)
          } else {
            await this.errorNotifications()
          }
        } catch (error) {
          await this.errorNotifications()
        }
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.v-sheet--offset {
  top: -24px;
}
.v-card {
  cursor: pointer;
}
</style>
