import {
  getFromCookie,
  getFromLocalStorage,
  getDecodedJWT,
  getAppleMusicToken
} from "~/utils/auth";
import Cookie from "js-cookie";

export default function({ store, req }) {
  console.log("HERE.........");
  if (process.server) {
    if (!req) return;
    // server side needs to extract from cookies
    let apple_token = Cookie.get("apple_token");
    // auth0Token = Cookie.get("auth0_token");
    if (!apple_token) {
      // server side
      apple_token = getAppleMusicToken();
      store.commit("SET_MUSIC_TOKEN", apple_token);
      Cookie.set("apple_token", apple_token); // saving token in cookie for server rendering    }
    }
  } else {
    // client side extracts from local storage
    // appleToken = getFromLocalStorage("apple_token");
    const auth0Token = store.state.api_token;
    if (!auth0Token) {
      console.log("NO AUTH0 TOKEN... should logout");
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
