<template>
  <v-card
    :loading="loading"
    class="mx-auto"
  >
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
        >
          <v-card-title>
            <v-btn x-large dark icon @click="$nuxt.$emit('drawer-close')">
              <v-icon>mdi-chevron-left</v-icon>
            </v-btn>
            <v-spacer />
            <v-btn dark icon class="mr-4">
              <v-icon>mdi-pencil</v-icon>
            </v-btn>
            <v-btn dark icon>
              <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
          </v-card-title>
        </v-img>
      </v-carousel-item>
    </v-carousel>
    <v-card-title>
      <v-row class="pl-4">
        {{ lot.title }}
        <v-spacer />
        <icons :lot="lot" />
      </v-row>
    </v-card-title>

    <v-card-text v-if="lot.user">
      <v-row
        align="center"
        class="mx-0"
      >
        <v-rating
          :value="4.5"
          color="amber"
          dense
          half-increments
          readonly
          size="14"
        />

        <div class="grey--text ml-4">
          4.5 (413)
        </div>
      </v-row>

      <div class="my-4 subtitle-1">
        <v-list-item-avatar
          color="grey lighten-2"
          class="ml-2 mt-1"
        >
          <v-img
            v-if="lot.user.image"
            :src="lot.user.image"
          />
          <v-icon v-else>
            mdi-camera
          </v-icon>
        </v-list-item-avatar>
        {{ lot.user.name }}
      </div>
      <div>{{ lot.description }}</div>
    </v-card-text>

    <v-divider class="mx-4" />

    <v-card-title>
      {{ lot.active ? 'Условия участия' : 'Победители' }}
      <v-spacer />
      <v-icon large>
        mdi-comment-question
      </v-icon>
    </v-card-title>

    <v-card-text>
      <v-row
        v-for="condition in lot.conditions"
        :key="condition.id"
        active-class="deep-purple accent-4 white--text"
        column
      >
        <a :href="condition.link" target="_blank" style="text-decoration: none;">
          <v-icon :color="condition.color" x-large>
            mdi-facebook
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
    </v-card-text>

    <v-divider class="mx-4" />
    <v-card-actions class="mx-2">
      <v-btn
        color="red"
        text
        @click="$nuxt.$emit('drawer-close')"
      >
        Закрыть
      </v-btn>
      <v-spacer />
      <span v-if="$auth.user.numbers[lot.id]" class="red--text text--lighten-1">
        Номер #{{ $auth.user.numbers[lot.id] }}
      </span>
      <span v-else-if="lot.user.id === $auth.user.id" class="px-2 py-1 red lighten-1 rounded-sm">
        Ваш лот
      </span>
      <span v-else-if="lot.active" class="success--text ">
        Лот завершен
      </span>
      <v-btn
        v-else
        color="primary"
        @click="reserve"
      >
        Резерв
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Card',
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
