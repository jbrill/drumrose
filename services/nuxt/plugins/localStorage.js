import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";
import Cookies from "js-cookie";

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    api_token: null,
    secret: null,
    apple_token: null,
    user_handle: null
  },
  plugins: [
    createPersistedState({
      storage: {
        getItem: key => Cookies.get(key),
        setItem(key, value) {
          Cookies.set(key, value, { expires: 3, secure: true });
        },
        removeItem: key => Cookies.remove(key)
      }
    })
  ],
  mutations: {
    set_api_token: (state, api_token) => (state.api_token = api_token),
    set_secret: (state, secret) => (state.secret = secret),
    set_apple_token: (state, apple_token) => (state.apple_token = apple_token),
    set_user_handle: (state, user_handle) => (state.user_handle = user_handle)
  },
  getters: {
    isAuthenticated: state => !!state.api_token,
    getAppleToken: state => !!state.apple_token
  }
});
