<template>
  <div id="create">
    <v-tooltip v-if="!$auth.loggedIn" left fixed>
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="blue darken-2"
          fab
          dark
          class="btn-no-auth"
          v-bind="attrs"
          v-on="on"
          @click="drawer('/auth')"
        >
          <v-icon>
            mdi-account
          </v-icon>
        </v-btn>
      </template>
      <span>Вход</span>
    </v-tooltip>
    <v-speed-dial
      v-else
      v-model="fab"
      fixed
      top
      right
      direction="bottom"
      slide-x-reverse-transition
    >
      <template v-slot:activator>
        <v-tooltip left>
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              v-model="fab"
              color="blue darken-2"
              dark
              fab
              v-bind="attrs"
              v-on="on"
            >
              <v-icon v-if="fab">
                mdi-close
              </v-icon>
              <v-avatar v-else-if="$auth.user.image">
                <v-img :src="$auth.user.image" />
              </v-avatar>
              <v-icon v-else large>
                mdi-account-circle
              </v-icon>
            </v-btn>
          </template>
          <span>Профиль</span>
        </v-tooltip>
      </template>
      <v-tooltip left>
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            fab
            dark
            small
            color="green"
            v-bind="attrs"
            v-on="on"
            @click="drawer('/profile')"
          >
            <v-icon>mdi-cog</v-icon>
          </v-btn>
        </template>
        <span>Настройки</span>
      </v-tooltip>

      <v-badge
        v-if="$auth.user.prize_count"
        color="pink lighten-1"
        :content="String($auth.user.prize_count)"
        bordered
        inline
        left
        tile
        overlap
      >
        <v-tooltip left>
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              fab
              dark
              small
              color="pink"
              v-bind="attrs"
              v-on="on"
              @click="drawer('/prize')"
            >
              <v-icon>mdi-gift</v-icon>
            </v-btn>
          </template>
          <span>Выигранные призы</span>
        </v-tooltip>
      </v-badge>

      <v-badge
        inline
        tile
        :content="String($auth.user.energy)"
        color="indigo"
      >
        <v-btn
          fab
          dark
          small
          color="indigo"
          @click="drawer('/energy')"
        >
          <v-icon>mdi-flash</v-icon>
        </v-btn>
      </v-badge>

      <v-tooltip left>
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            fab
            dark
            small
            color="red"
            v-bind="attrs"
            v-on="on"
            @click="logout"
          >
            <v-icon>mdi-door</v-icon>
          </v-btn>
        </template>
        <span>Выйти</span>
      </v-tooltip>
    </v-speed-dial>
  </div>
</template>
<script>
import { mapActions } from 'vuex'

export default {
  data: () => ({
    direction: 'top',
    fab: false
  }),
  methods: {
    drawer (url) {
      this.$router.push(url)
    },
    ...mapActions('user', ['logout'])
  }
}
</script>
<style scoped>
  /* This is for documentation purposes and will not be needed in your application */
  .btn-no-auth {
    position: absolute;
    z-index: 1;
    top: 16px;
    right: 16px;
  }
</style>
