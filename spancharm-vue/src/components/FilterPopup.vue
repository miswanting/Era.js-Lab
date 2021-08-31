<template lang="pug">
span.popup-filter(:class="{ enabled: props.enabled }")
  popup {{ props.value }}
  slot
</template>

<style lang="stylus" scoped>
.popup-filter
  display inline-block
  position relative

  popup
    display none
    position absolute
    left 50%
    bottom 100%
    backdrop-filter brightness(.9) blur(3px)
    text-align center
    transform translateX(-50%)
    padding .2rem
    border-radius .2rem
    width max-content

  &.enabled:hover > popup
    display block
</style>

<script lang="ts" setup>
import { defineComponent } from "vue";
const props = defineProps(["enabled", "value"]);
</script>
