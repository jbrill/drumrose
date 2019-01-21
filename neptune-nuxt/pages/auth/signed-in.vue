<template>
  <loading />
</template>

<script>
import {
  setToken,
  checkSecret,
  extractInfoFromHash,
  getAppleMusicToken
} from "~/utils/auth";
import Loading from "~/components/Loading.vue";
import { registerUser } from "~/utils/neptuneapi";

export default {
  components: {
    Loading
  },
  mounted() {
    const { token, secret } = extractInfoFromHash();
    if (!checkSecret(secret) || !token) {
      console.error("Something happened with the Sign In request");
    }
    setToken(token);
    console.log("TOKEN:\n");
    console.log(token);
    this.$router.replace("/");
  }
};
</script>
