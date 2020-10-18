<template>
  <v-row>
    <v-col
      v-for="(lot, i) in l"
      :key="i"
      lg="4"
      md="6"
      cols="12"
      offset-md="1"
    >
      <Card :lot="lot" />
    </v-col>
  </v-row>
</template>

<script>
/* eslint-disable no-console */
// import { mapGetters } from 'vuex'
import Card from '@/components/lot/list/Card'

export default {
  name: 'Lot',
  components: { Card },
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
      } else if (this.$store.getters['lot/filter'] === 'my') {
        lots = lots.filter(lot => lot.user.id === this.$auth.user.id)
      }
      return lots
    }
  },
  methods: {
    lotDetail (lot) {
      this.$store.dispatch('lot/lotDetail', lot)
    }
    /*
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
            // await this.$store.commit('user/SET_ENERGY', response.data.user_energy)
            await this.$store.dispatch(
              'notification/set_notification',
              { title: `Ваш номер ${response.data.number.num}`, class: 'success' }
            )
            setInterval(this.my_number = null, 3000)
          }
        } catch (error) {
          await this.errorNotifications()
        }
      }
    }
    */
  }
}
</script>

<style lang="scss" scoped>

</style>
