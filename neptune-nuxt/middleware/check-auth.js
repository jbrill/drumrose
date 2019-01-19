import {
  getUserFromCookie,
  getUserFromLocalStorage,
  getAppleMusicToken
} from "~/utils/auth";

export default function({ store, req }) {
  /* If server side
	If the cookie is expired, set user to null
  If client side
	If the user local storage is expired, set user to null
  If nuxt generate, pass this middleware
  */
  let loggedUser;
  let musicToken;
  if (process.server) {
    if (!req) return;
    musicToken = getAppleMusicToken();
    loggedUser = getUserFromCookie(req);
    store.commit("SET_MUSIC_TOKEN", musicToken);
  } else {
    loggedUser = getUserFromLocalStorage();
  }
  console.log("USER...");
  console.log(loggedUser);
  store.commit("SET_USER", loggedUser);
}
