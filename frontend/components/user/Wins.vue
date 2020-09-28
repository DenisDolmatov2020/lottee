<template>
  <div>
    <v-card>
      <v-card-title>
        <v-btn x-large dark icon @click="$nuxt.$emit('drawer-close')">
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
        <v-spacer />
        Уведомления
        <v-spacer />
        <v-btn dark icon class="mr-4">
          <v-icon>mdi-pencil</v-icon>
        </v-btn>

        <v-btn dark icon>
          <v-icon>mdi-dots-vertical</v-icon>
        </v-btn>
      </v-card-title>
      <v-alert
        class="ma-4"
        color="error"
        dark
        icon="mdi-vuetify"
        prominent
        border="left"
        close-text="Close Alert"
        dismissible
      >
        Praesent congue erat at massa. Nullam vel sem.
      </v-alert>
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'Wins',
  data () {
    return {
      alert: true
    }
  }
}
</script>

<style scoped>

</style>
