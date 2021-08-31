<template lang="pug">
.block-line
  slot
</template>

<style lang="stylus" scoped>
.block-line
  text-align v-bind('prop.align')
</style>

<script lang="ts" setup>
import { defineComponent } from "vue";
const prop =
  defineProps<{
    align: string;
  }>();
</script>
