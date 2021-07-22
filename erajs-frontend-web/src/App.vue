<template lang="pug">
RouterView
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { RouterView } from "vue-router";
export default defineComponent({
  name: "App",
  components: { RouterView },
  mounted() {
    console.log(this.$store);
    this.$store.state.theme.commit(
      "setIfLight",
      !window.matchMedia("(prefers-color-scheme: dark)").matches
    );
  },
});
</script>
