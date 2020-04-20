export default {
  /*
   ** Router config
   */
  srcDir: 'src/',
  router: {},
  /*
   ** Headers of the page
   */
  head: {
    title: 'DRUMROSE // affect culture',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'apple-music-developer-token', name: 'apple-music-developer-token', content: process.env.APPLE_MUSIC_KEY_ID },
      { hid: 'apple-music-app-name', name: 'apple-music-app-name', content: 'Drumrose' },
      { hid: 'apple-music-app-build', name: 'apple-music-app-build', content: 'My custom description' }
    ],
    link: [
      {
        rel: 'stylesheet',
        href: 'https://fonts.googleapis.com/icon?family=Material+Icons',
      },
      { rel: 'icon', type: 'image/x-icon', href: 'favicon.ico' },
      {
        rel: 'apple-touch-icon',
        sizes: '180x180',
        href: 'apple-touch-icon.png',
      },
      {
        rel: 'icon',
        type: 'image/png',
        sizes: '32x32',
        href: 'favicon-32x32.png',
      },
      {
        rel: 'icon',
        type: 'image/png',
        sizes: '16x16',
        href: 'favicon-16x16.png',
      },
      { rel: 'manifest', href: 'site.webmanifest' },
      { rel: 'mask-icon', color: '#5bbad5', href: 'safari-pinned-tab.svg' },
      { rel: 'theme-color', content: '#ffffff' },
    ],
    script: [{ src: 'https://js-cdn.music.apple.com/musickit/v1/musickit.js' }],
  },
  /*
   ** Global CSS
   */
  css: ['normalize.css', '~assets/main.css'],
  /*
   ** Environement variables
   */
  modules: [
    '@nuxtjs/axios',
    'bootstrap-vue/nuxt',
    'nuxt-svg-loader',
    'cookie-universal-nuxt',
  ],
  axios: {
    proxyHeaders: false,
  },
  plugins: [
    { src: '~utils/post_util.js' },
  ],
  /*
   ** Build configuration
   */
  buildModules: [
    // Simple usage
    '@nuxtjs/stylelint-module',

    // With options
    ['@nuxtjs/stylelint-module', {
      fix: true,
    }],
  ],
  build: {
    /*
     ** You can extend webpack config here
     */
    extend (config, { isDev }) {
      config.node = { fs: 'empty' };
      // Run ESLint on save
      if (isDev && process.client) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/,
        });
      }
    },
  },
};
