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

    // TODO: Delete... we shouldn't rely on store for tokens
    this.$store.commit("SET_USER", id_token);

    // Set localstorage
    window.localStorage.setItem("api_token", access_token);

    // redirect to home
    this.$router.replace("/");
  }
};
</script>
