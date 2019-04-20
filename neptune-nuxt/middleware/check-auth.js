import {
  getFromCookie,
  getFromLocalStorage,
  getDecodedJWT,
  getAppleMusicToken
} from "~/utils/auth";
import Cookie from "js-cookie";

export default function({ store, req }) {
  if (process.server) {
    if (!req) return;
    // server side needs to extract from cookies
    let apple_token = Cookie.get("apple_token");
    if (!apple_token) {
      // server side
      const apple_token = getAppleMusicToken();
      console.log("SETTING APPLE TOKEN?");
      console.log(apple_token);
      store.commit("SET_MUSIC_TOKEN", apple_token);
      Cookie.set("apple_token", apple_token); // saving token in cookie for server rendering    }
    }
  } else {
    // client side extracts from local storage
    const auth_token = window.localStorage.api_token;
    if (!auth_token) {
      console.log("SETTING USER TO NULL");
      store.commit("SET_USER", null);
    } else {
      if (!store.state.user) {
        console.log("NO USER IN STORE");
        console.log(auth_token);
        store.commit("SET_USER", auth_token);
      }
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
