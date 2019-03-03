<template>
  <loading />
</template>

<script>
import {
  setStorage,
  checkSecret,
  extractInfoFromHash,
  getAppleMusicToken
} from "~/utils/auth";
import Cookie from "js-cookie";
import Loading from "~/components/Loading.vue";
import { registerUser } from "~/utils/neptuneapi";

export default {
  mounted() {
    const { access_token, id_token, secret } = extractInfoFromHash();
    console.log(access_token);
    if (!checkSecret(secret) || !access_token) {
      // Something went wrong with auth!
      console.error("Something happened with the Sign In request");
    }
    console.log("auth0_token");
    console.log(access_token);
    // console.log(this.$store);
    this.$store.commit("SET_API_TOKEN", access_token);
    // redirect to home
    this.$router.replace("/");
  }
};
</script>
