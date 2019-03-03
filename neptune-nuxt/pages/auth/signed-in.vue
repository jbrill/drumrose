<template> </template>

<script>
import {
  setStorage,
  checkSecret,
  extractInfoFromHash,
  getAppleMusicToken
} from "~/utils/auth";
import Cookie from "js-cookie";
import Loading from "~/components/Loading.vue";

export default {
  mounted() {
    const { access_token, id_token, secret } = extractInfoFromHash();

    if (!checkSecret(secret)) {
      // Something went wrong with auth!
      window.localStorage.setItem("secret", secret);
    }

    this.$store.commit("SET_API_TOKEN", access_token);
    this.$store.commit("SET_USER", id_token);
    // redirect to home
    this.$router.replace("/");
  }
};
</script>
