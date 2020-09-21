<template>
  <nav id="c-circle-nav" :class="['c-circle-nav', { 'is-active': is_active }]">
    <button
      id="c-circle-nav__toggle"
      :class="['logo-button', { 'is-active': is_active }]"
      @click="is_active = !is_active"
    >
      <div class="stage">
        <div class="layer" />
        <div class="layer" />
        <div class="layer" />
        <div class="layer" />
        <div class="layer" />
        <div class="layer" />
        <div class="layer" />
        <div class="layer" />
        <div class="layer" />
        <div class="layer" />
        <div class="layer" />
        <div class="layer" />
        <div class="layer" />
        <div class="layer" />
        <div class="layer" />
        <div class="layer" />
        <div class="layer" />
        <div class="layer" />
        <div class="layer" />
        <div class="layer" />
      </div>
    </button>
    <ul class="c-circle-nav__items">
      <li
        class="c-circle-nav__item btn-entry"
        @click="$router.push('new')"
      >
        Все
      </li>
      <li
        class="c-circle-nav__item btn-entry"
        @click="pushToLots('active')"
      >
        Активные
      </li>
      <li
        class="c-circle-nav__item btn-entry"
        @click="pushToLots('have')"
      >
        Я в игре
      </li>
      <li
        class="c-circle-nav__item btn-entry"
        @click="pushToLots('my')"
      >
        Мои
      </li>
      <li
        class="c-circle-nav__item btn-entry"
        @click="pushToCreateLot"
      >
        Создать
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'Menu',
  data () {
    return {
      is_active: false
    }
  },
  created () {
    this.$nuxt.$on('close', () => {
      this.is_active = !this.is_active
    })
  },
  methods: {
    openS () {
      console.log('NUXT S')
      this.$nuxt.$emit('snackbar', { color: 'error', text: '' })
    },
    pushToLots (f) {
      this.$store.commit('lot/SET_FILTER', f)
      this.$router.push('/')
      this.is_active = false
    },
    pushToCreateLot () {
      this.$router.push('/new')
      this.is_active = false
    }
  }
}
</script>

<style lang="scss" scoped>
.logo-button {
  width: 160px;
  height: 73px;
  z-index: 9999;
  position: absolute;
  cursor: pointer;
  outline: none;
  border: none;
  background-color: transparent;
  .stage {
    margin: auto;
    position: absolute;
    top: 0;
    left: 0;
    perspective: 9999px;
    transform-style: preserve-3d;
    cursor: pointer;
  }
}

.layer {
  width: 100%;
  height: 100%;
  position: absolute;
  transform-style: preserve-3d;
  animation: ಠ_ಠ 5s infinite alternate ease-in-out -7.5s;
  animation-fill-mode: forwards;
  transform: rotateY(40deg) rotateX(33deg) translateZ(0);
}

.layer:after {
  font: 38px cursive;
  content: 'Loottee';
  white-space: pre;
  text-align: center;
  height: 100%;
  width: 100%;
  position: absolute;
  top: 10px;
  left: 10px;
  color: darken(#fff, 4%);
  letter-spacing: -2px;
  text-shadow: 4px 0 10px hsla(0, 0%, 0%, .13);
}

$i: 1;
$NUM_LAYERS: 20;
@for $i from 1 through $NUM_LAYERS {
  .layer:nth-child(#{$i}):after{
    transform: translateZ(($i - 1) * -1.5px);
  }
}

.layer:nth-child(n+#{round($NUM_LAYERS/2)}):after {
  -webkit-text-stroke: 3px hsla(0, 0%, 0%, .25);
}

.layer:nth-child(n+#{round($NUM_LAYERS/2 + 1)}):after {
  -webkit-text-stroke: 15px dodgerblue;
  text-shadow: 6px 0 6px darken(dodgerblue,35%),
  5px 5px 5px darken(dodgerblue,40%),
  0 6px 6px darken(dodgerblue,35%);
}

.layer:nth-child(n+#{round($NUM_LAYERS/2 + 2)}):after {
  -webkit-text-stroke: 15px darken(dodgerblue, 10%);
}

.layer:last-child:after {
  -webkit-text-stroke: 17px hsla(0, 0%, 0%, .1);
}

.layer:first-child:after{
  color: #fff;
  text-shadow: none;
}

@keyframes ಠ_ಠ {
  100% { transform: rotateY(-40deg) rotateX(-43deg); }
}

.c-circle-nav {
  position: fixed;
  top: 12px;
  left: 12px;
  z-index: 1000;
  width: 60px;
  height: 60px;
  border-radius: 30px;
}

.c-circle-nav__items {
  display: block;
  list-style: none;
  position: absolute;
  z-index: 90;
  margin: 0;
  padding: 0;
}

.c-circle-nav__item {
  display: block;
  cursor: pointer;
  width: 100px;
  font-size: 20px;
  text-align: center;
  position: absolute;
  top: 0;
  left: 0;
  padding: 5px 4px;
  border-radius: 24px;
  opacity: 0;
  -webkit-transition-property: -webkit-transform, opacity;
  transition-property: transform, opacity;
  -webkit-transition-duration: 0.3s, 0.3s;
  transition-duration: 0.3s, 0.3s;
  -webkit-transition-timing-function: cubic-bezier(0.35, -0.59, 0.47, 0.97);
  transition-timing-function: cubic-bezier(0.35, -0.59, 0.47, 0.97);
}

/**
* Transisition delays at the default state.
*/

.c-circle-nav__item:nth-child(1) {
  -webkit-transition-delay: 0.4s;
  transition-delay: 0.4s;
}

.c-circle-nav__item:nth-child(2) {
  -webkit-transition-delay: 0.3s;
  transition-delay: 0.3s;
}

.c-circle-nav__item:nth-child(3) {
  -webkit-transition-delay: 0.2s;
  transition-delay: 0.2s;
}

.c-circle-nav__item:nth-child(4) {
  -webkit-transition-delay: 0.1s;
  transition-delay: 0.1s;
}

.c-circle-nav__item:nth-child(5) {
  -webkit-transition-delay: 0s;
  transition-delay: 0s;
}
/**
* We're using the .is-active class, which is added to the nav via JavaScript.
* Once the nav is active, the items inherit the properties below. We will
* manually write out the transform properties for first and last items, as we
* already know their position. For all items in between though, we'll use some
* polar-to-cartesian math and some Sass functions to get the positioning.
*/

.c-circle-nav.is-active .c-circle-nav__item {
  -webkit-transition-timing-function: cubic-bezier(0.35, 0.03, 0.47, 1.59);
  transition-timing-function: cubic-bezier(0.35, 0.03, 0.47, 1.59);
}

.c-circle-nav.is-active .c-circle-nav__item:nth-child(1) {
  -webkit-transition-delay: 0s;
  transition-delay: 0s;
  -webkit-transform: translate(145px, 0);
  -ms-transform: translate(145px, 0);
  transform: translate(145px, 0);
}

@media (min-width: 480px) and (min-height: 480px) {
  .c-circle-nav.is-active .c-circle-nav__item:nth-child(1) {
    -webkit-transform: translate(288px, 0);
    -ms-transform: translate(288px, 0);
    transform: translate(288px, 0);
  }
}

.c-circle-nav.is-active .c-circle-nav__item:nth-child(2) {
  -webkit-transition-delay: 0.1s;
  transition-delay: 0.1s;
  -webkit-transform: translate(135px, 48px);
  -ms-transform: translate(135px, 48px);
  transform: translate(135px, 48px);
}

@media (min-width: 480px) and (min-height: 480px) {
  .c-circle-nav.is-active .c-circle-nav__item:nth-child(2) {
    -webkit-transform: translate(267px, 111px);
    -ms-transform: translate(267px, 111px);
    transform: translate(267px, 111px);
  }
}

.c-circle-nav.is-active .c-circle-nav__item:nth-child(3) {
  -webkit-transition-delay: 0.2s;
  transition-delay: 0.2s;
  -webkit-transform: translate(115px, 95px);
  -ms-transform: translate(115px, 95px);
  transform: translate(115px, 95px);
}

@media (min-width: 480px) and (min-height: 480px) {
  .c-circle-nav.is-active .c-circle-nav__item:nth-child(3) {
    -webkit-transform: translate(204px, 204px);
    -ms-transform: translate(204px, 204px);
    transform: translate(204px, 204px);
  }
}

.c-circle-nav.is-active .c-circle-nav__item:nth-child(4) {
  -webkit-transition-delay: 0.3s;
  transition-delay: 0.3s;
  -webkit-transform: translate(92px, 143px);
  -ms-transform: translate(92px, 143px);
  transform: translate(92px, 143px);
}

@media (min-width: 480px) and (min-height: 480px) {
  .c-circle-nav.is-active .c-circle-nav__item:nth-child(4) {
    -webkit-transform: translate(111px, 267px);
    -ms-transform: translate(111px, 267px);
    transform: translate(111px, 267px);
  }
}

.c-circle-nav.is-active .c-circle-nav__item:nth-child(5) {
  -webkit-transition-delay: 1s;
  transition-delay: 1s;
  -webkit-transform: translate(0, 186px);
  -ms-transform: translate(0, 186px);
  transform: translate(0, 186px);
}

@media (min-width: 480px) and (min-height: 480px) {
  .c-circle-nav.is-active .c-circle-nav__item:nth-child(5) {
    -webkit-transform: translate(0, 288px);
    -ms-transform: translate(0, 288px);
    transform: translate(0, 288px);
  }
}
/**
* Apart from the transform properties, we'll also make sure the items get
* the correct opacity.
*/

.c-circle-nav.is-active .c-circle-nav__item {
  opacity: 1;
}
/**
* Let's style the links now. This is just boilerplate stuff, and of course,
* you'll probably want to change up the icons to match your needs. In any case,
* we'll do it here for the sake of completion.
*/

.c-circle-nav__link {
  display: block;
  width: 100%;
  height: 100%;
  border-radius: 24px;
  box-shadow: inset 0 0 0 2px #fff;
}
.c-circle-nav__link img {
  display: block;
  max-width: 100%;
  height: auto;
}

.c-circle-nav__link:hover {
  box-shadow: inset 0 0 0 2px dodgerblue;
}

.c-mask {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 900;
  visibility: hidden;
  opacity: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.8);
  -webkit-transition: opacity 0.3s, visibility 0.3s;
  transition: opacity 0.3s, visibility 0.3s;
}

.c-mask.is-active {
  opacity: 1;
  visibility: visible;
}

</style>
