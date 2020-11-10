<template>
  <div>
    <Header :page="{ title: 'Подарки', color: 'purple', dark: true, update: false }" />
    <v-alert
      v-for="prize in prizes"
      :key="prize.id"
      class="ma-4"
      color="pink"
      dark
      icon="mdi-gift"
      prominent
      border="left"
    >
      <v-row align="center">
        <v-col class="grow">
          Вы выиграли {{ prize.lot.title }}, номер #{{ prize.num }}
        </v-col>
        <v-col class="shrink">
          <v-btn text @click="$router.push(`/lot/${prize.lot.id}`)">
            Перейти
          </v-btn>
        </v-col>
      </v-row>
    </v-alert>
  </div>
</template>

<script>
export default {
  middleware: ['auth'],
  async fetch () {
    this.prizes = await this.$axios.$get('/api/prize')
  },
  data () {
    return {
      alert: true,
      prizes: []
    }
  }
}
</script>
