<template lang="pug">
span.inline-input
  span [
  span.value(@input="input", contenteditable) {{ prop.modelValue }}
  span ]
</template>

<style lang="stylus" scoped>
.inline-input
  display inline-flex
  min-width 3rem
  backdrop-filter brightness(.9)

  &:hover
    backdrop-filter brightness(.8)

  &:active
    backdrop-filter brightness(.6) !important

  &:focus-within
    backdrop-filter brightness(.7)

  .value
    flex-grow 1
    outline none
</style>

<script lang="ts" setup>
import { defineComponent, ref } from "vue";
const prop = defineProps(["modelValue", "type"]);
const emit = defineEmits(["update:modelValue"]);
function input(e: any) {
  emit("update:modelValue", e.target.innerText);
}
</script>
