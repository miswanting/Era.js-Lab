<template lang="pug">
header.flex.cursor-pointer.select-none
  .flex
    .p-1(
      class="hover:bg-gray-200 active:bg-gray-300 dark:hover:bg-gray-800 dark:active:bg-gray-700"
    ) {{ $t('File') }}
    .p-1(
      class="hover:bg-gray-200 active:bg-gray-300 dark:hover:bg-gray-800 dark:active:bg-gray-700"
    ) {{ $t('Edit') }}
    .p-1(
      class="hover:bg-gray-200 active:bg-gray-300 dark:hover:bg-gray-800 dark:active:bg-gray-700"
    ) {{ $t('View') }}
    .p-1(
      class="hover:bg-gray-200 active:bg-gray-300 dark:hover:bg-gray-800 dark:active:bg-gray-700"
    ) {{ $t('Tool') }}
    .p-1(
      class="hover:bg-gray-200 active:bg-gray-300 dark:hover:bg-gray-800 dark:active:bg-gray-700"
    ) {{ $t('Window') }}
    .p-1(
      class="hover:bg-gray-200 active:bg-gray-300 dark:hover:bg-gray-800 dark:active:bg-gray-700"
    ) {{ $t('Help') }}
  .flex-grow.p-1.text-center.cursor-move.title {{ $t('Era.js') }}
  .flex
    .p-1(
      class="hover:bg-gray-200 active:bg-gray-300 dark:hover:bg-gray-800 dark:active:bg-gray-700",
      @click="$store.commit('locale/toggle')"
    )
      i.fas.fa-fw.fa-language
    .p-1(
      class="hover:bg-gray-200 active:bg-gray-300 dark:hover:bg-gray-800 dark:active:bg-gray-700",
      @click="$store.commit('theme/toggleTheme')"
    )
      i.fas.fa-fw.fa-moon(v-if="$store.state.theme.dark")
      i.fas.fa-fw.fa-sun(v-else)
    .p-1(
      class="hover:bg-gray-200 active:bg-gray-300 dark:hover:bg-gray-800 dark:active:bg-gray-700"
    )
      i.fas.fa-fw.fa-heart
      i.fas.fa-fw.fa-heart-broken
      i.fas.fa-fw.fa-heartbeat
    .p-1(
      class="hover:bg-gray-200 active:bg-gray-300 dark:hover:bg-gray-800 dark:active:bg-gray-700"
    )
      i.fas.fa-fw.fa-user
      i.fas.fa-fw.fa-user-secret
    .p-1(
      class="hover:bg-gray-200 active:bg-gray-300 dark:hover:bg-gray-800 dark:active:bg-gray-700",
      v-if="$store.state.electron.is"
    )
      i.fas.fa-fw.fa-window-minimize
    .p-1(
      class="hover:bg-gray-200 active:bg-gray-300 dark:hover:bg-gray-800 dark:active:bg-gray-700",
      v-if="$store.state.electron.is"
    )
      i.fas.fa-fw.fa-window-maximize
      i.fas.fa-fw.fa-window-restore
    .p-1(
      class="hover:bg-red-200 active:bg-red-300 dark:hover:bg-red-900 dark:active:bg-red-800",
      v-if="$store.state.electron.is"
    )
      i.fas.fa-fw.fa-window-close
</template>

<style lang="sass" scoped>
.title
  -webkit-app-region: drag
</style>

<script lang="ts">
import { defineComponent } from "vue";
// import { useI18n } from "vue-i18n";
export default defineComponent({
  // setup() {
  //   const {} = useI18n();
  // },
});
</script>
