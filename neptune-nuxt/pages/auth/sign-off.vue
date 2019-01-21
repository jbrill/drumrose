<template>
  <loading />
</template>

<script>
import Loading from "~/components/Loading.vue";

export default {
  components: {
    Loading
  },
  mounted() {
    const unsetToken = require("~/utils/auth").unsetToken;
    const logout = require("~/utils/lock").logout;

    unsetToken();
    logout();
  }
};
</script>
