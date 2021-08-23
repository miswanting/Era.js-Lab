<template lang="pug">
.flex-grow.shadow.border.border-gray-300.flex.flex-col(
  class="dark:border-gray-700",
  :class="{ border: !$store.state.electron.is, rounded: !$store.state.electron.is, shadow: !$store.state.electron.is, 'm-2': !$store.state.electron.is }"
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