<template>
  <div>
    <Header :page="{ title: 'Энергия', color: 'indigo darken-3', dark: true, update: false }" />
    <v-alert
      class="ma-4 v-alert-i"
      color="indigo"
      dark
      prominent
      border="left"
    >
      <v-list-item>
        <div class="left-item">
          <v-icon
            large
            class="icon-item"
          >
            mdi-clock
          </v-icon>
          <v-list-item-action-text class="clock">
            {{ item.clock }}
            <v-icon x-small>
              mdi-flash
            </v-icon>
            {{ tracker.days_row > 7 ? 7 : tracker.days_row }}
          </v-list-item-action-text>
        </div>
        <v-list-item-content>
          <v-list-item-title class="headline mb-1">
            {{ item.title }}
          </v-list-item-title>
          <span class="text-style">
            {{ item.text }}
          </span>
        </v-list-item-content>
      </v-list-item>
    </v-alert>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  data () {
    return {
      item:
        {
          icon: 'mdi-clock',
          color: 'indigo',
          title: 'Ежедневный бонус',
          text: 'Заходи каждый день и получай бонусы',
          clock: ''
        }
    }
  },
  computed: {
    ...mapState('track', ['tracker'])
  },
  created () {
    setInterval(this.getNow, 1000)
  },
  methods: {
    addNull (timeItem) {
      return String(timeItem).length === 1 ? '0' + timeItem : timeItem
    },
    getNow () {
      const tomorrow = new Date() // Создаем объект даты с текущем временем
      tomorrow.setHours(0, 0, 0, 0) // Обнуляем компоненты часа, минуты, секунды и миллисекунды, чтобы была полночь
      tomorrow.setDate(tomorrow.getDate() + 1) // Делаем следующий день
      const now = tomorrow - new Date()
      const hours = now / (1000 * 60 * 60) % 24 | 0
      const minutes = now / 1000 / 60 % 60 | 0
      const seconds = now / 1000 % 60 | 0
      this.item.clock = this.addNull(hours) + ':' + this.addNull(minutes) + ':' + this.addNull(seconds)
    }
  }
}
</script>

<style lang="scss" scoped>
.left-item {
  margin-left: -15px;
  margin-right: 15px;
}
.icon-item {
  width: 48px;
  height: 48px;
  background-color: rgba(255, 255, 255, 0.1);
  align-items: center;
  border-radius: 50%;
  display: flex;
  justify-content: center;
}
.text-style {
  color: rgba(255, 255, 255, 0.7);
}
</style>
