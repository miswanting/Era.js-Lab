<template lang="pug">
.block-page
  slot Empty Page
</template>

<style lang="stylus" scoped>
.block-page
  margin .5rem
  padding .5rem
  border 1px solid black
  box-shadow 0px 3px 3px
  border-radius .2rem
</style>

<script lang="ts" setup>
import { defineComponent, defineProps } from "vue";
</script>
