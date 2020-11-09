<template>
  <div>
    <Header :page="page" />
    <v-img height="100%">
      <v-row
        align="end"
        class="fill-height"
      >
        <v-spacer />
        <v-col
          align-self="start"
          class=""
          :cols="5"
          :offset="1"
          :sm="11"
        >
          <v-avatar
            class="profile"
            color="grey"
            size="164"
          >
            <v-img v-if="profile.image" :src="profile.image" />
            <v-icon v-else x-large>
              mdi-camera
            </v-icon>
          </v-avatar>
        </v-col>
        <v-spacer />
        <v-col
          :cols="7"
          :sm="12"
        >
          <v-list-item>
            <v-list-item-icon>
              <v-icon color="indigo">
                mdi-account
              </v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ profile.name }}</v-list-item-title>
              <v-list-item-subtitle> Имя </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
          <v-divider inset />
          <v-list-item>
            <v-list-item-icon>
              <v-icon color="indigo">
                mdi-phone
              </v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ profile.email }}</v-list-item-title>
              <v-list-item-subtitle> Email </v-list-item-subtitle>
            </v-list-item-content>
            <v-list-item-icon>
              <v-icon large>
                mdi-comment-question
              </v-icon>
            </v-list-item-icon>
          </v-list-item>
          <v-divider inset />
          <v-list-item>
            <v-list-item-icon>
              <v-icon color="indigo">
                mdi-phone
              </v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ profile.phone }}</v-list-item-title>
              <v-list-item-subtitle>Номер телефона</v-list-item-subtitle>
            </v-list-item-content>
            <v-list-item-icon>
              <v-icon large>
                mdi-comment-question
              </v-icon>
            </v-list-item-icon>
          </v-list-item>
          <v-divider inset />

          <v-list-item>
            <v-list-item-icon>
              <v-icon color="indigo">
                mdi-map-marker
              </v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ profile.address }}</v-list-item-title>
              <v-list-item-subtitle>Адрес</v-list-item-subtitle>
            </v-list-item-content>
            <v-list-item-icon>
              <v-icon large>
                mdi-comment-question
              </v-icon>
            </v-list-item-icon>
          </v-list-item>
        </v-col>
      </v-row>
    </v-img>
  </div>
</template>

<script>
export default {
  props: {
    user: {
      type: Object,
      default: null
    }
  },
  computed: {
    profile () {
      return this.user || this.$auth.user
    },
    my_profile () {
      return this.profile.id === this.$auth.user.id
    },
    page () {
      const myPage = { title: 'Профиль', color: 'blue lighten-1', dark: true, update: true }
      const userPage = { title: `Пользователь ${this.profile.name}`, color: 'green', dark: true, update: false }
      return this.my_profile ? myPage : userPage
    }
  }
}
</script>
