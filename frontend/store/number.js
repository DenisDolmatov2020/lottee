/* eslint-disable */
import jwt_decode from 'jwt-decode'


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
      console.log(1)
      console.log(rootState['lot'].lot.id)
      const response = await this.$axios.$post(`/api/number/${rootState['lot'].lot.id}/`)
      console.log(3)
      console.log(JSON.stringify(response))
      if (response.status === 200) {
        $nuxt.$emit('snackbar', { color: 'primary', text: `Ваш номер ${response.data.num}` })
      } else {
        console.log(JSON.stringify(response))
        $nuxt.$emit('snackbar', { color: 'error', text: 'Вам не удалось взять номер' })
      }
      console.log(2)
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
