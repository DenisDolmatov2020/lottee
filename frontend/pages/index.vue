<template>
  <v-row>
    <v-col
      v-for="(lot, i) in lots"
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
import { mapState, mapActions } from 'vuex'
import Card from '@/components/lot/list/Card'

export default {
  name: 'Lot',
  components: { Card },
  async fetch () {
    await this.fetchLots()
  },
  data: () => ({
    visible: false,
    lot: {},
    lot_paid: false,
    hover: null,
    my_number: null
  }),
  computed: {
    ...mapState('lot', [
      'lots'
    ])
  },
  methods: {
    ...mapActions('lot', [
      'fetchLots'
    ])
  }
}
</script>

<style lang="scss" scoped>

</style>
