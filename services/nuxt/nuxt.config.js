export default {
  /*
   ** Router config
   */
  srcDir: 'src/',
  /*
   ** Headers of the page
   */
  head: {
    title: 'DRUMROSE | Affect Culture',
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
    gzip: false,
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
    '@nuxtjs/sentry',
    '@nuxtjs/toast',
    'nuxt-svg-loader',
    'nuxt-healthcheck',
  ],
  plugins: [
    '~/plugins/nuxt-client-init.client.js',
    '~/plugins/carousel.client.js',
    '~/plugins/axios',
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
    analyze:true,
    extractCSS: true,
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
			home: '/',
		},
    strategies: {
			auth0: {
				domain: process.env.AUTH0_DOMAIN,
				client_id: process.env.AUTH0_CLIENT_ID,
				audience: 'https://django-server:8000',
			},
		},
	},
  sentry: {
    dsn: process.env.SENTRY_DSN, // Enter your project's DSN here
    config: {
      environment: "dev",
    },
    webpackConfig: {
      include: ".",
      release: "v1.0.0",
      ignoreFile: ".gitignore",
    },
  },
  vuetify: {
		theme: {
			dark: true,
			themes: {
				dark: {
					primary: '#9c0235',
					secondary: '#772ce6',
					accent: '#f3f367',
				},
      },
      rtl: true,
		},
  },
  toast: {
    position: 'top-right',
    register: [ // Register custom toasts
      {
        name: 'my-error',
        message: 'Oops...Something went wrong',
        options: {
          type: 'error',
        },
      },
      {
        name: 'apple_login',
        message: 'Sign into Apple Music for full track access',
        options: {
          type: 'info',
        },
      },
    ],
  },
};
