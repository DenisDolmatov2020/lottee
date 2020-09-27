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
  async fetchLot ({ state, commit, dispatch }, payload) {
    payload.lot.conditions = JSON.stringify(payload.conditions)
    const formData = new FormData()
    const keys = Object.keys(payload.lot)
    if (payload.lot.image) { await formData.append('image', payload.lot.image) }
    for (const key of keys) {
      if (payload.lot[key]) {
        formData.append(key, payload.lot[key])
      }
    }
    try {
      const response = await this.$axios({
        url: state.url,
        method: 'POST',
        headers: {
          'Content-Type': 'multipart/form-data'
        },
        data: formData
      })
      if (response.status === 201) {
        // await commit('SET_FILTER', 'my')
        await this.$router.push({ path: '/' })
        $nuxt.$emit('snackbar', { color: 'primary', text: 'Лот создан' })
      } else {
        console.log(JSON.stringify(response))
        $nuxt.$emit('snackbar', { color: 'error', text: 'Лот не создан' })
      }
    } catch (error) {
      $nuxt.$emit('snackbar', { color: 'error', text: 'Ошибка при создании лота' })
    }
  },
  async lotDetail ({ state, commit }, lot) {
    try {
      const response = await this.$axios({
        url: `${state.url}/${lot.id}`,
        headers: { Authorization: '' },
        method: 'GET'
      })
      if (response.status === 200) {
        commit('SET_LOT', response.data)
      }
    } catch (error) {
      console.log(error)
      $nuxt.$emit('snackbar', { color: 'error', text: 'Ошибка при загрузке лота' })
    }
  },
  async fetchLots ({ state, commit, dispatch }) {
    try {
      const response = await this.$axios({
        url: state.url,
        headers: { Authorization: '' },
        method: 'GET'
      })
      if (response.status === 200) {
        commit('SET_LOTS', response.data)
      }
    } catch (error) {
      console.log(error)
      $nuxt.$emit('snackbar', { color: 'error', text: 'Ошибка при загрузке лотов' })
    }
  }
}

export const getters = {
  lot: s => s.lot,
  lots: s => s.lots,
  filter: s => s.filter
}

