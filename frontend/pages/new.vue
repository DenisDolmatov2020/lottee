<template>
  <div class="profile-page">
    <div class="profile-container">
      <div class="profile">
        <div class="profile-title">
          <div
            style="cursor: pointer; margin-left: 15px;"
            @click="$router.push('/')"
          >
            X
          </div>
          <div>
            Новый лот
          </div>
          <div />
        </div>
        <div class="steps">
          <div
            v-for="(tab, index) of tabs"
            :key="index"
            :class="['step', { 'step-active': index === active_tab, 'step-pointer': lot.title.length && lot.title.length <= 48 && index !== active_tab }]"
            @click="active_tab = lot.title ? index : 0"
          >
            {{ tab }}
          </div>
        </div>
        <div v-if="active_tab === 0">
          <div class="fields">
            <div
              class="field-title field"
            >
              <img
                alt="user icon"
                class="icon-field"
                :src="require('~/assets/icons/gift.svg')"
              >
              <div class="wthree-field">
                <input
                  id="lot-title"
                  v-model="lot.title"
                  name="title"
                  type="text"
                  value=""
                  placeholder="Название"
                  required
                >
              </div>
            </div>
            <div
              class="field-description field"
            >
              <img
                alt="email icon"
                class="icon-field"
                :src="require('~/assets/icons/pen_description.svg')"
              >
              <div class="wthree-field">
                <input
                  id="email"
                  v-model="lot.description"
                  name="description"
                  type="text"
                  value=""
                  placeholder="Описание"
                  required
                >
              </div>
            </div>
          </div>
          <ul class="img-list">
            <li>
              <img
                v-if="lot.image"
                :src="makeImage(lot.image)"
              >
              <span
                v-else
                class="img-placeholder"
              >
                - Image -
              </span>
              <input
                type="file"
                class="img-item"
                accept="image/*"
                @change="fileChange"
              >
            </li>
          </ul>
        </div>
        <section
          v-else-if="active_tab === 1"
          id="content"
        >
          <v-col cols="12">
            <v-subheader class="pl-0">
              Количество участников
              {{ lot.players }}
            </v-subheader>
            <v-slider
              v-model="lot.players"
              dense
              thumb-label
              :min="rules.players.min"
              :max="rules.players.max"
            >
              <template v-slot:append>
                <v-text-field
                  v-model="lot.players"
                  class="mt-0 pt-0"
                  hide-details
                  single-line
                  type="number"
                  style="width: 60px"
                  :min="rules.players.min"
                  :max="rules.players.max"
                />
              </template>
            </v-slider>
          </v-col>

          <v-col cols="12">
            <v-subheader class="pl-0">
              Количество победителей
              {{ lot.winners }}
            </v-subheader>
            <v-slider
              v-model="lot.winners"
              thumb-label
              step="1"
              ticks="always"
              tick-size="4"
              :color="rules.winners.color"
              :track-color="rules.winners.track_color"
              :min="rules.winners.min"
              :max="rules.winners.max"
            >
              <template v-slot:append>
                <v-text-field
                  v-model="lot.winners"
                  class="mt-0 pt-0"
                  hide-details
                  single-line
                  type="number"
                  style="width: 60px"
                  :min="rules.winners.min"
                />
              </template>
            </v-slider>
          </v-col>
          <v-col cols="12">
            <v-subheader class="pl-0">
              Цена за 1 приз
              {{ rules.price.value }}
              {{ rules.price.value === 9999 ? '+' : '' }}
              {{ rules.price.price === 1000 ? 'и меньше' : '' }}
            </v-subheader>
            <v-slider
              v-model="rules.price.value"
              thumb-label="always"
              :color="rules.price.color"
              :track-color="rules.price.track_color"
              :step="100"
              :min="rules.price.min"
              :max="rules.price.max"
            >
              <template v-slot:append>
                <v-text-field
                  v-model="rules.price.value"
                  single-line
                  type="number"
                  style="width: 60px"
                  :min="rules.price.min"
                  :max="rules.price.max"
                />
              </template>
            </v-slider>
          </v-col>
        </section>
        <section
          v-show="active_tab === 2"
        >
          <conditions
            :lot="lot"
            @createLot="addLot"
          />
        </section>
        <div
          class="buttons"
        >
          <div
            v-if="0 < lot.title.length && lot.title.length <= 48 && active_tab < 2"
            class="btn btn-next"
            @click="active_tab += 1"
          >
            Далее
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'New',
  data () {
    return {
      active_tab: 0,
      tabs: ['Приз', 'Опции', 'Условия'],
      files: [],
      lot: {
        title: '',
        creator: 1,
        description: '',
        players: 1,
        winners: 1,
        energy: 1,
        conditions: [],
        image: null,
        image_two: null,
        image_three: null,
        image_four: null
      },
      rules: {
        winners: {
          min: 1,
          max: 10
        },
        price: {
          value: 1000,
          min: 0,
          max: 9999
        },
        players: {
          min: 1,
          max: 9999
        }
      }
    }
  },
  watch: {
    price (v) {
      this.lot.energy = Math.floor(v / 1000) + 1
    }
  },
  methods: {
    makeImage (file) {
      return URL.createObjectURL(file)
    },
    fileChange (event) {
      this.lot.image = event.target.files[0]
    },
    async addLot (conditions) {
      await this.$nuxt.$emit('preload-on')
      await this.$store.dispatch('lot/fetchLot', { lot: this.lot, conditions })
    }
  }
}
</script>
<style lang="sass" scoped>
.file-upload-form, .image-preview
  font-family: "Helvetica Neue",Helvetica,Arial,sans-serif
  padding: 20px
img.preview
  width: 200px
  background-color: white
  border: 1px solid #DDD
  padding: 5px
.cube-container
  display: flex
.cube-header
  z-index: 998
  position: absolute
  display: flex
  text-shadow: 1px 1px 1px #FFFFFF
  font-size: 24px
// left: 150px
.range
  position: absolute
  width: 100%
  cursor: pointer
  z-index: 999
  margin-top: 1px
  height: 60px
  background: transparent
  -webkit-appearance: none
  outline: none
  border: none
  &::-webkit-slider-runnable-track
    width: 100%
    height: 1px
    cursor: pointer
    box-shadow: none
    border-radius: 0
    -webkit-appearance: none
  &::-moz-range-track
    width: 100%
    height: 3px
    cursor: pointer
    box-shadow: none
    background: #ffffff
    border-radius: 0
    -webkit-appearance: none
  &::-webkit-slider-thumb
    height: 42px
    width: 15px
    border-radius: 22px
    background: rgba(255,255,255,1)
    cursor: pointer
    -webkit-appearance: none
    margin-top: -20px
  &::-moz-range-thumb
    box-shadow: 0 10px 10px rgba(0,0,0,0.25)
    height: 42px
    width: 15px
    border-radius: 22px
    background: rgba(255,255,255,1)
    cursor: pointer
    -webkit-appearance: none
    margin-top: -20px
.buttons
  display: flex
  width: 100%
.btn
  margin: 50px 20px 30px auto
  padding: 10px
  width: 200px
.btn-next
  box-shadow: 0 0 40px 40px #81D4FA inset, 0 0 0 0 #81D4FA
.btn-next:hover
  color: #81D4FA
  box-shadow: 0 0 10px 0 #81D4FA inset, 0 0 10px 4px #81D4FA
.img-list
  list-style: none
  padding: 0
  margin: 0
  li
    border: 5px solid transparent
    box-sizing: border-box
    width: 25%
    float: left
    position: relative
    cursor: pointer
    .img-item
      width: 100%
      height: 100%
      cursor: pointer
      position: absolute
      top: 0
      left: 0
      z-index: 1000
      /* visibility: hidden; */
      opacity: 0
  img
    max-width: 100%
    vertical-align: middle

/* Image Placeholder Styles  */
.img-placeholder:before,
.img-placeholder:after
  padding-top: 33.33%
  content: ""
  display: block
.img-placeholder
  background: #222
  box-shadow: 0 0 0 8px #222 inset, 0 0 0 9px #333 inset
  color: #444
  line-height: 0
  text-align: center
  display: block

/* The hover effect  */
.img-list li:before
  transition: all .5s ease
  content: ""
  position: absolute
  top: 0
  left: 0
  right: 0
  bottom: 0
  background: #333
  transform: scale(0)
.img-list li:hover:before
  opacity: .5
  transform: scale(1)
.img-list li:after
  transition: all .6s ease .2s
  content: ""
  position: absolute
  top: 8px
  left: 8px
  right: 8px
  bottom: 8px
  border: 1px solid #aaa
  background: #000
  opacity: 0
  transform: scale(0)
.img-list li:hover:after
  opacity: .35
  transform: scale(1)
.fields
  display: flex
  flex-wrap: wrap
  padding: 1em
.field
  display: flex
  padding: 1em
.wthree-field
  width: 100%
.field-title
  flex-basis: 250px
.field-description
  flex: 380px
.icon-field
  width: 36px
.steps
  display: flex
.step
  flex-basis: 262px
  height: 50px
  text-align: center
  padding-top: 12px
  transition: transform 0.5s ease 0.5s
  background-color: #424242

.step-active
  background: #81D4FA
  color: #424242
  border: none
  border-radius: 3px
  position: relative
  text-transform: uppercase
  letter-spacing: 0
  -webkit-box-shadow: 0 0 20px 5px rgba(129,212,250,1)
  -moz-box-shadow: 0 0 20px 5px rgba(129,212,250,1)
  box-shadow: 0 0 20px 5px rgba(129,212,250,1)
  will-change: box-shadow, transform
  /* transition: box-shadow 0.2s cubic-bezier(0.4, 0, 1, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1)
  /* transform: translate3d(-8px, 0px, 0px)
  transition: box-shadow 0.8s ease 0.3s
.step-pointer
  cursor: pointer

.description
  font-size: 15px
  color: grey

.icon-pen
  width: 38px
  height: 38px
  margin-top: 10px
  cursor: pointer

.colors-title
  font-size: 24px
  margin-left: 75px
  margin-bottom: 25px

.trackers
  width: 420px
  margin: 30px auto 0

.mh-professional-progress
  display: flex
  flex-wrap: wrap
  flex-basis: 320px
  justify-content: space-evenly

.progressbar-text
  position: absolute
  top: 50%
  left: 50%
  padding: 0
  margin: 0
  transform: translate(-50%, -50%)
  color: #00bcd4

ul
  list-style-type: disc
  margin-block-start: 1em
  margin-block-end: 1em
  margin-inline-start: 0
  margin-inline-end: 0
  padding-inline-start: 40px

ul li
  list-style-type: none

.mh-professional-progress li
  display: inline-block
  float: none
  max-width: 150px
  text-align: center

.mh-progress.mh-progress-circle
  display: inline-block
  width: 100px
  height: 100px

.mh-progress
  margin-bottom: 10px
  font: 900 1.1428571429em/1 Cinzel, cursive

.mh-professional-progress li
  display: inline-block
  margin: 10px 50px
  float: none
  max-width: 320px
  text-align: center

.dark-vertion .mh-progress path:nth-child(1)
  stroke: rgba(255, 255, 255, 0.5)

.mh-progress path:nth-child(2)
  stroke: #00bcd4
::placeholder
  font-family: cursive

.candidatos
  position: relative
  margin-bottom: 15px

.candidatos .parcial
  display: inline-block
  width: 100%
  vertical-align: middle

.candidatos .parcial .info
  position: relative

.candidatos .parcial .info .nome
  position: absolute
  top: 0
  left: 0
  font-size: 15px
  font-weight: 600
  opacity: 0.9

.candidatos .parcial .info .percentagem-num
  position: absolute
  top: 0
  right: 0
  font-size: 14px
  font-weight: normal

.dark-vertion .candidatos .parcial .progressBar
  background: rgba(199, 198, 198, 0.6)

.candidatos .parcial .progressBar
  position: relative
  width: 100%
  height: 7px
  margin: 30px 0 2px
  border-radius: 10px
  background: rgba(0, 0, 0, 0.5)

.candidatos .parcial .percentagem
  position: absolute
  top: 0
  left: 0
  height: 7px
  border-top-left-radius: 10px
  border-bottom-left-radius: 10px
  border-top-right-radius: 10px
  border-bottom-right-radius: 10px
  background: #00bcd4
  -webkit-transition: 3s all
  -webkit-animation-duration: 3s
  -webkit-animation-name: animationProgress
.profile-avatar, .checkboxes, .profile-info
  margin: 25px auto

.checkboxes
  margin-top: 30px

.field-checkbox
  margin-bottom: 10px
.field-group label
  font-size: 15px
.radio input
  position: absolute
  left: -9999px
.checkbox i
  position: absolute
  bottom: 5px
  left: 2px
  display: block
  width: 14px
  height: 14px
  outline: none
  border: none
  background: #fff
.check label
  margin: 0
  font-size: 1em
  text-transform: capitalize
  color: #fff
  letter-spacing: 1px
  font-weight: 300
.checkbox input:checked+i:after,
.radio input:checked+i:after
  opacity: 1
.checkbox input+i:after
  content: ''
  top: 0
  left: 0
  width: 14px
  height: 14px
  font: normal 8px/16px FontAwesome
  text-align: center
.checkbox input+i:after,
.radio input+i:after
  position: absolute
  opacity: 0
  transition: opacity 0.1s
  -o-transition: opacity 0.1s
  -ms-transition: opacity 0.1s
  -moz-transition: opacity 0.1s
  -webkit-transition: opacity 0.1s

.wthree-field input
  padding: 10px
  font-size: 14px
  color: #333
  letter-spacing: 1px
  border-color: #81D4FA
  border-width: 1px 1px 1px 1px
  background: #fff
  box-sizing: border-box
  font-family: 'Open Sans', sans-serif
  width: 100%
  outline: none
  border-top-right-radius: 30px
  border-bottom-right-radius: 30px

li:nth-child(2) a,
li:nth-child(2) a
  color: #fff
@media screen and (max-width: 375px)
  form .field-group .wthree-field
    flex: 3 37%
.profile-header
  display: flex
  justify-content: space-between
  flex-wrap: wrap

.profile-avatar
  width: 155px
  height: 155px
  background-size: cover
  border-radius: 50%
  border: 5px solid #81D4FA
  text-align: center
  justify-content: center

.profile-avatar-hover
  width: 156px
  height: 156px
  background-color: rgba(0, 0, 0, 0.99)
  opacity: 0
  border-radius: 50%
  margin: -5.5px
.profile-avatar-hover:hover
  opacity: 0.8
  padding-top: 35%
.profile-avatar-icon
  width: 50px
  height: 50px
/* #4dbfd9 #0bceaf #00bcd4 */
.profile-page
  // background: url('http://demos.creative-tim.com/material-bootstrap-wizard/assets/img/wizard-book.jpg') no-repeat center center fixed
  -webkit-background-size: cover
  -moz-background-size: cover
  -o-background-size: cover
  background-size: cover
  padding: 50px 0 150px 0
  font-family: cursive

.profile-container
  max-width: 50em
  margin: 1.5em auto
.profile
  background: rgba(0, 0, 0, 0.5)
  border-radius: 1px 1px 1px 0
  margin: 0 1em
  box-shadow: 12px 12px rgba(0, 0, 0, 0.6)
  -webkit-box-shadow: 12px 12px rgba(0, 0, 0, 0.6)
  -o-box-shadow: 12px 12px rgba(0, 0, 0, 0.6)
  -moz-box-shadow: 12px 12px rgba(0, 0, 0, 0.6)
  -ms-box-shadow: 12px 12px rgba(0, 0, 0, 0.6)
  font-weight: 600
  color: #81D4FA

.profile-title
  display: flex
  justify-content: space-between
  font-size: 36px
  margin: -20px auto 20px
  text-align: center
  font-family: Snell Roundhand, cursive, sans-serif

.user-back
  margin-top: 5px
  width: 48px
  height: 48px
/* range */
.cube
  position: relative
  width: 500px
  height: 60px
  margin: 2.5rem auto
  -webkit-transform-style: preserve-3d
  -moz-transform-style: preserve-3d
  -ms-transform-style: preserve-3d
  -o-transform-style: preserve-3d
  transform-style: preserve-3d
  -webkit-perspective: 320px
  -moz-perspective: 320px
  -ms-perspective: 320px
  -o-perspective: 320px
  perspective: 320px

  .slider-range-min
    position: absolute
    width: 94%
    left: 3%
    top: 27px
    margin: 0
    z-index: 999

  .ui-slider
    height: 5px
    border: none
    background: rgba(0,0,0,0.1)
    -webkit-box-shadow: 0 2px 2px rgba(255,255,255,0.25), inset 0 1px 3px rgba(0,0,0,0.3)
    -moz-box-shadow:   0 2px 2px rgba(255,255,255,0.25), inset 0 1px 3px rgba(0,0,0,0.3)
    box-shadow:        0 2px 2px rgba(255,255,255,0.25), inset 0 1px 3px rgba(0,0,0,0.3)

  .ui-slider:before, .ui-slider:after
    content: 'IIIIIIIIIII'
    position: absolute
    left: 2px
    width: 100%
    font-family:  'Source Sans Pro', sans-serif
    font-size: 1.2rem
    font-weight: 300
    color: rgba(0,0,0,0.3)
    letter-spacing: 37px
    text-shadow: 1px 1px 0 rgba(255,255,255,0.2)
    padding: 1em

  .ui-slider:before
    top: -1.4rem

  .ui-slider:after
    bottom: -1.4rem

  .ui-slider-range
    background: transparent
  .ui-slider .ui-slider-handle
    top: -8px
    width: 26px
    height: 20px
    margin-left: -15px
    padding-left: 4px
    border: none
    background: rgba(255,255,255,0.7)
    border-radius: 2px
    text-align: center
    font-family:  'Anonymous Pro', sans-serif
    font-size: 1.2rem
    line-height: 20px
    color: rgba(0,0,0,0.5)
    text-decoration: none
    letter-spacing: 3px
    cursor: pointer
    text-shadow: 1px 1px 2px rgba(255,255,255,1)
    -webkit-box-shadow: 1px 1px 8px rgba(0,0,0,0.3)
    -moz-box-shadow:    1px 1px 8px rgba(0,0,0,0.3)
    box-shadow:         1px 1px 8px rgba(0,0,0,0.3)

  .ui-slider .ui-slider-handle:focus
    outline: none

  /* typo */
  h1
    font-size: 2.7rem
    font-weight: 200
    color: rgba(0,0,0,0.7)
    text-shadow: 1px 1px 0 rgba(255,255,255,0.3)

  p
    font-size: 1.2rem
    font-weight: 300
    line-height: 1.8rem
    color: rgba(0,0,0,0.8)

  .credits a
    position: relative
    display: inline-block
    color: #529e0e
    text-decoration: none

  .credits a:after
    content: ''
    position: absolute
    left: -1.5%
    bottom: -1px
    width: 0%
    height: 1px
    background: #529e0e
    -webkit-transition: width 0.1s
    -moz-transition:    width 0.1s
    -o-transition:      width 0.1s
    transition:         width 0.1s

  .credits a:hover a:after
    width: 103%
  /* base */
  #content
    -webkit-box-sizing:  border-box
    -moz-box-sizing:    border-box
    box-sizing:         border-box
    width:  100%
    height:  100%
    padding-top:  5rem
    text-align:  center
  html, body
    height:  100%
    background-image:  -webkit-gradient(linear, left top, left bottom, from(rgba(0,0,0,0.08)), to(rgba(0,0,0,0.05)))
    background-image:  -webkit-linear-gradient(top, rgba(0,0,0,0.08), rgba(0,0,0,0.05))
    background-image:    -moz-linear-gradient(top, rgba(0,0,0,0.08), rgba(0,0,0,0.05))
    background-image:      -o-linear-gradient(top, rgba(0,0,0,0.08), rgba(0,0,0,0.05))
    background-image:         linear-gradient(to bottom, rgba(0,0,0,0.08), rgba(0,0,0,0.05))
    background-repeat:  no-repeat
    background-size:  100% 100%
    background-position:  0 0
    font-family:  'Source Sans Pro', sans-serif

.a, .b, .c, .d
  position: absolute
  width: 50%
  height: 100%
  left: 0
  z-index: 222

.a:before, .b:before, .c:before, .d:before, .a:after, .b:after
  content: ''
  position: absolute
  top: 0
  left: 0
  width: 500px
  height: 60px

.a:before, .b:before, .c:before, .d:before
  z-index: 111

.a:after, .b:after
  z-index: 333

.b
  top: 0
  -webkit-transform: rotateX(75deg) translateY(-60px)
  -moz-transform:    rotateX(75deg) translateY(-60px)
  -o-transform:      rotateX(75deg) translateY(-60px)
  -ms-transform:     rotateX(75deg) translateY(-60px)
  transform:         rotateX(75deg) translateY(-60px)
  -webkit-transform-origin: 0% 0%
  -moz-transform-origin:    0% 0%
  -o-transform-origin:      0% 0%
  -ms-transform-origin:     0% 0%
  transform-origin:         0% 0%

.c
  top: 0
  -webkit-transform: rotateX(75deg)
  -moz-transform:    rotateX(75deg)
  -o-transform:      rotateX(75deg)
  -ms-transform:     rotateX(75deg)
  transform:         rotateX(75deg)
  -webkit-transform-origin: 100% 100%
  -moz-transform-origin:    100% 100%
  -o-transform-origin:      100% 100%
  -ms-transform-origin:     100% 100%
  transform-origin:         100% 100%

.d
  -webkit-transform: translateZ(-60px) translateY(-15px)
  -moz-transform:    translateZ(-60px) translateY(-15px)
  -o-transform:      translateZ(-60px) translateY(-15px)
  -ms-transform:     translateZ(-60px) translateY(-15px)
  transform:         translateZ(-60px) translateY(-15px)

/* colors */
.a, .b
  background-image:  -webkit-gradient(linear, left top, left bottom, from(rgba(116,198,43,0.8)), to(rgba(116,198,43,0.8)))
  background-image:  -webkit-linear-gradient(top, rgba(116,198,43,0.8), rgba(116,198,43,0.8))
  background-image:     -moz-linear-gradient(top, rgba(116,198,43,0.8), rgba(116,198,43,0.8))
  background-image:       -o-linear-gradient(top, rgba(116,198,43,0.8), rgba(116,198,43,0.8))
  background-image:          linear-gradient(to bottom, rgba(116,198,43,0.8), rgba(116,198,43,0.8))
  background-repeat: no-repeat
  background-size: 100% 100%
  background-position: 0 0

.c, .d
  background-image: -webkit-gradient(linear, left top, left bottom, from(rgba(116,198,43,0.5)), to(rgba(116,198,43,0.5)))
  background-image: -webkit-linear-gradient(top, rgba(116,198,43,0.5), rgba(116,198,43,0.5))
  background-image:    -moz-linear-gradient(top, rgba(116,198,43,0.5), rgba(116,198,43,0.5))
  background-image:      -o-linear-gradient(top, rgba(116,198,43,0.5), rgba(116,198,43,0.5))
  background-image:         linear-gradient(to bottom, rgba(116,198,43,0.5), rgba(116,198,43,0.5))
  background-repeat: no-repeat
  background-size: 100% 100%
  background-position: 0 0

.c:before
  -webkit-box-shadow: 0 30px 20px -20px rgba(0,0,0,0.4), 0px 40px 15px -15px rgba(0,0,0,0.25)
  -moz-box-shadow:    0 30px 20px -20px rgba(0,0,0,0.4), 0px 40px 15px -15px rgba(0,0,0,0.25)
  box-shadow:         0 30px 20px -20px rgba(0,0,0,0.4), 0px 40px 15px -15px rgba(0,0,0,0.25)

.a:before, .b:before, .c:before, .d:before
  background-color: rgba(0,0,0,0.05)

.a:after
  background-image: -webkit-gradient(linear, left top, left bottom, from(rgba(0,0,0,0.07)), to(rgba(0,0,0,0)))
  background-image: -webkit-linear-gradient(top, rgba(0,0,0,0.07), rgba(0,0,0,0))
  background-image: -moz-linear-gradient(top, rgba(0,0,0,0.07), rgba(0,0,0,0))
  background-image: -o-linear-gradient(top, rgba(0,0,0,0.07), rgba(0,0,0,0))
  background-image: linear-gradient(to bottom, rgba(0,0,0,0.07), rgba(0,0,0,0))

.b:after
  background-image: -webkit-gradient(linear, left top, left bottom, from(rgba(255,255,255,0.1)), to(rgba(255,255,255,0.25)))
  background-image: -webkit-linear-gradient(top, rgba(255,255,255,0.1), rgba(255,255,255,0.25))
  background-image: -moz-linear-gradient(top, rgba(255,255,255,0.1), rgba(255,255,255,0.25))
  background-image: -o-linear-gradient(top, rgba(255,255,255,0.1), rgba(255,255,255,0.25))
  background-image: linear-gradient(to bottom, rgba(255,255,255,0.1), rgba(255,255,255,0.25))

.credits a
  position: relative
  display: inline-block
  color: #529e0e
  text-decoration: none

.credits a:after
  content: ''
  position: absolute
  left: -1.5%
  bottom: -1px
  width: 0%
  height: 1px
  background: #529e0e
  -webkit-transition: width 0.1s
  -moz-transition:    width 0.1s
  -o-transition:      width 0.1s
  transition:         width 0.1s

.credits a:hover::after
  width: 103%
.cube-price
  .a, .b, .c, .d
    background-color: rgba(76,175,80,0.8)
    background-image: linear-gradient(to bottom, rgba(76,175,80,0.8), rgba(76,175,80,0.8))
.cube-prize
  .a, .b, .c, .d
    background-color: rgba(100,58,123,0.8)
    background-image: linear-gradient(to bottom, rgba(100,58,123,0.8), rgba(100,58,123,0.8))
.cube-people
  .a, .b, .c, .d
    background-color: rgba(129,212,250,0.8)
    background-image: linear-gradient(to bottom, rgba(129,212,250,0.8), rgba(129,212,250,0.8))
</style>
