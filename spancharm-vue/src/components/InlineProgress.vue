<template lang="pug">
span.inline-progress
  span.inline-bar
</template>

<style lang="stylus" scoped>
.inline-progress
  display inline-block
  width v-bind('props.width+"px"')
  backdrop-filter brightness(.9)
  text-align left
  background-color v-bind('props.bgColor')

  .inline-bar
    display inline-block
    text-align center
    width v-bind('rate()*100+"%"')
    background-color v-bind('props.color')

    &::before
      content '\200b'
</style>

<script lang="ts" setup>
import { defineProps } from "vue";
// Require: width, value, max, color, bg-color
const props = defineProps([
  "width",
  "modelValue",
  "min",
  "max",
  "low",
  "high",
  "optimum",
  "good-color",
  "color",
  "bad-color",
  "bg-color",
]);
function rate() {
  return props.min
    ? (props.modelValue - props.min) / (props.max - props.min)
    : props.modelValue / props.max;
}
// const rate = props.min
//   ? props.modelValue / (props.max - props.min)
//   : props.modelValue / props.max;
</script>
