<template lang="pug">
.viewport
  slot Empty Viewport
</template>

<style lang="stylus" scoped>
.viewport
  position absolute
  top 0
  bottom 0
  left 0
  right 0
  overflow-y auto
  overflow-x hidden
  padding .5rem

  &::-webkit-scrollbar
    width .5rem
    padding .5rem
    margin .5rem

  &::-webkit-scrollbar-track
    border-radius .5rem
    border .5px solid

  &::-webkit-scrollbar-thumb
    border-radius .5rem
    border .5px solid
</style>

<script lang="ts" setup>
import { defineComponent, defineProps } from "vue";
</script>
