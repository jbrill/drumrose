import {
  getFromCookie,
  getFromLocalStorage,
  getDecodedJWT,
  getAppleMusicToken
} from "~/utils/auth";
import auth0 from "auth0-js";
import config from "~/config.json";
import { getBaseUrl } from "~/utils/lock";
import { store } from "~/plugins/localStorage";

export default function({ app, req }) {
  if (process.server) {
    const api_token = store.state.api_token;
    if (!api_token) {
      const api_token = app.$cookies.get("api-token");
      store.commit("set_api_token", api_token);
    }

    // server side needs to extract from cookies
    let apple_token = store.state.apple_token;
    if (!apple_token) {
      const apple_token = getAppleMusicToken();
      app.$cookies.set("apple-token", apple_token, {
        path: "/",
        maxAge: 60 * 60 * 24 * 7
      });
      store.commit("set_apple_token", apple_token);
    }
  } else {
    console.log(store.state);
    // client side needs to extract from cookies
    let apple_token = store.state.apple_token;
    if (!apple_token) {
      const apple_token = app.$cookies.get("apple-token");
      store.commit("set_apple_token", apple_token);
    }

    // client side needs to extract from cookies
    let api_token = store.state.api_token;
    if (!api_token) {
      console.log("NO API TOKEN");
      const api_token = app.$cookies.get("api-token");
      store.commit("set_api_token", api_token);

      // app.$cookies.set("api-token", api_token, {
      //   path: "/",
      //   maxAge: 60 * 60 * 24 * 7
      // });
      // store.commit("set_api_token", api_token);
    }
  }
}

// TO USE LATER
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
