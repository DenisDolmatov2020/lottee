<template>
  <v-dialog
    v-if="$auth.loggedIn"
    v-model="dialog"
    max-width="600px"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        dark
        icon
        class="mr-4"
        v-bind="attrs"
        v-on="on"
      >
        <v-icon>mdi-pencil</v-icon>
      </v-btn>
    </template>
    <v-card>
      <v-card-text>
        <v-container>
          <v-row>
            <v-file-input
              v-model="user.image"
              label="Аватар"
              prepend-icon="mdi-camera"
            />
            <v-col
              cols="12"
              md="6"
            >
              <v-text-field
                v-model="user.name"
                label="Имя"
              />
            </v-col>
            <v-col
              cols="12"
              md="6"
            >
              <v-text-field
                v-model="user.email"
                label="Email"
                required
              />
            </v-col>
            <v-col
              cols="12"
              md="6"
            >
              <v-text-field
                v-model="user.phone"
                label="Номер телефона"
                required
              />
            </v-col>
            <v-col
              cols="12"
              md="6"
            >
              <v-text-field
                v-model="user.address"
                label="Адрес доставки"
                required
              />
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-btn
          color="error"
          text
          @click="dialog = false"
        >
          Отменить
        </v-btn>
        <v-spacer />
        <v-btn
          color="success"
          text
          @click="update(user); dialog = false"
        >
          Сохранить
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'Modal',
  data () {
    return {
      dialog: false,
      user: {}
    }
  },
  created () {
    this.user = {
      image: null,
      name: this.$auth.user.name,
      email: this.$auth.user.email,
      phone: this.$auth.user.phone,
      address: this.$auth.user.address
    }
  },
  methods: {
    ...mapActions('user', [
      'update'
    ])
  }
  /* computed: {
    user: {
      get () {
        return this.$store.state.a
      },
      set (value) {
        this.$store.commit('updateA', value)
      }
    }
  } */
}
</script>

<style scoped>

</style>
