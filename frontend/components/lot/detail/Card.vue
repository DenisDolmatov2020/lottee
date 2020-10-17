<template>
  <div>
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
              <v-menu
                bottom
                min-width="200px"
                rounded
                offset-y
              >
                <template v-slot:activator="{ on }">
                  <v-btn
                    icon
                    x-large
                    v-on="on"
                  >
                    <v-avatar
                      rounded
                      :tile="winner.user.id !== $auth.user.id"
                      color="green"
                      size="48"
                    >
                      <img v-if="winner.user.image" :src="winner.user.image">
                      <v-icon v-else color="white">
                        mdi-account-outline
                      </v-icon>
                    </v-avatar>
                  </v-btn>
                </template>
                <v-card>
                  <v-list-item-content class="justify-center">
                    <div class="mx-auto text-center">
                      <v-row>
                        <v-col>
                          <v-avatar
                            rounded
                            :tile="winner.user.id !== $auth.user.id"
                            color="green"
                          >
                            <img v-if="winner.user.image" :src="winner.user.image">
                            <v-icon v-else color="white">
                              mdi-account-outline
                            </v-icon>
                          </v-avatar>
                        </v-col>
                        <v-col>
                          <h3>{{ winner.user.name }}</h3>
                          <p class="caption mt-1">
                            {{ winner.user.email }}
                          </p>
                        </v-col>
                      </v-row>
                      <div v-if="lot.user.id === $auth.user.id">
                        <v-divider class="my-3" />
                        <v-btn
                          depressed
                          rounded
                          text
                        >
                          {{ winner.user.phone }} {{ lot.user.id }} {{ $auth.user.id }}
                        </v-btn>
                        <v-divider class="my-3" />
                        <v-btn
                          depressed
                          rounded
                          text
                        >
                          {{ winner.user.address }}
                        </v-btn>
                      </div>
                    </div>
                  </v-list-item-content>
                </v-card>
              </v-menu>
            </v-col>
          </v-row>
        </div>
      </v-card-text>
    </div>

    <v-spacer />
    <v-divider class="mx-4" />
    <v-card-actions class="mx-2">
      <v-btn
        color="red"
        text
        @click="$nuxt.$emit('drawer-close')"
      >
        Закрыть
      </v-btn>
      <v-spacer  />
      <span v-if="$auth.loggedIn && $auth.user.numbers[lot.id]" class="blue--text text--lighten-1">
        Номер #{{ $auth.user.numbers[lot.id] }}
      </span>
      <v-spacer />
      <span v-if="lot.user.id === $auth.user.id" class="px-2 py-1 blue lighten-1 rounded-sm">
        Ваш лот
      </span>
      <span v-else-if="!lot.active" class="success--text">
        Лот завершен
      </span>
      <v-btn
        v-else-if="!$auth.user.numbers[lot.id]"
        color="primary"
        @click="reserve"
      >
        Резерв
      </v-btn>
      <span v-else />
    </v-card-actions>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Card',
  data: () => ({
    show: false,
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
    ...mapState('lot', {
      lot: state => state.lot
    })
  },
  methods: {
    ...mapActions('number', [
      'reserve'
    ])
  }
}
</script>

<style scoped>

</style>
