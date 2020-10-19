<template>
  <v-app id="main" :style="{background: $vuetify.theme.themes[theme].background}">
    <Logo />
    <Speed />
    <v-main>
      <v-container>
        <nuxt />
      </v-container>
    </v-main>
    <Drawer />
    <Snackbar />
  </v-app>
</template>

<script>
/* eslint-disable no-console */
export default {
  computed: {
    theme () {
      return (this.$vuetify.theme.dark) ? 'dark' : 'light'
    }
  },
  mounted () {
    const prizeSocket = new WebSocket('ws://127.0.0.1:8000/ws/prize/')
    console.log(prizeSocket)
    prizeSocket.onopen = () => {
      prizeSocket.onmessage = ({ data }) => {
        const lot = JSON.parse(data)
        console.log('Data LOTS WINNERS DATA: ' + data)
        setTimeout(function () {
          this.$nuxt.$emit('snackbar', { text: `Лот ${lot.title} завершен` })
        }, 5000)
        let winners = 'Номера '
        let you = false
        for (let i = 0; i < lot.winners.length; i++) {
          console.log(lot.winners[i])
          winners += `#${lot.winners[i].num} `
          if (+lot.winners[i].user === +this.$auth.user.id) {
            you = true
          }
        }
        setTimeout(function () {
          this.$nuxt.$emit('snackbar',
            {
              icon: you ? 'mdi-gift' : 'mdi-counter',
              color: you ? 'pink' : 'primary',
              text: you ? `Вы выйграли ${lot.title}` : winners,
              lot_id: lot.id
            }
          )
        }, 10000)
      }
    }
  }
  /*
  beforeDestroy () {
    this.prizeSocket.onclose = (e) => {
      console.log('Socket is closed. Reconnect will be attempted in 1 second.')
    }
    this.prizeSocket.onclose = true
  },
  methods: {
    new_message () {
      console.log('NEW MESSI')
      this.prizeSocket.send(JSON.stringify({
        text: 'INOUT MESSI', user: 3
      }))
    }
  }
  */
}
</script>
