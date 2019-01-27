<template>
  <div class="sign--out__contain">
    <b-btn class="neptune_btn_strong">Sign Out</b-btn>
  </div>
</template>

<script>
import { webAuthFactory, getBaseUrl } from "~/utils/lock";
import auth0 from "auth0-js";
import config from "~/config.json";

export default {
  middleware: "anonymous",
  mounted() {
    var _this = this;
    var webAuth = new auth0.WebAuth({
      domain: config.AUTH0_CLIENT_DOMAIN,
      clientID: config.AUTH0_CLIENT_ID,
      responseType: "token id_token",
      redirectUri: `${getBaseUrl()}/auth/signed-in`,
      audience: config.API_AUDIENCE
    });
    webAuth.checkSession(
      {
        audience: config.API_AUDIENCE,
        scope: "read:posts"
      },
      function(err, authResult) {
        if (authResult) {
          console.log(authResult);
          const accessToken = authResult.accessToken;
          _this.$store.commit("SET_API_TOKEN", accessToken);
          // redirect to home
          _this.$router.replace("/");
        } else if (err) {
          // err if automatic parseHash fails
          console.error(err.error_description);
          webAuth.login();
        }
      }
    );
  },
  methods: {
    onSubmitForm: function(e) {
      event.preventDefault();
      console.log(e);
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
.sign--in__contain {
}
</style>
