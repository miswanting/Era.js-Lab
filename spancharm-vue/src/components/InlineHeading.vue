<template lang="pug">
h1.inline-heading(v-if="$props.level === 1")
  slot Empty Heading 1
h2.inline-heading(v-else-if="$props.level === 2")
  slot Empty Heading 2
h3.inline-heading(v-else-if="$props.level === 3")
  slot Empty Heading 3
h4.inline-heading(v-else-if="$props.level === 4")
  slot Empty Heading 4
h5.inline-heading(v-else-if="$props.level === 5")
  slot Empty Heading 5
h6.inline-heading(v-else)
  slot Empty Heading 6
</template>

<style lang="stylus" scoped>
.inline-heading
  display inline-block
</style>

<script lang="ts" setup>
import { defineComponent, h } from "vue";
const prop =
  defineProps<{
    level: number;
  }>();
</script>
