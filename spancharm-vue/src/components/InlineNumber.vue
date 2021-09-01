<template lang="pug">
span.inline-number
  span.op(@click="click(0)") #{ '<' }
  span.value(@input="input", contenteditable) {{ props.modelValue }}
  span.op(@click="click(1)") #{ '>' }
</template>

<style lang="stylus" scoped>
.inline-number
  display inline-block
  background-color #0001

  &:hover
    background-color #0002

  &:active
    background-color #0003

  span
    display inline-block

    &:hover
      background-color #0001

  .op
    cursor pointer

  .value
    cursor text
    flex-grow 1
    outline none
</style>

<script lang="ts" setup>
const props = defineProps(["modelValue"]);
const emit = defineEmits(["update:modelValue"]);
function input(e: any) {
  emit("update:modelValue", e.target.innerText);
}
function click(v: number) {
  if (v === 0) {
    emit("update:modelValue", props.modelValue - 1);
  } else {
    emit("update:modelValue", props.modelValue + 1);
  }
}
</script>
