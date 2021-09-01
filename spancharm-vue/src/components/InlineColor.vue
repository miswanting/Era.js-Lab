<template lang="pug">
span.inline-color(@click="click") {{ props.modelValue }}
  input(type="color", ref="color", @input="input")
</template>

<style lang="stylus" scoped>
.inline-color
  display inline-block
  cursor pointer
  color v-bind('contrast(props.modelValue)')
  background-color v-bind('props.modelValue')

  &:hover
    outline 1px solid #0001

  input
    width 0
    height 0
    padding 0
    border 0
</style>

<script lang="ts" setup>
interface Props {
  modelValue: string;
}
const props = withDefaults(defineProps<Props>(), {
  modelValue: "#000000",
});
const emit = defineEmits(["update:modelValue"]);
function contrast(hex: string) {
  const r = parseInt(hex.slice(1, 3), 16);
  const g = parseInt(hex.slice(3, 5), 16);
  const b = parseInt(hex.slice(5, 7), 16);
  return r + g + b > (256 * 3) / 2 ? "#000000" : "#ffffff";
}
function input(e: any) {
  emit("update:modelValue", e.target.value);
}
</script>
<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  methods: {
    click() {
      (this.$refs as any).color.click();
    },
  },
});
</script>
