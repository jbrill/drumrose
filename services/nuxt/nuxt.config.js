export default {
  /*
   ** Router config
   */
  srcDir: 'src/',
  router: {
  },
  /*
   ** Headers of the page
   */
  head: {
    title: 'DRUMROSE // HOME',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
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
  render: {
    gzip: false
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
    '@nuxtjs/auth',
    'nuxt-svg-loader',
    'cookie-universal-nuxt',
  ],
  axios: {
  },
  plugins: [
    '~/plugins/nuxt-client-init.client.js',
    '~/plugins/ripple.client.js',
    '~/plugins/tooltip.client.js',
    '~/plugins/hotkey.client.js',
    '~/plugins/vuetify.client.js',
    '~/plugins/carousel.client.js',
  ],
  /*
   ** Build configuration
   */
  buildModules: [
    // With options
    ['@nuxtjs/stylelint-module', {
      fix: true,
    }],
    // With options
    ['@nuxtjs/vuetify', { /* module options */ }],
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
  auth: {
    redirect: {
			login: '/',
			logout: '/',
			callback: '/auth/signed-in',
			home: '/'
		},
    strategies: {
			auth0: {
				domain: process.env.AUTH0_DOMAIN,
				client_id: process.env.AUTH0_CLIENT_ID,
				audience: 'https://django-server:8000',
			}
		}
	}
};
