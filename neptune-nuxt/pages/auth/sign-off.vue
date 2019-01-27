<template>
  <loading />
</template>

<script>
import { unsetAll } from "~/utils/auth";
import Loading from "~/components/Loading.vue";

export default {
  components: {
    Loading
  },
  mounted() {
    unsetAll();
    // logout();

    // redirect to home
    this.$router.replace("/");
  }
};
</script>
