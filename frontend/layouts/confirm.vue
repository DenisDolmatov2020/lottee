<template>
  <div style="text-align: center; margin-top: 300px;">
    <div v-if="ok">
      Почта подтверждена, через {{ time_seconds }}с. произойдет переход на страницу логина
    </div>
    <div v-else>
      Этот токен устарел попробуйте заново
      <v-btn dark @click="$router.push('/login?page=1')">
        Перейти
      </v-btn>
    </div>
  </div>
</template>

<script>
export default {
  async fetch () {
    if (this.$route.query.user_id && this.$route.query.token) {
      try {
        const response = await this.$axios.post('/api/my-user/confirm-email/',
          { user_id: +this.$route.query.user_id, token: this.$route.query.token }
        )
        console.log(JSON.stringify(response.status))
        if (response.status === 200) {
          this.ok = true
          console.log(JSON.stringify('EMAIL confirmed'))
        } else if (response.status === 226) {
          this.ok = false
          console.log(JSON.stringify('OLDEST TOKEN'))
        }
      } catch (error) {
        this.ok = false
      }
    }
  },
  data () {
    return {
      ok: true,
      time_seconds: 5,
      text: 'Идет проверка данных'
    }
  },
  watch: {
    time_seconds (value) {
      if (!value) {
        this.$router.push('/login?page=1')
      }
    }
  },
  async created () {
    await setInterval(() => {
      this.time_seconds -= 1
    }, 1000)
  }
}
</script>

<style scoped>

</style>
