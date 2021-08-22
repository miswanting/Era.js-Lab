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
    this.$store.commit(
      "theme/setIfDark",
      window.matchMedia("(prefers-color-scheme: dark)").matches
    );
    document.body.addEventListener("keypress", (e) => {
      if (e.key === "`") {
        this.$store.commit("console/toggle");
      }
    });
    this.$router.push('/AVG')
  },
});
</script>
