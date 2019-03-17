<template>
  <div class="sign--in__contain">
    <b-btn @click="onSubmitForm" class="neptune-button__strong">Sign In</b-btn>
  </div>
</template>

<script>
import { getBaseUrl } from "~/utils/lock";
import auth0 from "auth0-js";
import config from "~/config.json";

export default {
  middleware: "anonymous",
  methods: {
    onSubmitForm: function(e) {
      var webAuth = new auth0.WebAuth({
        domain: config.AUTH0_CLIENT_DOMAIN,
        audience: config.API_AUDIENCE,
        clientID: config.AUTH0_CLIENT_ID,
        responseType: "token id_token",
        redirectUri: `${getBaseUrl()}/auth/signed-in`,
        scope: "openid profile"
      });
      webAuth.authorize();
    }
  },
  data() {
    return {
      modalShow: false
    };
  }
};
</script>
<style scoped>
.neptune-button__strong {
  font-size: 0.8rem;
}
</style>
