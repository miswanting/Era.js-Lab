<template lang="pug">
span.inline-input.rank(v-if="props.type === 'rank'")
  span.item(v-for="i in props.max - props.min", @click="click(i)") {{ props.modelValue < i ? props.falseText : props.trueText }}
</template>

<style lang="stylus" scoped>
.inline-input
  display inline-block

.rank
  cursor pointer
  background-color #0001

  &:hover
    background-color #0002

  &:active
    background-color #0003

  .item
    &:hover
      background-color #0001
</style>

<script lang="ts" setup>
interface Props {
  modelValue?: number;
  type?: string;
  min?: number;
  max?: number;
  trueText?: string;
  falseText?: string;
}
const props = withDefaults(defineProps<Props>(), {
  modelValue: 0,
  type: "rank",
  min: 0,
  max: 5,
  trueText: "★",
  falseText: "☆",
});
const emit = defineEmits(["update:modelValue"]);
function click(v: number) {
  if (v === props.modelValue) v = 0;
  emit("update:modelValue", v);
}
</script>
