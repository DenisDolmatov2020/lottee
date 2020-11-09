<template>
  <div>
    <Header :page="{ title: 'Подарки', color: 'purple', dark: true, update: false }" />
    <v-alert
      v-for="win in $auth.user.wins"
      :key="win.id"
      class="ma-4"
      color="pink"
      dark
      icon="mdi-gift"
      prominent
      border="left"
    >
      <v-row align="center">
        <v-col class="grow">
          Вы выиграли {{ win.lot.title }}, номер #{{ win.num }}
        </v-col>
        <v-col class="shrink">
          <v-btn text @click="$router.push(`/lot/${win.lot.id}`)">
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
  data () {
    return {
      alert: true
    }
  }
}
</script>
