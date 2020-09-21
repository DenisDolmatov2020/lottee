<template>
  <div
    class="prizes"
  >
    <div
      v-for="(lot, i) in l"
      :key="i"
    >
      <div class="prize">
        <div
          v-if="lot.active"
          class="cap"
          :class="{ 'cap-hover': hoverOpen(lot) }"
          @mouseenter="lotOpen(lot.id)"
        >
          <span
            v-if="lot.user.id === user.id || !!numbers[String(lot.id)]"
            :class="[ 'my-number', { 'my-number-new': my_number === lot.id }]"
          >
            {{ lot.user.id === user.id ? 'Ваш' : `#${numbers[String(lot.id)]}` }}
          </span>
          <span
            v-else
            :class="['btn', { 'btn-hover': hoverOpen(lot) }, { 'active': user.energy >= lot.energy }]"
            @click="lotDetail(lot)"
          >
            {{ user.energy >= lot.energy ? 'Принять участие' : 'Недостаточно энергии' }}
            <br>
            <span v-if="user.energy >= lot.energy">
              <img
                width="24px"
                alt="flash"
                :src="require('~/assets/icons/flash.svg')"
              >
              <span class="btn-count-energy">
                {{ lot.energy }}
              </span>
            </span>
          </span>
        </div>
        <div v-else>
          <div class="cap-free">
            <span
              v-if="lot.user.id === user.id"
              :class="[ 'my-number', { 'my-number-new': my_number === lot.id }]"
            >
              {{ lot.user.id === user.id ? 'Ваш' : `#${numbers[String(lot.id)]}` }}
            </span>
          </div>
          <div
            v-if="lot.wins"
            class="show-winners"
          >
            <div
              v-for="win in lot.wins"
              :key="win.id"
            >
              #{{ win.num }}
            </div>
          </div>
        </div>
        <div
          :class="['label', { 'label-hover': hoverOpen(lot) }, { 'label-wins': !lot.free }]"
        >
          <div class="lot">
            <span class="lot-title">
              {{ lot.title.slice(0, 9) }}
              <br>
              {{ lot.title.slice(9, 18) }}
              <br>
              {{ lot.title.slice(18,) }}
            </span>
            <span
              v-if="lot.user"
              class="lot-owner"
            >
              {{ lot.user.id === user.id ? 'Ваш лот' : lot.user.name }}
            </span>
          </div>
        </div>
        <div
          v-if="lot.free"
          :class="['rope', { 'rope-hover': hoverOpen(lot) }]"
        />
        <div class="box">
          <figure
            v-if="lot.image"
            class="photo"
            :style="`background-image: url(${lot.image})`"
          >
            <span class="winners">
              x{{ lot.winners }}
            </span>
          </figure>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Lot',
  async fetch ({ store }) {
    await store.dispatch('lot/fetchLots')
  },
  data: () => ({
    visible: false,
    lot: {},
    lot_paid: false,
    lots: [],
    hover: null,
    my_number: null
  }),
  computed: {
    numbers () {
      return this.$store.getters['user/numbers']
    },
    user () {
      return this.$store.getters['user/user']
    },
    l () {
      // NEED switch
      let lots = this.$store.getters['lot/lots']
      if (this.$store.getters['lot/filter'] === 'active') {
        lots = lots.filter(lot => lot.active === true)
      } else if (this.$store.getters['lot/filter'] === 'have') {
        lots = lots.filter(lot => this.numbers[lot.id])
      } else if (this.$store.getters['lot/filter'] === 'my') {
        lots = lots.filter(lot => lot.user.id === this.$store.getters['user/user'].id)
      }
      return lots
    }
  },
  methods: {
    hoverOpen (lot) {
      return this.$store.getters['user/isAuthenticated'] &&
        this.hover === lot.id &&
        +lot.user.id !== +this.user.id &&
        lot.active
    },
    lotOpen (id) {
      this.hover = id
    },
    errorNotifications () {
      this.$store.dispatch(
        'notification/set_notification',
        { title: 'Возникла ошибка при попытке взять номер', class: 'error' }
      )
    },
    async lotDetail (lot) {
      this.lot = await lot
      await this.$router.push({ name: 'lots-id', params: { id: lot.id, lot } })
      // await this.$store.commit('lot/SET_LOT', lot)
      // await this.$nuxt.$emit('drawer', 'Detail')
    },
    async takeNumber (lot) {
      if (this.user.energy >= lot.energy) {
        try {
          const response = await this.$axios({
            url: `/api/lots/number/${lot.id}/`,
            method: 'POST'
          })
          if (response.status === 200) {
            this.my_number = lot.id
            this.$store.commit('user/SET_NUMBER', response.data.number)
            await this.$store.commit('user/SET_ENERGY', response.data.user_energy)
            await this.$store.dispatch(
              'notification/set_notification',
              { title: `Ваш номер ${response.data.number.num}`, class: 'success' }
            )
            setInterval(this.my_number = null, 3000)
          } else {
            await this.errorNotifications()
          }
        } catch (error) {
          await this.errorNotifications()
        }
      }
    }
  }
}
</script>

<style lang="scss" scoped>

.lightbox:target {
  opacity: 1;
  visibility: visible;
}
.prizes {
  display: flex;
  flex-wrap: wrap;
  padding: 0 150px;
  justify-content: space-around;
  .prize {
    width: 300px;
    height: 310px;
    margin: 100px;
    .show-winners {
      position: absolute;
      width: 250px;
      height: 75px;
      margin-left: 55px;
      margin-top: 8px;
      font-size: 18px;
      font-family: cursive;
      display: flex;
      justify-content: space-around;
      flex-wrap: wrap;
      div {
        width: 60px;
        height: 60px;
        line-height: 60px;
        border-radius: 50%;
        border: 3px solid #FEFEFE;
        text-align: center;
        background-color: rgba(0, 0, 0, 0.5);
        cursor: pointer;
      }
    }
    .cap-free {
      position: absolute;
      z-index: 2;
      margin-top: 70px;
      margin-left: -205px;
      width: 325px;
      height: 145px;
      background: url(~@/assets/images/prize/cap_free.png) no-repeat;
      transform: rotate(-65deg);
      .my-number {
        position: absolute;
        top: 85px;
        left: 20px;
        font-size: 32px;
        color: #424242;
        transition: 3s;
      }
    }
    .cap {
      position: absolute;
      z-index: 1;
      margin-top: -115px;
      width: 340px;
      height: 215px;
      background: url(~@/assets/images/prize/cap_2.png) no-repeat;
      transition: 1s;
      .my-number {
        position: absolute;
        /* margin-top: -103px; */
        top: 155px;
        left: 40px;
        font-size: 32px;
        color: #424242;
        transform: rotate(-25deg);
        transition: 3s;
      }
      .my-number-new {
        transition: 3s;
        transform: scale(10);
      }
      .btn {
        width: 110px;
        height: 67px;
        letter-spacing: -1px;
        border-radius: 5px;
        padding: 5px;
        margin-top: 222px;
        margin-left: 57px;
        color: #F44336;
        box-shadow: 0 0 10px 0 #F44336 inset;
        opacity: 0;
        transition: opacity 0s;
      }
      .active {
        color: #FEFEFE;
        box-shadow: 0 0 10px 0 #FFFFFF inset;
        opacity: 0;
        transition: opacity 0s;
        &:hover {
          background-color: rgba(255, 255, 255, 0.8);
          color: #0d47a1;
          box-shadow: 0 0 10px 0 #0d47a1 inset;
        }
      }
      .btn-u {
        width: 90px;
        height: 47px;
        padding: 15px;
        background-color: #FEFEFE;
        color: #424242;
        margin-top: 222px;
        margin-left: 57px;
        border-radius: 5px;
      }
      .btn-2 {
        flex-wrap: wrap;
        margin-left: 180px;
        margin-top: -80px;
        width: 105px;
        height: 55px;
        padding: 10px;
        background-color: rgba(0, 0, 0, 0.1);
      }
      .btn-hover {
        transition-delay: 0.8s;
        opacity: 1;
        span {
          .btn-count-energy {
            color: #0d47a1;
            margin-left: -7px;
            font-size: 24px;
          }
        }
      }
    }
    .cap-hover {
      margin-top: -215px;
      height: 315px;
    }
    .rope {
      z-index: 8;
      position: absolute;
      margin-left: 155px;
      margin-top: -53px;
      width: 35px;
      height: 400px;
      background: url(~@/assets/images/prize/rope.png) no-repeat;
      transition: 1s;
    }
    .rope-hover {
      margin-top: -153px;
    }
    .label {
      z-index: 3;
      position: absolute;
      margin-left: 265px;
      margin-top: -10px;
      width: 185px;
      height: 185px;
      background: url(~@/assets/images/prize/labe.png) no-repeat;
      transition: 1s;
      &:hover {
        transform: rotate(-45deg) translateY(-32px) translateX(92px) scale(1.2);
      }
      .lot {
        position: absolute;
        width: 130px;
        height: 75px;
        margin-left: 43px;
        margin-top: 67px;
        display: flex;
        flex-direction: column;
        color: #424242;
        transform: rotate(46deg);
        .lot-title {
          font-weight: 600;
          font-size: 18px;
          color: #35495e;
          // letter-spacing: 1px;
        }
        .lot-owner {
          position: absolute;
          bottom: 0;
          right: 0;
        }
        .logo {
          width: 38px;
          height: 38px;
          border-radius: 50%;
        }
      }
    }
    .label-hover {
      margin-top: -110px;
    }
    .label-wins {
      z-index: 1;
      margin-left: -50px;
      margin-top: 260px;
      transform: rotate(-44deg) translateY(-32px) translateX(92px) scale(1.0);
      &:hover {
        transform: rotate(-46deg) translateY(-32px) translateX(92px) scale(1.0);
      }
    }
    .box {
      margin-top: 115px;
      margin-left: 31px;
      width: 300px;
      height: 310px;
      background: url(~@/assets/images/prize/box_2.png) no-repeat;
      figure.photo {
        color: #fff;
        position: relative;
        overflow: hidden;
        top: 95px;
        left: 22px;
        max-width: 255px;
        height: 207px;
        background: #000000;
        background: center center no-repeat;
        background-size: cover;
        .winners {
          color: #424242;
          position: absolute;
          right: 3px;
          bottom: 3px;
          padding: 8px;
          width: 30px;
          height: 30px;
          text-align: center;
          border-radius: 50px;
          background-color: #FEFEFE;
        }
      }
    }
  }
}
</style>
