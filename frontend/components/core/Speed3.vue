<template>
  <v-card id="create">
    <v-btn
      v-if="!$store.getters['user/isAuthenticated']"
      color="blue darken-2"
      fab
      dark
      class="btn-no-auth"
      @click="toLogin"
    >
      <v-icon>
        mdi-account
      </v-icon>
    </v-btn>
    <v-speed-dial
      v-else
      v-model="fab"
      top
      right
      direction="bottom"
      slide-x-reverse-transition
    >
      <template v-slot:activator>
        <v-badge
          color="indigo"
          :content="String(user.energy)"
          left
          overlap
        >
          <v-btn
            v-model="fab"
            color="blue darken-2"
            dark
            fab
          >
            <v-icon v-if="fab">
              mdi-close
            </v-icon>
            <v-icon v-else large>
              mdi-account-circle
            </v-icon>
          </v-btn>
        </v-badge>
      </template>
      <v-btn
        fab
        dark
        small
        color="green"
        @click="drawer('Profile')"
      >
        <v-icon>mdi-cog</v-icon>
      </v-btn>
      <v-btn
        fab
        dark
        small
        color="gray"
      >
        <v-icon>mdi-bell-outline</v-icon>
      </v-btn>
      <v-btn
        fab
        dark
        small
        color="indigo"
      >
        <v-icon>mdi-plus</v-icon>
      </v-btn>
      <v-btn
        fab
        dark
        small
        color="red"
        @click="toLogout"
      >
        <v-icon>mdi-door</v-icon>
      </v-btn>
    </v-speed-dial>
  </v-card>
</template>
<script>
export default {
  data: () => ({
    direction: 'top',
    fab: false
  }),

  computed: {
    user () {
      return this.$store.getters['user/user']
    }
  },
  methods: {
    toLogin () {
      this.$router.push('/login')
    },
    toLogout () {
      this.$store.dispatch('user/logout')
    },
    drawer (component) {
      console.log('DRAWER EMIT')
      this.$nuxt.$emit('drawer', component)
    }
  }
}
</script>
<style>
  /* This is for documentation purposes and will not be needed in your application */
  #create .v-speed-dial {
    position: absolute;
  }

  #create .v-btn--floating {
    position: relative;
  }
  .btn-no-auth {
    z-index: 1;
    position: absolute;
    top: 16px;
    right: 16px;
  }
</style>
