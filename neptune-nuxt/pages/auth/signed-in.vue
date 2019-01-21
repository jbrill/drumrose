<template>
  <loading />
</template>

<script>
import { setStorage, checkSecret, extractInfoFromHash } from "~/utils/auth";
import Loading from "~/components/Loading.vue";
import { registerUser } from "~/utils/neptuneapi";

export default {
  components: {
    Loading
  },
  mounted() {
    const { auth0_token, secret } = extractInfoFromHash();
    const { apple_token } = getAppleMusicToken();

    if (!checkSecret(secret) || !auth0_token || !apple_token) {
      // Something went wrong with auth!
      console.error("Something happened with the Sign In request");
    }

    // set Auth0 API token
    setStorage(api_token, "auth0_token");
    // set apple music token
    setStorage(apple_token, "apple_token");

    // redirect to home
    this.$router.replace("/");
  }
};
</script>
