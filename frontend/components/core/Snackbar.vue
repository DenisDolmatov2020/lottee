<template>
  <div>
    <v-snackbar
      v-model="snackbar"
      :color="color"
      :timeout="timeout"
      shaped
    >
      <v-icon large class="mr-2">
        {{ icon }}
      </v-icon>
      {{ text }}

      <template v-slot:action="{ attrs }">
        <v-btn
          v-if="lot_id"
          color="white"
          text
          v-bind="attrs"
          @click="$store.dispatch('lot/lotDetail', lot_id)"
        >
          Перейти
        </v-btn>
        <v-btn
          v-else
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
    icon: '',
    timeout: null,
    color: '',
    text: '',
    lot_id: null
  }),
  created () {
    this.$nuxt.$on('snackbar', (payload) => {
      this.icon = payload.icon || 'mdi-check-box-multiple-outline'
      this.timeout = payload.timeout || 3500
      this.color = payload.color || 'primary'
      this.text = payload.text || ''
      this.lot_id = payload.lot_id || null
      this.snackbar = true
    })
  }
}
</script>

<style scoped>

</style>
