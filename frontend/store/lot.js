/* eslint-disable */


export const state = () => ({
  url: '/api/lot/',
  lot: {},
  lots: []
})

export const mutations = {
  SET_LOT (state, lot) {
    state.lot = lot
  },
  SET_LOTS (state, lots) {
    state.lots = lots
  }
}

export const actions = {
  async reserve({ state, commit, dispatch }) {
    try {
      const response = await this.$axios({
        url: '/api/number/',
        method: 'PATCH',
        data: { lot_id: state.lot.id }
      })
      if (response.status === 200) {
        $nuxt.$emit('snackbar', { text: `Ваш номер #${response.data}` })
      } else {
        $nuxt.$emit('snackbar', { color: 'error', text: 'Вам не удалось взять номер' })
      }
      // dispatch('fetchLot', this.$route.params.id)
      this.$auth.fetchUser()
    } catch (error) {
      $nuxt.$emit('snackbar', { icon: 'mdi-flash', color: 'error', text: 'Недостаточно энергии' })
    }
  },
  async createLot ({ state, commit, dispatch }, payload) {
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
        await this.$router.push({ path: '/' })
        $nuxt.$emit('snackbar', { text: 'Лот создан' })
      } else {
        $nuxt.$emit('snackbar', { color: 'error', text: 'Лот не создан' })
      }
    } catch (error) {
      $nuxt.$emit('snackbar', { color: 'error', text: 'Ошибка при создании лота' })
    }
  },
  async fetchLot ({ state, commit }, lot_id) {
    try {
      const response = await this.$axios({
        url: `${state.url}/${lot_id}`,
        headers: { Authorization: '' },
        method: 'GET'
      })
      if (response.status === 200) {
        await commit('SET_LOT', response.data)
      }
    } catch (error) {
      $nuxt.$emit('snackbar', { color: 'error', text: 'Ошибка при загрузке лота' })
    }
  },
  async fetchLots ({ state, commit }) {
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
  lot: s => s.lot
}

