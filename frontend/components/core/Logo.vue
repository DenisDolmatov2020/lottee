<template>
  <button
    class="logo-button"
    @click="$router.push('/')"
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
</template>

<script>
export default {
  name: 'Menu'
}
</script>

<style lang="scss" scoped>
.logo-button {
  width: 160px;
  height: 73px;
  z-index: 7;
  position: fixed;
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
</style>
