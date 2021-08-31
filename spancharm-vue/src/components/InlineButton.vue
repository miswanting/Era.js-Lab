<template lang="pug">
span.inline-button(@click="click", :style="props.style")
  slot
</template>

<style lang="stylus" scoped>
.inline-button
  display inline-block
  cursor pointer
  backdrop-filter brightness(.9)

  &:hover
    backdrop-filter brightness(.8)

  &:active
    backdrop-filter brightness(.7)
</style>

<script lang="ts" setup>
import { defineProps } from "vue";
const props = defineProps(["disabled", "style"]);
function click() {}
</script>
