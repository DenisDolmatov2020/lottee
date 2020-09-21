<template>
  <span>
    <v-speed-dial
      v-model="fab"
      fixed
      top
      right
      direction="left"
      transition="slide-y-transition"
    >
      <template #activator>
        <v-btn
          v-model="fab"
          color="blue darken-2"
          dark
          fab
        >
          <v-icon v-if="fab">
            mdi-close
          </v-icon>
          <v-icon v-else>
            mdi-account-circle
          </v-icon>
        </v-btn>
      </template>

      <v-tooltip bottom>
        <template #activator="{ on }">
          <v-btn
            fab
            dark
            small
            color="green"
            v-on="on"
            @click="toUserModal('profile')"
          >
            <v-icon>
              mdi-account-cog-outline
            </v-icon>
          </v-btn>
        </template>
        <span>
          Профиль
        </span>
      </v-tooltip>
      <v-tooltip bottom>
        <template #activator="{ on }">
          <v-btn
            fab
            dark
            small
            color="cyan"
            v-on="on"
            @click="toUserModal('company')"
          >
            <v-icon>
              mdi-account-group-outline
            </v-icon>
          </v-btn>
        </template>
        <span>Компания</span>
      </v-tooltip>
      <v-tooltip bottom>
        <template #activator="{ on }">
          <v-btn
            fab
            dark
            small
            color="red"
            v-on="on"
          >
            <v-icon>mdi-logout</v-icon>
          </v-btn>
        </template>
        <span>Выйти</span>
      </v-tooltip>
    </v-speed-dial>
    <v-speed-dial
      v-model="fab"
      fixed
      top
      right
      direction="bottom"
      transition="slide-x-reverse-transition"
      class="bottom-speed"
    >
      <v-tooltip left>
        <template #activator="{ on }">
          <v-btn
            fab
            dark
            :small="profile.energy < 100"
            :large="profile.energy > 9999"
            color="energy"
            v-on="on"
            @click="toUserModal('energy')"
          >
            <v-icon>mdi-flash</v-icon>
            {{ profile.energy }}
          </v-btn>
        </template>
        <span> Добавить энергии </span>
      </v-tooltip>

      <v-tooltip left>
        <template #activator="{ on }">
          <v-btn
            fab
            dark
            :small="profile.energy < 100"
            :large="profile.energy > 9999"
            color="amber"
            v-on="on"
            @click="toUserModal('stars')"
          >
            <v-icon>
              mdi-trophy-award
            </v-icon>
            {{ profile.energy }}
          </v-btn>
        </template>
        <span>
          Звездочки
        </span>
      </v-tooltip>
      <v-tooltip left>
        <template #activator="{ on }">
          <v-btn
            fab
            dark
            :small="profile.karma < 100"
            :large="profile.karma > 9999"
            color="light-blue accent-1"
            v-on="on"
            @click="toUserModal('karma')"
          >
            <v-icon>
              mdi-diamond-stone
            </v-icon>
            {{ profile.karma }}
          </v-btn>
        </template>
        <span>
          Алмазы
        </span>
      </v-tooltip>
      <v-tooltip left>
        <template #activator="{ on }">
          <v-btn
            fab
            dark
            :small="profile.karma < 100"
            :large="profile.karma > 9999"
            color="black"
            v-on="on"
            @click="toUserModal('karma')"
          >
            <v-icon>mdi-yin-yang</v-icon>
            {{ profile.karma }}
          </v-btn>
        </template>
        <span> Карма </span>
      </v-tooltip>
    </v-speed-dial>
  </span>
</template>

<script>
export default {
  name: 'Speed',
  data: () => ({
    fab: false,
    show: false
  }),
  computed: {
    profile () {
      return this.$store.getters['user/user']
    }
  },
  created () {
    this.$nuxt.$on('drawer', () => {
      this.fab = true
    })
    this.$nuxt.$on('close-speed', () => {
      this.fab = false
    })
  },
  methods: {
    destroyProfile () {
      this.$store.commit('profile/destroyProfile')
    },
    toUserModal (page) {
      this.$nuxt.$emit('open-show', page)
      // this.openModal()
    },
    openModal () {
      this.show = true
    }
  }
}
</script>

<style lang="sass">

.bottom-speed
  right: 42px
  top: 70px

</style>
