<template>
  <v-app id="main" :style="{background: $vuetify.theme.themes[theme].background}">
    <Logo />
    <Speed />
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
    <Drawer v-if="drawer" />
    <Snackbar />
  </v-app>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
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
    ...mapState('lot', ['lots']),
    drawer () {
      return this.$route.path !== '/'
    },
    theme () {
      return (this.$vuetify.theme.dark) ? 'dark' : 'light'
    }
  },
  mounted () {
    if (this.$auth.loggedIn) {
      this.trackerTimer()
      const prizeSocket = new WebSocket('ws://127.0.0.1:8000/ws/prize/')
      prizeSocket.onopen = () => {
        prizeSocket.onmessage = ({ data }) => {
          const lot = JSON.parse(data)

          setTimeout(function () {
            this.$nuxt.$emit('snackbar', { text: `Лот ${lot.title} завершен` })
          }, 5000)
          let winners = 'Номера '
          let you = null
          for (let i = 0; i < lot.winners.length; i++) {
            winners += `#${lot.winners[i].num} `
            if (+lot.winners[i].user === +this.$auth.user.id) {
              you = lot.winners[i].num
            }
          }
          setTimeout(function () {
            this.$nuxt.$emit('snackbar',
              {
                icon: you ? 'mdi-gift' : 'mdi-counter',
                color: you ? 'deep-purple' : 'primary',
                text: you ? `Вы выйграли ${lot.title} с номером #${you}` : winners,
                lot_id: lot.id
              }
            )
          }, 10000)
        }
      }
    }
  },
  methods: {
    ...mapActions('lot', ['fetchLots']),
    ...mapActions('track', ['trackerTimer'])
  }
}
</script>
