<template lang="pug">
.flex-grow.rounded.border-gray-300.flex.flex-col(
  class="dark:border-gray-700",
  :class="{ border: !$store.state.electron.is, shadow: !$store.state.electron.is, 'm-2': !$store.state.electron.is }"
)
  Header
  main.flex-grow.grid.items-end
    canvas.absolute
    .z-1.m-2
      .border.border-gray-300.inline-block.px-1.text-center.rounded-t(
        class="dark:border-gray-700"
      ) 123
      .border.border-gray-300.p-1.rounded-b(class="dark:border-gray-700") 123
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
export default defineComponent({
  components: { Header, Footer },
  mounted() {
    const main = document.querySelector("main");
    const canvas = document.querySelector("canvas");
    if (main && canvas) {
      const ctx = canvas.getContext("2d");
      canvas.width = main.clientWidth;
      canvas.height = main.clientHeight;
      window.addEventListener("resize", () => {
        if (ctx) {
          ctx.lineWidth = 10;
          ctx.beginPath();
          ctx.moveTo(0, 0);
          ctx.lineTo(canvas.width, canvas.height);
          ctx.closePath();
          ctx.stroke();
        }
        canvas.width = main.clientWidth;
        canvas.height = main.clientHeight;
      });
    }
  },
});
</script>