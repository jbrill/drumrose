import {
  getFromCookie,
  getFromLocalStorage,
  getDecodedJWT
} from "~/utils/auth";

export default function({ store, req }) {
  let auth0Token;
  let appleToken;

  if (process.server) {
    if (!req) return;
    // server side needs to extract from cookies
    appleToken = getFromCookie("apple_token");
    auth0Token = getFromCookie("auth0_token");
  } else {
    // client side extracts from local storage
    appleToken = getFromLocalStorage("apple_token");
    auth0Token = getFromLocalStorage("auth0_token");
  }

  // const loggedUser = getDecodedJWT(auth0Token);

  store.commit("SET_MUSIC_TOKEN", appleToken);
  store.commit("SET_API_TOKEN", auth0Token);
  // store.commit("SET_USER", loggedUser);
}
