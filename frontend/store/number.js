/* eslint-disable */


export const state = () => ({
  url: '/api/lot/',
  lot: {},
  lots: [],
  api_url: process.env.API_URL,
  filter: null
})

export const mutations = {
  SET_FILTER (state, filter) {
    state.filter = filter
  },
  SET_LOT (state, lot) {
    state.lot = lot
  },
  SET_LOTS (state, lots) {
    state.lots = lots
  }
}

export const actions = {
  async reserve({ rootState, commit }) {
    try {
      const response = await this.$axios({
        url: '/api/number/',
        method: 'PATCH',
        data: { lot_id: rootState['lot'].lot.id }
      })
      if (response.status === 200) {
        $nuxt.$emit('snackbar', { color: 'primary', text: `Ваш номер ${response.data.num}` })
      } else {
        $nuxt.$emit('snackbar', { color: 'error', text: 'Вам не удалось взять номер' })
      }
      await this.$auth.fetchUser()
    } catch (error) {
      $nuxt.$emit('snackbar', { color: 'error', text: 'Ошибка' })
    }
  }
}

export const getters = {
  lot: s => s.lot,
  lots: s => s.lots,
  filter: s => s.filter
}
