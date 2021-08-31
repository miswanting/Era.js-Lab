<template lang="pug">
.block-grid
  slot
</template>

<style lang="stylus" scoped>
.block-grid
  display grid
  grid-template-columns v-bind('getColumnString()')
  text-align vbind('prop.align')
</style>

<script lang="ts" setup>
import { defineComponent, defineProps } from "vue";
const prop =
  defineProps<{
    columns: number;
    align: string;
  }>();

function getColumnString() {
  let s = "";
  for (let i = 0; i < prop.columns; i++) {
    s += "1fr ";
  }
  return s;
}
</script>
