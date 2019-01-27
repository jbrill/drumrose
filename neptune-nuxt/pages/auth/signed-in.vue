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
  components: {
    Loading
  },
  mounted() {
    const { token, secret } = extractInfoFromHash();
    console.log(token);
    // if (!checkSecret(secret) || !auth0_token) {
    //   // Something went wrong with auth!
    //   console.log("1");
    //   console.error("Something happened with the Sign In request");
    // }
    console.log("auth0_token");
    console.log(this.$store);
    this.$store.commit("SET_API_TOKEN", token);
    // redirect to home
    this.$router.replace("/");
  }
};
</script>
