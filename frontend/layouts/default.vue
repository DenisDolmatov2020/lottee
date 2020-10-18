<template>
  <v-app id="main" :style="{background: $vuetify.theme.themes[theme].background}">
    <Menu />
    <Speed3 />
    <v-main>
      <v-container>
        1111111 {{ messages }}
        <v-btn @click="new_message">
          SEND MESSI
        </v-btn>
        <nuxt />
      </v-container>
    </v-main>
    <Drawer />
    <CreateFab />
    <Snackbar />
  </v-app>
</template>

<script>
/* eslint-disable no-console */
export default {
  data: () => ({
    message: [],
    prizeSocket: {}
  }),
  sockets: {
    connect () {
      console.log('socket connected SOCKET')
    },
    disconnect () {
      console.log('socket disconnected... SOCKETS')
    },
    customEmit (val) {
      console.log('this method was fired by the socket server. eg: io.emit(customEmit, data)')
    }
  },
  computed: {
    theme () {
      return (this.$vuetify.theme.dark) ? 'dark' : 'light'
    }
  },
  mounted () {
    this.prizeSocket = new WebSocket('ws://127.0.0.1:8000/ws/prize/')
    console.log(this.prizeSocket)
    this.prizeSocket.onopen = () => {
      this.prizeSocket.onmessage = ({ data }) => {
        this.messages.push(JSON.parse(data))
        console.log('Data LOTS WINNERS DATA: ' + data)
        console.log('Data LOTS WINNERS TYPE: ' + typeof data)
      }
    }
  },
  methods: {
    new_message () {
      console.log('NEW MESSI')
      this.prizeSocket.send(JSON.stringify({
        text: 'INOUT MESSI', user: 3
      }))
    }
  }
}
</script>
