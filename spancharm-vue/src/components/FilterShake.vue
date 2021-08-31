<template lang="pug">
span.shake-filter(
  :class="{ shake: props.enabled, 'shake-constant': props.forever }"
)
  slot
</template>

<style lang="stylus" scoped>
.shake-filter
  display inline-block
</style>

<script lang="ts" setup>
import { ref } from "vue";
const props = defineProps(["enabled", "forever"]);
</script>
