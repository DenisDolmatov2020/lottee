<template>
  <div v-if="lot.id && +lot.id === +$route.params.id">
    <Header :page="{ title: 'Лот', color: 'white', dark: false, update: false }" />
    <v-carousel
      cycle
      height="250"
      hide-delimiter-background
      show-arrows-on-hover
    >
      <v-carousel-item
        v-for="(slide, i) in slides"
        :key="i"
      >
        <v-img
          height="250"
          :src="slide"
        />
      </v-carousel-item>
    </v-carousel>
    <v-card-title>
      <v-row class="pl-4">
        {{ lot.title }}
        <v-spacer />
        <icons :lot="lot" />
      </v-row>
    </v-card-title>

    <v-card-text>
      {{ lot.description }}
    </v-card-text>
    <Company v-if="lot.user" :company="lot.user" />

    <v-divider class="mx-4" />

    <v-card v-if="lot.active && lot.condition">
      <v-card-title>
        Условия участия
        <v-spacer />
        <v-menu transition="slide-x-reverse-transition">
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="secondary"
              text
              dark
              v-bind="attrs"
              v-on="on"
            >
              <v-icon large color="gray">
                mdi-comment-question
              </v-icon>
            </v-btn>
          </template>
          <v-sheet color="warning" class="white-text">
            Выполнив условия, можно принять участие в <br>
            розыгрыше если условия будут выполнены после участия, <br>
            в случае победы результат аннулируется.
          </v-sheet>
        </v-menu>
      </v-card-title>

      <v-card-text>
        <div>
          <v-row
            v-for="condition in lot.conditions"
            :key="condition.id"
            active-class="deep-purple accent-4 white--text"
            column
          >
            <a :href="condition.link" target="_blank" style="text-decoration: none;">
              <v-icon :color="condition.color" x-large>
                mdi-{{ condition.icon }}
              </v-icon>
              <v-chip v-if="condition.subscribe" :color="condition.color" class="ma-2">
                Подписка
              </v-chip>
              <v-chip v-if="condition.like" :color="condition.color" class="ma-2">
                Лайк
              </v-chip>
              <v-chip v-if="condition.comment" :color="condition.color" class="ma-2">
                Коммент
              </v-chip>
              <v-chip v-if="condition.repost" :color="condition.color" class="ma-2">
                Репост
              </v-chip>
            </a>
          </v-row>
        </div>
      </v-card-text>
    </v-card>
    <div v-else-if="!lot.active && lot.wins">
      <v-card-title class="red--text text-lighten-1">
        Победители
        <v-spacer />
      </v-card-title>

      <v-card-text>
        <div>
          <v-row>
            <v-col
              v-for="winner in lot.wins"
              :key="`winner_${winner.id}`"
              cols="2"
              active-class="deep-purple accent-4 white--text"
            >
              <v-btn
                icon
                x-large
                @click="$router.push({ name: 'profile', params: { user: winner.user }})"
              >
                <v-avatar
                  rounded
                  :tile="$auth.loggedIn && winner.user.id === $auth.user.id"
                  :color="$auth.loggedIn && winner.user.id === $auth.user.id ? 'blue' : 'green'"
                  size="48"
                >
                  <img v-if="winner.user.image" :src="winner.user.image">
                  <v-icon v-else color="white">
                    mdi-account-outline
                  </v-icon>
                </v-avatar>
              </v-btn>
            </v-col>
          </v-row>
        </div>
      </v-card-text>
    </div>

    <v-spacer />
    <v-divider class="mx-4" />
    <v-card-actions class="mx-2">
      <v-btn
        v-if="$auth.loggedIn && lot.user.id !== $auth.user.id && !$auth.user.numbers[lot.id] && lot.active"
        dark
        color="blue lighten-1"
        block
        @click="reserve"
      >
        Резерв {{ lot.free_numbers }}
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
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  async fetch () {
    await this.fetchLot(this.$route.params.id)
    // await this.$nuxt.$emit('drawer-open')
  },
  data: () => ({
    loading: false,
    colors: [
      'indigo',
      'warning',
      'pink darken-2',
      'red lighten-1',
      'deep-purple accent-4'
    ],
    slides: [
      'https://cdn.vuetifyjs.com/images/cards/cooking.png',
      'https://cdn.vuetifyjs.com/images/cards/cooking.png',
      'https://cdn.vuetifyjs.com/images/cards/cooking.png',
      'https://cdn.vuetifyjs.com/images/cards/cooking.png',
      'https://cdn.vuetifyjs.com/images/cards/cooking.png'
    ]
  }),
  computed: {
    ...mapState('lot', [
      'lot'
    ])
  },
  methods: {
    ...mapActions('lot', [
      'reserve',
      'fetchLot'
    ])
  }
}
</script>

<style scoped>

</style>
