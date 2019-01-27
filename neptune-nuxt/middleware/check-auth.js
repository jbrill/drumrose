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
