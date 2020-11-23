<template>
  <v-navigation-drawer
    :value="drawer"
    right
    fixed
    temporary
    width="480"
    floating
    permanent
  >
    <nuxt />
    <template v-if="$route.name === 'id'" v-slot:append>
      <v-card-actions class="mx-2">
        <v-btn
          dark
          color="blue lighten-1"
          block
          @click="takeNumber"
        >
          Взять номер
        </v-btn>
        <v-row v-else>
          <v-col cols="5" class="blue--text text--lighten-1">
            {{ $auth.loggedIn && $auth.user.numbers[lot.id] ? `Ваш номер #${$auth.user.numbers[lot.id]}` : '' }}
          </v-col>
          <v-spacer />
          <v-col :class="lot.active ? 'success--text' : 'error--text'">
            {{ lot.active ? `Свободно ${lot.free_numbers}` : 'Лот завершен' }}
          </v-col>
        </v-row>
      </v-card-actions>
    </template>
  </v-navigation-drawer>
</template>

<script>

import { mapActions, mapState } from 'vuex'

export default {
  name: 'Drawer',
  data () {
    return {
      pages: {
        new: { title: 'Подарки', color: 'pink', dark: true }
      }
    }
  },
  computed: {
    ...mapState('lot', ['lot']),
    drawer () {
      return this.$route.name !== 'index'
    }
  },
  methods: {
    ...mapActions('lot', ['reserve']),
    async takeNumber () {
      await this.reserve()
    }
  }
}
</script>

<style scoped>

</style>
