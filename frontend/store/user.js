/* eslint-disable */

export const actions = {
  async register ({ dispatch }, user) {
    try {
      const response = await this.$axios({
        url: '/api/my-user/create/',
        data: user,
        method: 'POST'
      })
      if (response.status === 201) await dispatch('login', user)
      else $nuxt.$emit('snackbar', { color: 'error', text: 'Такой пользователь уже существует' })
    } catch (error) {
      $nuxt.$emit('snackbar', { color: 'error', text: 'Ошибка при регистрации' })
    }
  },
  async login ({ commit, dispatch }, user) {
    try {
      await this.$auth.loginWith('local', {
        data: user
      })
      $nuxt.$emit('snackbar', { color: 'success', text: 'ВХОД ВЫПОЛНЕН' })
      await $nuxt.$emit('drawer-close')
    } catch (error) {
      let text = 'Ошибка при входе'
      if (error.response && error.response.status === 401) {
        text = 'Не верные данные'
      }
      $nuxt.$emit('snackbar', { color: 'error', text })
    }
  },
  async update ({ state, dispatch }, user) {
    const formData = new FormData()
    const keys = Object.keys(user)
    keys.forEach(key => {
      if (key !== 'image' || key === 'image' && user[key] && typeof user[key] === 'object') {
        formData.append(key, user[key])
        console.log(key + ':' + JSON.stringify(user[key]))
        console.log(typeof user[key])
      }
    });
    formData.getAll('image');
    try {
      const response = await this.$axios.patch(
        '/api/my-user/', formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
      console.log('Success: ' + JSON.stringify(response.data))
      if (response.status === 200) {
        $nuxt.$emit('snackbar', { color: 'success', text: 'Изменения профиля сохранены' })
        await this.$auth.fetchUser()
      }
      console.log('STATUS: ' + JSON.stringify(response.status))
    } catch (error) {
      console.log('STATUS in error: ' + JSON.stringify(error.response.status))
      console.log('STATUS in error response: ' + JSON.stringify(error.response))
      console.log('Error: ', error)
      $nuxt.$emit('snackbar', { color: 'error', text: 'Ошибка при обновлении профиля' })
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
      console.log(JSON.stringify(response.data.user))
      await commit('SET_USER', response.data.user)
      await commit('SET_NUMBERS', response.data.numbers)
    } catch (error) {
      // eslint-disable-next-line no-console
      console.log('auth_error_login_action', error)
    }
  },
  async logout () {
    await this.$auth.logout()
    $nuxt.$emit('snackbar', { color: 'primary', text: 'Вы вышли из профиля' })
  },
}
