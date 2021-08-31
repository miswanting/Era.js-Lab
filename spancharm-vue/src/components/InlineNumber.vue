<template lang="pug">
span.inline-number
  span.op(@click="click(0)") #{ '<' }
  span.value(@input="input", contenteditable) {{ value }}
  span.op(@click="click(1)") #{ '>' }
</template>

<style lang="stylus" scoped>
.inline-number
  display inline-flex
  backdrop-filter brightness(.9)

  .op
    cursor pointer

    &:hover
      backdrop-filter brightness(.8)

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
const props = defineProps(["modelValue"]);
const value = ref(props.modelValue);
const emit = defineEmits(["update:modelValue"]);
function input(e: any) {
  emit("update:modelValue", e.target.innerText);
}
function click(v: number) {
  if (v === 0) {
    value.value -= 1;
  } else {
    value.value += 1;
  }
  emit("update:modelValue", value.value);
}
</script>
