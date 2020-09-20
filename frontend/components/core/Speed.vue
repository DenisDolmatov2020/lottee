<template>
  <div>
    <div
      v-if="$store.getters['user/isAuthenticated']"
      :class="['button-icon-logout']"
      @click="$store.dispatch('user/logout')"
    >
      <img
        alt="logout"
        :src="require('~/assets/icons/door.svg')"
      >
      <span class="icon-text">
        Выйти
      </span>
    </div>
    <div
      v-if="$store.getters['user/isAuthenticated']"
      class="button-icon-bell"
      @click="$store.commit('notification/BELL')"
    >
      <img
        alt="logout"
        :src="require('~/assets/icons/bell.svg')"
      >
      <span class="icon-text">
        Уведомления
      </span>
    </div>
    <div
      v-if="$route.path !== '/login'"
      :class="['button-icon-user', $store.getters['user/isAuthenticated'] ? 'button-icon-user-auth':'button-icon-user-not-auth']"
      @click="openUser"
    >
      <img
        :src="$store.getters['user/isAuthenticated'] ? require('~/assets/icons/user_cog.svg') : require('~/assets/icons/user_round.svg')"
      >
      <span>
        {{ $store.getters['user/isAuthenticated'] ? 'Профиль' : 'Логин' }}
      </span>
    </div>
    <div
      v-if="$store.getters['user/isAuthenticated']"
      class="button-energy"
    >
      <span class="count">
        {{ user.energy }}
      </span>
      <img
        width="32px"
        height="32px"
        :src="require('~/assets/icons/flash.svg')"
      >
    </div>
    <div
      v-if="$store.getters['user/isAuthenticated']"
      class="button-karma"
      @click="drawer('Karma')"
    >
      <span class="count">
        {{ user.karma }}
      </span>
      <img
        width="32px"
        height="32px"
        :src="require('~/assets/icons/karma.svg')"
      >
    </div>
  </div>
</template>

<script>

export default {
  name: 'Speed',
  data () {
    return {
      open: false,
      profile: {
        energy: 10000
      }
    }
  },
  computed: {
    user () {
      return this.$store.getters['user/user']
    }
  },
  methods: {
    openUser () {
      if (this.$store.getters['user/isAuthenticated']) {
        // this.$router.push('/user/profile')
        this.drawer('Profile')
      } else {
        this.$router.push('/login')
      }
    },
    drawer (component) {
      this.$nuxt.$emit('drawer', component)
    }
  }
}
</script>

<style lang="scss" scoped>
  /* bell */
  .button-icon-user,
  .button-icon-logout,
  .button-icon-bell,
  .button-energy,
  .button-star,
  .button-karma {
    position: fixed;
    z-index: 9;
    border: solid #FFFFFF;
    border-radius: 60px;
    box-shadow: rgba(0, 0, 0, 0.2) 0 3px 5px -1px, rgba(0, 0, 0, 0.14) 0px 6px 10px 0px, rgba(0, 0, 0, 0.12) 0px 1px 18px 0px;
  }
  .main {
    position: absolute;
    top: 140px;
    right: 10%;
    min-width: 500px;
    min-height: 500px;
    padding: 5px;
  }
  .button-energy,
  .button-star,
  .button-karma {
    right: 29px;
    width: 38px;
    height: 38px;
    padding: 5px;
    text-align: center;
    background-color: #FFFFFF;
    .count {
      font-family: monospace;
      position: absolute;
      min-width: 10px;
      padding: 0 4px;
      border-radius: 50px;
      top: 35px;
      right: -12px;
      color: #FFFFFF;
    }
  }
  .button-energy {
    top: 95px;
    /*
    &:hover {
      border-color: rgb(13, 71, 161);
    }
    */
    .count {
      background-color: rgb(13, 71, 161);
    }
  }
  /*
  .button-star {
    top: 160px;
    &:hover {
      border-color: rgb(255, 193, 7);
      // background-color: rgb(255, 193, 7);
    }
    .count {
      background-color: rgb(255, 193, 7);
    }
  }
  */
  .button-karma {
    top: 160px;
    /*
    &:hover {
      border-color: #424242;
      // background-color: #424242
    }
    */
    .count {
      background-color: #424242;
    }
  }
  /* user */
  .button-icon-user-auth {
    background-color: #43A047;
  }
  .button-icon-user-not-auth {
    background-color: #0277BD
  }
  .button-icon-bell,
  .button-icon-logout {
    cursor: pointer;
    right: 160px;
    width:42px;
    height: 42px;
    background-color: #F44336;
    img {
      width: 28px;
      top: 8px;
      left: 8px;
    }
    .icon-text {
      top: 10px;
      right: 10px;
    }
  }
  .button-icon-bell {
    right: 100px;
    background-color: #424242;
    img {
      width: 22px;
      top: 6px;
      left: 10px;
    }
    .count {
      position: relative;
      top: -5px;
      left: 5px;
      background-color: #43A047;
      color: #FEFEFE;
      padding: 5px;
    }
  }
  .button-icon-user {
    cursor: pointer;
    right: 24px;
    width: 56px;
    height: 56px;
    img {
      width: 36px;
      top: 10px;
      left: 10px;
    }
    span {
      top: 15px;
      right: 15px;
    }
  }
  .button-icon-logout,
  .button-icon-bell {
    &:hover {
      width: 156px;
      span {
        opacity: 1;
        visibility: visible;
      }
    }
  }
  .button-icon-user {
    &:hover {
      border-color: #0277BD;
    }
  }
  .button-icon-logout,
  .button-icon-bell,
  .button-icon-user {
    top: 16px;
    transition: .5s ease-in-out;
    img {
      position: absolute;
    }
    span {
      position: absolute;
      color: white;
      opacity: 0;
      visibility: hidden;
      transition: .35s opacity, .35s visibility;
    }
  }
</style>
