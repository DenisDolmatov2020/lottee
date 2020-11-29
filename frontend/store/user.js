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
        this.$router.replace('/login?page=2')
        $nuxt.$emit('snackbar', { color: 'error', text: 'Токен устарел, попробуйте заново' })
      })
  },
  async update ({ state, dispatch }, user) {
    const formData = new FormData()
    const keys = Object.keys(user)
    keys.forEach(key => {
      if (key !== 'image' || key === 'image' && user[key] && typeof user[key] === 'object') {
        formData.append(key, user[key])
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
      if (response.status === 200) {
        $nuxt.$emit('snackbar', { color: 'success', text: 'Изменения профиля сохранены' })
        await this.$auth.fetchUser()
      }
    } catch (error) {
      $nuxt.$emit('snackbar', { color: 'error', text: 'Ошибка при обновлении профиля' })
    }
  },
  async logout () {
    await this.$auth.logout()
    this.$router.push('/login')
    $nuxt.$emit('snackbar', { color: 'primary', text: 'Вы вышли из профиля' })
  }
}
