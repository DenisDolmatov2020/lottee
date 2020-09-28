<template>
  <v-timeline :dense="mobile">
    <v-timeline-item
      v-for="lot in l"
      :key="lot.id"
      :color="lot.active ? 'green': 'red'"
      fill-dot
    >
      <template
        v-if="lot.user && lot.user.image"
        #icon
      >
        <span class="white--text">
          123
        </span>
      </template>
      <template
        v-if="!mobile"
        #opposite
      >
        <v-card
          :color="lot.active ? 'green darken-1' : 'red lighten-1'"
          class="px-4 white--text text-center"
        >
          {{ lot.active ? '1' : 'Завершен' }}
        </v-card>
      </template>
      <v-card :color="lot.active ? 'green darken-1' : 'red lighten-1'">
        <Card :lot="lot" />
      </v-card>
    </v-timeline-item>
  </v-timeline>
</template>
<script>
import Card from '@/components/lot/list/Card'

export default {
  components: { Card },
  async fetch ({ store }) {
    await store.dispatch('lot/fetchLots')
  },
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
    },
    mobile () {
      return this.$vuetify.breakpoint.smAndDown
    },
    date () {
      return new Date()
    }
  },
  methods: {
    trueDate (date) {
      return date > 9 ? date : `0${date}`
    },
    dateStart (dateS) {
      const date = new Date(dateS)
      return `${date.getUTCDate()}/${date.getUTCMonth()} ${this.trueDate(date.getUTCHours())} : ${this.trueDate(date.getUTCMonth())}`
    },
    lotStart (startDate) {
      return new Date(startDate)
    }
  }
}
</script>

<style scoped>
.v-sheet--offset {
  top: -24px;
  position: relative;
}
</style>
