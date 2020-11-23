<template>
  <div v-if="lot.id && +lot.id === +$route.params.id">
    <Header :page="{ title: 'Лот', color: 'white', dark: false, update: false }" />
    <v-carousel
      v-if="lot.images.length"
      cycle
      height="250"
      hide-delimiter-background
      :show-arrows="false"
      :show-arrows-on-hover="false"
      hide-delimiters
    >
      <v-carousel-item
        v-for="(image, i) in lot.images"
        :key="i"
      >
        <v-img
          height="250"
          :src="image.url"
        />
      </v-carousel-item>
    </v-carousel>
    <v-card-title>
      <v-row class="pl-4 grey--text">
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
      <v-card
        class="mx-auto my-2 pb-2"
        max-width="400"
        rounded="xl"
        color="deep-purple lighten-1"
      >
        <v-card-title class="white--text text-lighten-1">
          Победител{{ lot.wins.length === 1 ? 'ь' : 'и' }}
          <v-spacer />
          <v-btn icon dark large>
            <v-icon>
              mdi-comment-question
            </v-icon>
          </v-btn>
        </v-card-title>

        <v-card-text>
          <v-row>
            <v-col
              v-for="winner in lot.wins"
              :key="`winner_${winner.id}`"
              cols="2"
              active-class="deep-purple white--text"
            >
              <v-btn
                icon
                x-large
                @click="$router.push({ name: 'profile', params: { user: winner.user }})"
              >
                <v-avatar
                  :rounded="$auth.loggedIn && winner.user.id === $auth.user.id"
                  :color="$auth.loggedIn && winner.user.id === $auth.user.id ? 'blue' : 'green'"
                  size="48"
                  class="white--text"
                >
                  #{{ winner.num }}
                </v-avatar>
              </v-btn>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
    </div>
    <v-spacer />
    <v-divider class="mx-4" />
    <v-btn
      v-if="$auth.loggedIn && lot.user.id !== $auth.user.id && !$auth.user.numbers[lot.id] && lot.active"
      dark
      color="blue lighten-1"
      style="position: absolute; bottom: 10px;"
      block
      @click="takeNumber"
    >
      Взять номер
    </v-btn>
    <v-row v-else>
      <v-col cols="5" class="blue--text text--lighten-1 ml-4">
        {{ $auth.loggedIn && $auth.user.numbers[lot.id] ? `Ваш номер #${$auth.user.numbers[lot.id]}` : '' }}
      </v-col>
      <v-spacer />
      <v-col :class="lot.active ? 'success--text' : 'error--text'">
        {{ lot.active ? `Свободно ${lot.free_numbers}` : 'Лот завершен' }}
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  async fetch () {
    await this.fetchLot(this.$route.params.id)
  },
  data: () => ({
    loading: false,
    colors: [
      /*
      'red darken-4',
      'red',
      'red lighten-3',
      'yellow lighten-2',
      'yellow',
      'yellow darken-2'
       */
      'light-blue lighten-3',
      'light-blue lighten-2',
      'light-blue lighten-1',
      'light-blue',
      'light-blue darken-1',
      'light-blue darken-2',
      'blue darken-2',
      'light-blue darken-3',
      'blue darken-3',
      'light-blue darken-4',
      'blue darken-4'
    ]
  }),
  computed: {
    ...mapState('lot', ['lot'])
  },
  methods: {
    ...mapActions('lot', ['reserve', 'fetchLot']),
    async takeNumber () {
      await this.reserve()
    }
  }
}
</script>

<style scoped>
</style>
