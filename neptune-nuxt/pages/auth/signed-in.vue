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
import { store } from "~/plugins/localStorage";

export default {
  mounted() {
    const { access_token, id_token, secret } = extractInfoFromHash();

    if (!checkSecret(secret)) {
      // Something went wrong with auth!
      store.commit("set_secret", secret);
    }

    console.log(store);
    this.$cookies.set("api-token", access_token, {
      path: "/",
      maxAge: 60 * 60 * 24 * 7
    });
    store.commit("set_api_token", access_token);

    // redirect to home
    this.$router.replace("/");
  }
};
</script>
