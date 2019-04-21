const webpack = require("webpack");
module.exports = {
  /*
   ** Router config
   */
  router: {
    middleware: "check-auth"
  },
  /*
   ** Headers of the page
   */
  head: {
    title: "Neptune - Affect Culture",
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      {
        hid: "description",
        name: "description",
        content: "Neptune Web Platform"
      }
    ],
    link: [
      {
        rel: "stylesheet",
        href: "https://fonts.googleapis.com/icon?family=Material+Icons"
      },
      { rel: "icon", type: "image/x-icon", href: "favicon.ico" },
      {
        rel: "apple-touch-icon",
        sizes: "180x180",
        href: "apple-touch-icon.png"
      },
      {
        rel: "icon",
        type: "image/png",
        sizes: "32x32",
        href: "favicon-32x32.png"
      },
      {
        rel: "icon",
        type: "image/png",
        sizes: "16x16",
        href: "favicon-16x16.png"
      },
      { rel: "manifest", href: "site.webmanifest" },
      { rel: "mask-icon", color: "#5bbad5", href: "safari-pinned-tab.svg" },
      { rel: "theme-color", content: "#ffffff" }
    ],
    script: [
      { src: "https://js-cdn.music.apple.com/musickit/v1/musickit.js" },
      { src: "https://cdn.auth0.com/js/auth0/9.5.1/auth0.min.js" }
    ]
  },
  /*
   ** Global CSS
   */
  css: ["normalize.css", "~assets/main.css"],
  /*
   ** Environement variables
   */
  env: {
    AUTH0_CLIENT_ID: "",
    AUTH0_CLIENT_DOMAIN: "",
    APPLE_MUSIC_KEY_ID: "",
    APPLE_MUSIC_TEAM_ID: ""
  },
  modules: [
    "@nuxtjs/axios",
    "bootstrap-vue/nuxt",
    "nuxt-svg-loader",
    "cookie-universal-nuxt"
  ],
  plugins: [{ src: "~/plugins/localStorage.js" }],
  axios: {
    proxyHeaders: false
  },
  /*loading: '~/components/Loading.vue',*/
  /*
   ** Build configuration
   */
  build: {
    /*
     ** You can extend webpack config here
     */
    extend(config, { isDev }) {
      config.node = { fs: "empty" };
      // Run ESLint on save
      if (isDev && process.client) {
        config.module.rules.push({
          enforce: "pre",
          test: /\.(js|vue)$/,
          loader: "eslint-loader",
          exclude: /(node_modules)/
        });
      }
    }
  }
};
