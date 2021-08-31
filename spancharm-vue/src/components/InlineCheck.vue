<template lang="pug">
span.inline-check(@click="click", :class="{ active }")
  span(v-if="active") {{ prop.yes }}
  span(v-else) {{ prop.no }}
</template>

<style lang="stylus" scoped>
.inline-check
  display inline-flex
  backdrop-filter brightness(.9)
  cursor pointer

  &:hover
    backdrop-filter brightness(.8)

  &:active
    backdrop-filter brightness(.7)
</style>

<script lang="ts" setup>
import { defineComponent, ref, defineProps } from "vue";
const prop = defineProps(["default", "yes", "no", "disabled"]);
const active = ref(prop.default);
const emit = defineEmits(["update:modelValue"]);

function click(e: any) {
  active.value = !active.value;
  emit("update:modelValue", active.value);
}
</script>
