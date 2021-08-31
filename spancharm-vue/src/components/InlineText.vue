<template lang="pug">
span.inline-text(:style="props.style")
  slot
</template>

<style lang="stylus" scoped>
.inline-text
  display inline-block
</style>

<script lang="ts" setup>
import { defineProps } from "vue";
const props = defineProps(["style"]);
</script>
