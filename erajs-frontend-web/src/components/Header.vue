<template lang="pug">
header.flex.cursor-pointer
  .flex
    .p-1(class="hover:bg-gray-300 active:bg-gray-400") {{ $t('File') }}
    .p-1(class="hover:bg-gray-300 active:bg-gray-400") Edit
    .p-1(class="hover:bg-gray-300 active:bg-gray-400") View
    .p-1(class="hover:bg-gray-300 active:bg-gray-400") Tool
    .p-1(class="hover:bg-gray-300 active:bg-gray-400") Window
    .p-1(class="hover:bg-gray-300 active:bg-gray-400") Help
  .flex-grow.p-1.text-center.cursor-move Era.js
  .flex
    .p-1(class="hover:bg-gray-300 active:bg-gray-400")
      i.fas.fa-fw.fa-language
    .p-1(
      class="hover:bg-gray-300 active:bg-gray-400",
      @click="$store.state.theme.commit('toggleTheme')"
    )
      i.fas.fa-fw.fa-sun(v-if="$store.state.theme.light")
      i.fas.fa-fw.fa-moon(v-else)
    .p-1(class="hover:bg-gray-300 active:bg-gray-400")
      i.fas.fa-fw.fa-heart
      i.fas.fa-fw.fa-heart-broken
      i.fas.fa-fw.fa-heartbeat
    .p-1(class="hover:bg-gray-300 active:bg-gray-400")
      i.fas.fa-fw.fa-user
      i.fas.fa-fw.fa-user-secret
    .p-1(class="hover:bg-gray-300 active:bg-gray-400")
      i.fas.fa-fw.fa-window-minimize
    .p-1(class="hover:bg-gray-300 active:bg-gray-400")
      i.fas.fa-fw.fa-window-maximize
      i.fas.fa-fw.fa-window-restore
    .p-1(class="hover:bg-gray-300 active:bg-gray-400")
      i.fas.fa-fw.fa-window-close
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useI18n } from "vue-i18n";
export default defineComponent({
  setup() {
    const {} = useI18n();
  },
});
</script>
