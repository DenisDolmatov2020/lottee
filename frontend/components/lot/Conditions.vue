<template>
  <div>
    <div
      class="header"
    >
      <img
        v-if="condition.icon"
        class="icon-cloud"
        :src="require(`~/assets/icons/${condition.icon}.svg`)"
      >
      <div class="field">
        <img
          alt="user icon"
          class="icon-link"
          :src="require(`~/assets/icons/${condition.value ? 'link_success' : 'link'}.svg`)"
        >
        <div class="box-field">
          <input
            v-model="condition.link"
            name="link"
            type="text"
            placeholder="Ссылка"
            required
            @input="initLink"
          >
        </div>
      </div>
      <img
        v-if="readyCondition && company_paid"
        alt="add condition"
        class="icon-plus"
        :src="require(`~/assets/icons/plus.svg`)"
        @click="addCondition"
      >
    </div>
    <section>
      <div
        v-if="subscribe && condition.value"
        @click="condition.subscribe = !condition.subscribe"
      >
        <span :class="['option', { 'option-active': condition.subscribe }]">
          <span
            v-if="condition.subscribe"
            class="check-round"
          />
          Подписка
        </span>
      </div>
      <div
        v-if="like && condition.value"
        @click="condition.like = !condition.like"
      >
        <span :class="['option', { 'option-active': condition.like }]">
          <span
            v-if="condition.like"
            class="check-round"
          />
          Лайк
        </span>
      </div>
      <div
        v-if="repost && condition.value"
        @click="condition.repost = !condition.repost"
      >
        <span :class="['option', { 'option-active': condition.repost }]">
          <span
            v-if="condition.repost"
            class="check-round"
          />
          Репост
        </span>
      </div>
      <div
        v-if="comment && condition.value"
        @click="condition.comment = !condition.comment"
      >
        <span :class="['option', { 'option-active': condition.comment }]">
          <span
            v-if="condition.comment"
            class="check-round"
          />
          Коммент
        </span>
      </div>
    </section>
    <div
      v-for="(c, i) in conditions.slice().reverse()"
      :key="i"
      class="condition-item"
      :style="`border-color: ${c.color}; background-color: ${c.color}1a`"
    >
      <div>
        <div class="flex">
          <img
            :src="require(`~/assets/icons/${c.icon}.svg`)"
            class="icon-condition"
          >
          <div
            v-if="c.subscribe"
            class="action-item"
          >
            Подписка
          </div>
          <div
            v-if="c.like"
            class="action-item"
          >
            Лайк
          </div>
          <div
            v-if="c.repost"
            class="action-item"
          >
            Репост
          </div>
          <div
            v-if="c.comment"
            class="action-item"
          >
            Коммент
          </div>
          <div
            class="icon-close"
            @click="conditions.splice(conditions.length - i - 1, 1)"
          >
            x
          </div>
        </div>
        <div class="c-title">
          {{ c.title }}
          {{ c.link }}
        </div>
      </div>
    </div>
    <div
      class="buttons"
    >
      <div
        class="btn btn-next"
        @click="addLot"
      >
        Создать
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Conditions',
  props: {
    lot: {
      type: Object,
      default: () => {}
    }
  },
  data () {
    return {
      company_paid: true,
      conditions: [],
      condition: {},
      subscribe: false,
      like: false,
      comment: false,
      repost: false
    }
  },
  computed: {
    readyCondition () {
      return this.condition.link && this.condition.value
    }
  },
  beforeMount () {
    this.initCondition()
  },
  methods: {
    initCondition () {
      this.condition = {
        title: '',
        link: '',
        value: false,
        icon: 'cloud',
        color: '#424242',
        subscribe: false,
        like: false,
        comment: false,
        repost: false
      }
      this.subscribe = false
      this.like = false
      this.comment = false
      this.repost = false
    },
    addCondition () {
      if (this.readyCondition) {
        this.conditions.push(this.condition)
        this.initCondition()
      }
    },
    async addLot () {
      if (this.lot.title) {
        // await this.$nuxt.$emit('preload-on')
        await this.addCondition()
        this.$emit('createLot', this.conditions)
      }
    },
    initLink () {
      let site = this.condition.link
      site = site.trim().replace(/(^\w+:|^)\/\//, '').replace(/^www.|/, '')
      site = site.split('/')
      this.condition.value = true
      this.condition.subscribe = true
      this.subscribe = true
      if (site[1] && (site[0] === 'youtube.com' || site[0] === 'youtu.be')) {
        this.condition.icon = 'youtube'
        this.condition.color = '#F44336'
        this.condition.title = 'Youtube'
        if (site[1] && site[1].indexOf('watch') === 0) {
          this.condition.like = false
          this.like = true
          this.condition.commit = false
          this.comment = true
        }
      } else if (site[1] && (site[0] === 'facebook.com' || site[0] === 'fb.com')) {
        this.condition.icon = 'fb'
        this.condition.color = '#1565C0'
        this.condition.title = 'Facebook'
        if (site[2] === 'videos' || site[2] === 'photos' || site[1].indexOf('photo.php') === 0) {
          this.condition.like = false
          this.like = true
          this.condition.commit = false
          this.comment = true
          this.condition.repost = false
          this.repost = true
        }
      } else if (site[0] === 'instagram.com' && site[1]) {
        this.condition.icon = 'instagram'
        this.condition.color = '#5e35b1'
        this.condition.title = 'Instagram'
        if (site[1] === 'p') {
          this.condition.like = false
          this.like = true
          this.condition.commit = false
          this.comment = true
        }
      } else if (site[0] === 'twitter.com' && site[1]) {
        this.condition.icon = 'twitter'
        this.condition.color = '#00bcd4'
        this.condition.title = 'Twitter'
        if (site[2] === 'status') {
          this.condition.like = false
          this.like = true
          this.condition.commit = false
          this.comment = true
          this.condition.repost = false
          this.repost = true
        }
      } else {
        this.condition.value = false
        this.condition.icon = 'cloud'
        this.condition.like = false
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.c-title {
  width: 90%;
  word-break: break-all;
}
.buttons {
  display: flex;
  width: 100%;
}
.btn {
  margin-left: auto;
  padding: 10px;
  width: 200px;
}
.btn-next {
  box-shadow: 0 0 40px 40px #81D4FA inset, 0 0 0 0 #81D4FA;
}
.icon-close {
  margin-left: auto;
  margin-top: -20px;
  font-size: x-large;
}
.icon-condition {
  width: 36px;
}
.action-item {
  background-color: #424242;
  padding: 5px;
  margin: 0 1em;
  border-radius: 20px;
  border-width: 2px;
  border-style: groove;
}
.condition-item {
  width: 90%;
  color: #ffffff;
  border-width: 3px;
  border-style: groove;
  border-radius: 20px;
  padding: 1em;
  margin: 1.5em;
}
.icon-plus {
  width: 50px;
  cursor: pointer;
}
.fields {
  width: 100%;
}
.field {
  width: 100%;
}
.box-field {
  width: 100%;
}
.box-field input {
  width: 100%;
  padding-left: 32px;
}
.header {
  display: flex;
}
@media screen and (max-width: 292px) {
  .header {
    flex-direction: column;
  }
}
.icon-cloud {
  min-width: 42px;
  margin: 1em;
}
.icon-link {
  position: absolute;
  width: 28px;
  margin-top: 7px;
  margin-left: 3px;
}
section {
  display: flex;
  flex-flow: row wrap;
}
section > div {
  flex: 1;
  padding: 0.5rem;
}

.option {
  max-width: 250px;
  height: 50px;
  display: block;
  background: #424242;
  border: 2px solid #81D4FA;
  border-radius: 20px;
  padding: 1rem;
  margin-bottom: 1rem;
  text-align: center;
  position: relative;
  cursor: pointer;
}
.option-active {
  background: #81D4FA;
  color: hsla(215, 0%, 100%, 1);
  box-shadow: 0 0 20px #81D4FA;
}
.check-round {
   color: hsla(215, 5%, 25%, 1);
   font-family: cursive;
   border: 2px solid #81D4FA;
   content: url('https://api.iconify.design/mdi:check-outline.svg?height=24&color=green');
   font-size: 24px;
   position: absolute;
   top: -12px;
   left: 28px;
   transform: translateX(-50%);
   border-radius: 50%;
   background: white;
   box-shadow: 0 2px 5px -2px #81D4FA;
}

</style>
