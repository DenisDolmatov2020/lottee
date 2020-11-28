/* eslint-disable */

export const actions = {
  async register ({ dispatch }, user) {
    try {
      const response = await this.$axios({
        url: '/api/my-user/create/',
        method: 'POST',
        data: user
      })
      if (response.status === 201) await dispatch('login', user)
      else $nuxt.$emit('snackbar', { color: 'error', text: 'Такой пользователь уже существует' })
    } catch (error) {
      console.error('ERROR REGISTRATION ' + JSON.stringify(error))
      $nuxt.$emit('snackbar',
        { color: 'error', icon: 'mdi-list-status', text: 'Эта почта уже зарегистрирована попробуйте войти' }
      )
    }
  },
  async login ({ commit, dispatch }, user) {
    try {
      await this.$auth.loginWith('local', { data: user})
      $nuxt.$emit('snackbar', { color: 'success', text: 'ВХОД ВЫПОЛНЕН' })
      dispatch('track/trackerTimer', null, { root: true })
      await $nuxt.$emit('drawer-close')
    } catch (error) {
      let text = 'Ошибка при входе'
      if (error.response && error.response.status === 401) {
        text = 'Не верные данные'
      }
      $nuxt.$emit('snackbar', { color: 'error', text })
    }
  },
  async reset ({ commit, dispatch }, user) {
    await this.$axios.post('/api/my-user/password_reset/', user)
      .then(() => {
        $nuxt.$emit('snackbar', { color: 'primary', text: 'Инструкция сброса отравлена на почту' })
        this.$router.push('/')
      })
      .catch(() => { $nuxt.$emit('snackbar', { color: 'error', text: 'Нет пользователя с таким адресом' })})
  },
  async confirm ({ commit, dispatch }, user) {
    await this.$axios.post('/api/my-user/password_reset/confirm/', user)
      .then(() => {
        $nuxt.$emit('snackbar', { color: 'success', text: 'Новый пароль сохранен' })
        this.$router.push('/')
      })
      .catch(() => {
        $nuxt.$emit('snackbar', { color: 'error', text: 'Токен устарел, попробуйте заново' })
        this.$router.push('/')
      })
  },
  async valid ({ commit, dispatch }, user) {
    console.log('V')
    await this.$axios.post('/api/my-user/password_reset/validate_token/', user)
      .then(async (response) => {
        await console.log(response)
      })
      .catch(async (error) => {
        // await console.error(error)
        await this.$router.push('/')
        console.log('C')
      })
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
    })
    formData.getAll('image')
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
      console.error(error)
      $nuxt.$emit('snackbar', { color: 'error', text: 'Ошибка при обновлении профиля' })
    }
  },
  /*
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
  */
  async logout () {
    await this.$auth.logout()
    this.$router.push('/login')
    $nuxt.$emit('snackbar', { color: 'primary', text: 'Вы вышли из профиля' })
  }
}
