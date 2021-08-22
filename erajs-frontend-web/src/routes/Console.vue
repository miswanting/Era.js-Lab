<template lang="pug">
.flex-grow.rounded.shadow.border.border-gray-300.flex.flex-col(
  class="dark:border-gray-700"
)
  Header
  main.flex-grow
    .px-1
      i.fas.fa-spinner.fa-pulse
</template>
<script lang="ts">
import { defineComponent } from "vue";
import Header from "../components/Header.vue";
export default defineComponent({
  components: { Header },
});
</script>