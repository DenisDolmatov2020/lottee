<template>
  <div>
    <v-card>
      <v-card-title>
        <v-btn x-large dark icon @click="$nuxt.$emit('drawer-close')">
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
        <v-spacer />
        Мои подарки
        <v-spacer />
        <v-btn dark icon class="mr-4">
          <v-icon>mdi-pencil</v-icon>
        </v-btn>

        <v-btn dark icon>
          <v-icon>mdi-dots-vertical</v-icon>
        </v-btn>
      </v-card-title>

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
            Выигрышный номер #{{ win.num }}
          </v-col>
          <v-col class="shrink">
            <v-btn text @click="$router.push(`/lot/${win.lot}`)">
              Перейти {{ win }}
            </v-btn>
          </v-col>
        </v-row>
      </v-alert>
    </v-card>
  </div>
</template>

<script>
export default {
  data () {
    return {
      alert: true
    }
  }
}
</script>
