<template>
  <v-navigation-drawer
    v-model="drawer"
    right
    absolute
    temporary
    width="480"
  >
    <v-row>
      <v-col cols="12">
        <v-card>
          <v-toolbar :color="options[component].color" light extended>
            <v-btn icon @click="drawer = false">
              <v-icon large class="white--text">
                mdi-close
              </v-icon>
            </v-btn>
            <v-spacer />
            <v-toolbar-title class="white--text">
              {{ options[component].title }}
            </v-toolbar-title>
            <v-spacer />
            <v-btn icon>
              <v-icon>mdi-pen</v-icon>
            </v-btn>
            <v-btn icon>
              <v-icon>mdi-view-module</v-icon>
            </v-btn>
            <template v-slot:extension>
              <v-btn
                fab
                color="cyan accent-2"
                bottom
                left
                absolute
                @click="dialog = !dialog"
              >
                <v-icon>mdi-plus</v-icon>
              </v-btn>
            </template>
          </v-toolbar>
          <v-list two-line subheader>
            <v-subheader inset>
              Folders
            </v-subheader>

            <v-divider inset />

            <v-subheader inset>
              Files
            </v-subheader>
          </v-list>

          <v-dialog v-model="dialog" max-width="500px">
            <v-card>
              <v-card-text>
                <v-text-field label="File name" />

                <small class="grey--text">* This doesn't actually save.</small>
              </v-card-text>

              <v-card-actions>
                <component :is="component" />
                <v-spacer />

                <v-btn text color="primary" @click="dialog = false">
                  Submit
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-card>
      </v-col>
    </v-row>
  </v-navigation-drawer>
</template>

<script>
import Profile from '@/components/user/Profile'

export default {
  name: 'Drawer',
  components: { Profile },
  data () {
    return {
      component: 'Profile',
      drawer: false,
      dialog: false,
      options: {
        Profile: { title: 'Профиль', color: 'green' },
        Store: { title: 'Магазин', color: 'light-blue' }
      }
    }
  },
  created () {
    this.$nuxt.$on('drawer', (component) => {
      this.component = component
      this.drawer = true
    })
  }
}
</script>

<style scoped>

</style>
