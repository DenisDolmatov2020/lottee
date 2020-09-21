<template>
  <div>
    <v-snackbar
      v-model="snackbar"
      :color="color"
    >
      <v-icon large class="mr-2">
        {{ color === 'error' ? 'mdi-close-box-multiple-outline' : 'mdi-check-box-multiple-outline' }}
      </v-icon>
      {{ text }}

      <template v-slot:action="{ attrs }">
        <v-btn
          color="white"
          text
          v-bind="attrs"
          @click="snackbar = false"
        >
          <v-icon>
            mdi-close
          </v-icon>
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script>
export default {
  name: 'Snackbar',
  data: () => ({
    snackbar: false,
    color: '',
    text: 'www'
  }),
  created () {
    this.$nuxt.$on('snackbar', (payload) => {
      console.log(`COLOR TEXT ${payload.color} `)
      this.color = payload.color
      this.text = payload.text
      this.snackbar = true
    })
  }
}
</script>

<style scoped>

</style>
