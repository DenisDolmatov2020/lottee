<template>
  <v-card
    v-if="$auth.loggedIn"
    tile
  >
    <v-img height="100%">
      <v-row
        align="end"
        class="fill-height"
      >
        <v-col
          align-self="start"
          class=""
          :cols="5"
          :sm="12"
        >
          <v-avatar
            class="profile"
            color="grey"
            size="164"
          >
            <v-img :src="$auth.user.image ? $auth.user.image: ''" />
          </v-avatar>
        </v-col>
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
              <v-list-item-title>{{ $auth.user.name }}</v-list-item-title>
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
              <v-list-item-title>{{ $auth.user.email }}</v-list-item-title>
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
              <v-list-item-title>{{ $auth.user.phone }}</v-list-item-title>
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
              <v-list-item-title>{{ $auth.user.address }}</v-list-item-title>
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
  </v-card>
</template>

<script>
export default {
  name: 'Profile'
}
</script>
