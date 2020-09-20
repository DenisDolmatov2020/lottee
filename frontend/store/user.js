/* eslint-disable */

export const state = () => ({
  token: '',
  user: {},
  numbers: {}
})

export const mutations = {
  SET_TOKEN (state, payload) {
    // state.userId = payload.userId
    state.token = payload.token
  },
  SET_USER_PROFILE (state, payload) {
    state.user = payload.user
    state.numbers = payload.numbers
  },
  SET_NUMBERS (state, numbers)   {
    state.numbers = numbers
  },
  SET_NUMBER (state, payload) {
    state.numbers[payload.lot] = payload.num
  },
  SET_ENERGY (state, energy) {
    state.user.energy = energy
  },
  ADD_ENERGY (state, energy) {
    state.user.energy += energy
  },
  LOGOUT (state) {
    state.token = ''
    state.user = {}
  }
}
import jwt_decode from 'jwt-decode'
export const actions = {
  async register ({ dispatch }, user) {
    try {
      const response = await this.$axios({
        url: '/api/my-user/create/',
        data: user,
        method: 'POST',
      })
      await console.log(response.status)
      if (response.status === 201) await dispatch('login', user)
      else await dispatch('notification/set_notification', { title: 'E-mail уже используется', class: '' }, { root: true })
    } catch (error) {
      await dispatch('notification/set_notification', { title: 'Ошибка при регистрации', class: 'error' }, { root: true })
    }
  },
  async login ({ commit, dispatch }, user) {
    try {
      const response = await this.$axios({
        url: '/api/my-user/token/',
        data: user,
        method: 'POST'
      })
      this.$axios.defaults.headers.common.Authorization = `JWT ${response.data.access}`
      localStorage.token = await response.data.refresh
      localStorage.acceess = await response.data.access
      console.log(response.data.access)
      const decoder = jwt_decode(response.data.access)
      console.log('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
      console.log(JSON.stringify(decoder))
      await commit('SET_TOKEN', { token: await response.data.refresh })
      await commit('SET_USER_PROFILE', { user: decoder.user_profile })
      // await dispatch('notification/set_notification', { title: 'Вы вошли в аккаунт', class: '' }, { root: true })
      await this.$router.push('/')
    } catch (error) {
      if (error.response.status === 401) {
        // await dispatch('notification/set_notification', { title: 'Неверная почта или пароль', class: 'error' }, { root: true })
      } else {
        // await dispatch('notification/set_notification', { title: 'Ошибка при входе', class: 'error' }, { root: true })
      }
    }
  },
  async update ({ state, commit, dispatch }, payload) {
    const formData = new FormData()
    if (payload.name) {
      await formData.append('name', payload.name)
    }
    if (payload.image) {
      await formData.append('image', payload.image)
    }
    try {
      const response = await this.$axios.patch(
        '/api/my-user/profile/', formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
      await console.log('Success: ' + JSON.stringify(response.data))
      if (response.status === 200) {
        await commit('SET_USER', response.data)
        let text = 'Изменения пользователя сохранены'
        // await dispatch('notification/set_notification', { title: text, class: '' }, { root: true })
        //  $nuxt.$emit('open-snack', { snackbar: true, background_color: 'success', text, timeout: 1500 })
      }
    } catch (error) {
      // eslint-disable-next-line no-console
      console.log('Error: ', error)
      // await dispatch('error/errorActions', { error: error }, { root: true } )
      let text = 'Ошибка при сохранении'
      console.log(text)
      // await dispatch('notification/set_notification', { title: text, class: '' }, { root: true })
      // $nuxt.$emit('open-snack', { snackbar: true, background_color: 'error', text, timeout: 1500 })
    }
  },
  async profile ({ commit }) {
    try {
      const response = await this.$axios({
        url: '/api/my-user/profile/',
        method: 'GET'
      })
      await console.log( `Response status : ${ JSON.stringify(response) }` )
      localStorage.user = await JSON.stringify(response.data)
      console.log('++++++++++++++++_++++++++++++++++++++____')
      console.log(JSON.stringify(response.data.user))
      await commit('SET_USER', response.data.user)
      await commit('SET_NUMBERS', response.data.numbers)
    } catch (error) {
      // eslint-disable-next-line no-console
      console.log('auth_error_login_action', error)
    }
  },
  async logout ({ commit, dispatch }) {
    localStorage.removeItem('user')
    localStorage.removeItem('token')
    await commit('LOGOUT')
    delete this.$axios.defaults.headers.common.Authorization
    await this.$router.push('/login')
    dispatch('notification/set_notification', { title: 'Вы вышли из аккаунта', class: '' }, { root: true })
  }
}

export const getters = {
  user: s => s.user,
  numbers: s => s.numbers,
  isAuthenticated: s => !!s.token
}
