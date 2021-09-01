<template lang="pug">
span.inline-input.text(v-if="type === 'text'")
  span [
  span.value(@input="input", contenteditable) {{ props.modelValue }}
  span ]
span.inline-input.color(@click="clickColor", v-if="type === 'color'")
  span.value {{ props.modelValue }}
  input(type="color", ref="color", @input="input")
span.inline-input.number(v-if="type === 'number'")
  span [
  span.value(@input="input", contenteditable) {{ props.modelValue }}
  span ]
InlineRank(v-if="type === 'rank'", v-model="ttt")
</template>

<style lang="stylus" scoped>
.inline-input
  display inline-flex

.color
  cursor pointer

  .value
    color v-bind('contrast(props.modelValue)')
    background-color v-bind('props.modelValue')

  input
    width 0
    height 0
    padding 0
    border 0
</style>

<script lang="ts" setup>
import { ref } from "vue";
import InlineRank from "./InlineRank.vue";
const props = defineProps(["type", "modelValue", "default"]);
const ttt=ref(3)
let type: string;
if (props.type === undefined) type = "text";
else type = props.type;
let value = ref("");
if (props.default === undefined) {
  if (type === "color") value.value = "#000000";
} else value = ref(props.default);
const emits = defineEmits(["update:modelValue"]);
function contrast(hex: string) {
  const raw = hex.slice(1, 7);
  const r = parseInt(raw.slice(0, 2), 16);
  const g = parseInt(raw.slice(2, 4), 16);
  const b = parseInt(raw.slice(4, 6), 16);
  return r + g + b > (256 * 3) / 2 ? "#000000" : "#ffffff";
}
</script>
<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  methods: {
    input(e: any) {
      if (this.type === "text") {
        this.$emit("update:modelValue", e.target.innerText);
      } else if (this.type === "color") {
        this.value = (this.$refs as any).color.value;
        this.$emit("update:modelValue", this.value);
      }
    },
    clickColor() {
      (this.$refs as any).color.click();
    },
  },
});
</script>
