<template>
  <v-row>
    <v-col cols="12">
      <v-card
        class="mx-auto"
      >
        <v-card-title>
          <v-btn x-large dark icon @click="$nuxt.$emit('drawer-close')">
            <v-icon>mdi-chevron-left</v-icon>
          </v-btn>
          <v-spacer />
          Профиль
          <v-spacer />

          <Modal />
        </v-card-title>
        <v-row justify="center">
          <v-avatar size="150">
            <v-img
              :src="$auth.user.image"
              dark
            />
          </v-avatar>
        </v-row>
        <v-list two-line>
          <v-list-item>
            <v-list-item-icon>
              <v-icon color="indigo">
                mdi-account
              </v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ $auth.user.name }}</v-list-item-title>
              <v-list-item-subtitle>Имя</v-list-item-subtitle>
            </v-list-item-content>

            <v-list-item-icon>
              <v-icon>mdi-message-text</v-icon>
            </v-list-item-icon>
          </v-list-item>

          <v-divider inset />

          <v-list-item>
            <v-list-item-icon>
              <v-icon color="indigo">
                mdi-email
              </v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ $auth.user.email }}</v-list-item-title>
              <v-list-item-subtitle>Email</v-list-item-subtitle>
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
        </v-list>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'Profile'
}
</script>

<style scoped></style>
