<template lang="pug">
.flex-grow.shadow.border.border-gray-300.flex.flex-col(
  class="dark:border-gray-700",
  :class="{ border: !$store.state.electron.is, rounded: !$store.state.electron.is, shadow: !$store.state.electron.is, 'm-2': !$store.state.electron.is }"
)
  header.absolute.top-0.right-0.p-1(
    class="hover:bg-red-200 active:bg-red-300 dark:hover:bg-red-900 dark:active:bg-red-800",
    v-if="$store.state.electron.is",
    @click="close"
  )
    i.fas.fa-times.fa-fw
  main.flex-grow.grid.place-items-center
    .text-gray-400
      i.fas.fa-spinner.fa-pulse
      span Start Backend
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { ipcRenderer } from "electron";
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
export default defineComponent({
  components: { Header, Footer },
  methods: {
    close() {},
  },
});
</script>