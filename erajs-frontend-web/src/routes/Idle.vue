<template lang="pug">
.flex-grow.rounded.shadow.border.border-gray-300.flex.flex-col(
  class="dark:border-gray-700"
  :class={rounded:!$store.isElectron,shadow:!$store.isElectron,border:!$store.isElectron}
)
  Header
  main.flex-grow.grid.place-items-center
    div.text-gray-400 Start Backend
</template>
<script lang="ts">
import { defineComponent } from "vue";
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
export default defineComponent({
  components: { Header, Footer },
});
</script>