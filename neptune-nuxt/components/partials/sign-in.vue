<template>
  <div class="sign--in__contain">
    <b-btn class="neptune-button__strong" v-b-modal.modalPopover>Sign In</b-btn>
    <b-modal id="modalPopover" title="Join the fun" hide-footer>
      <form method="POST" @submit="onSubmitForm">
        <div class="form-group">
          <label for="username"> Email: </label>
          <input
            ref="username"
            type="text"
            name="username"
            class="form-control"
          />
        </div>

        <div class="form-group">
          <label for="password"> Password: </label>
          <input
            ref="password"
            type="password"
            name="password"
            class="form-control"
          />
        </div>

        <div class="form-group" v-if="!submitted">
          <b-button
            @click="show = false"
            type="submit"
            class="btn btn-default"
            v-bind:disabled="errors"
            variant="primary"
          >
            Sign In
          </b-button>
        </div>
        <div class="alert alert-success" v-if="submitted">Thanks!</div>
      </form>
    </b-modal>
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
    // webAuth.checkSession(
    //   {
    //     audience: config.API_AUDIENCE,
    //     scope: "read:posts"
    //   },
    //   function(err, authResult) {
    //     if (authResult) {
    //       console.log(authResult);
    //       const accessToken = authResult.accessToken;
    //       _this.$store.commit("SET_API_TOKEN", accessToken);
    //       // redirect to home
    //       _this.$router.replace("/");
    //     } else if (err) {
    //       // err if automatic parseHash fails
    //       console.error(err.error_description);
    //       webAuth.login();
    //     }
    //   }
    // );
  },
  methods: {
    onSubmitForm: function(e) {
      event.preventDefault();
      console.log(this.$refs.username.value);
      var _this = this;
      var webAuth = new auth0.WebAuth({
        domain: config.AUTH0_CLIENT_DOMAIN,
        clientID: config.AUTH0_CLIENT_ID,
        responseType: "token id_token",
        redirectUri: `${getBaseUrl()}/auth/signed-in`,
        audience: config.API_AUDIENCE
      });
      // webAuth.login();
      // webAuth.checkSession(
      //   {
      //     audience: config.API_AUDIENCE,
      //     scope: "read:posts"
      //   },
      //   function(err, authResult) {
      //     if (authResult) {
      //       console.log(authResult);
      //       const accessToken = authResult.accessToken;
      //       _this.$store.commit("SET_API_TOKEN", accessToken);
      //       // redirect to home
      //       _this.$router.replace("/");
      //     } else if (err) {
      //       // err if automatic parseHash fails
      //       console.error(err.error_description);
      //       webAuth.login();
      //     }
      //   }
      // );
      const options = {
        username: this.$refs.username,
        password: this.$refs.password
      };
      webAuth.login(options, `${getBaseUrl()}/auth/signed-in`);

      // webAuth.authorize();
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
