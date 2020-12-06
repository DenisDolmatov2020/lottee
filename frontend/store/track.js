/* eslint-disable */
export const state = () => ({
  tracker: {}
})

export const mutations = {
  SET_TRACKER (state, tracker) {
    state.tracker = tracker
  }
}

export const actions = {
  trackerTimer ({ dispatch }) {
    setInterval(() => { dispatch('tracker') }, 60 * 60 * 1000) // каждую минуту
  },
  async tracker ({ commit }) {
    if (this.$auth.loggedIn) {
      const response = await this.$axios.get('/api/tracker')
      commit('SET_TRACKER', response.data)
      if (response.status === 201) {
        $nuxt.$emit('snackbar', {
          color: 'indigo',
          icon: 'mdi-flash',
          title: `+${response.data.days_row < 8 ? response.data.days_row : 7} к энергии`,
          timeout: 7000,
          text: `Получен ежедневный бонус за
                  ${response.data.days_row}
                  ${response.data.days_row === 1 ? 'день' : response.data.days_row < 5 ? 'дня' : 'дней'}
                  посещения подряд`
        })
        this.$auth.fetchUser()
      }
    }
  }
}
