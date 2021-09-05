<template>
  <div>
    <v-app-bar 
      fixed
      style="padding: 4px"
      app
    >
      <v-toolbar-title>
        <nuxt-link class="toolbar-title" to="/">
          <img width="24" height="24" src="~../assets/img/iteration1.png">
          <span class="drumrose-title">DRUMROSE</span>
        </nuxt-link>
      </v-toolbar-title>
      <v-spacer />
      <v-btn
        nuxt
        to="/"
        text
        plain
        large
        class="font-weight-bold"
      >
        Home
      </v-btn>
      <v-btn
        nuxt
        to="/music"
        text
        plain
        large
        class="font-weight-bold"
      >
        Music
      </v-btn>
      <v-btn
        nuxt
        to="/playlists"
        text
        plain
        large
        class="font-weight-bold"
      >
        Playlists
      </v-btn>
      <v-btn
        nuxt
        to="/people"
        text
        plain
        large
        class="font-weight-bold"
      >
        People
      </v-btn>
      <v-spacer />
      <SearchBar style="margin: 5px" />
      <v-btn
        v-if="!auth.loggedIn"
        class="font-weight-bold"
        style="margin: 5px"
        raised
        @click="login"
      >
        Log In
      </v-btn>
      <v-btn
        v-if="!auth.loggedIn"
        class="font-weight-bold"
        style="margin: 5px"
        color="var(--primary-red)"
        raised
        @click="login"
      >
        Sign Up
      </v-btn>
      <v-menu
        open-on-hover
        dark
        offset-y
        transition="slide-y-transition"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            small
            v-bind="attrs"
            v-on="on"
          >
            <v-avatar
              v-if="auth.loggedIn"
              size="26"
              color="var(--primary-purple)"
            >
              <v-icon dark>
                mdi-account-circle
              </v-icon>
            </v-avatar>
            <v-icon>
              mdi-dots-horizontal
            </v-icon>
          </v-btn>
        </template>
        <v-list dense>
          <v-list-item
            v-if="auth.loggedIn"
            nuxt
            :to="'/people/' + getAuthHandle"
          >
            <v-list-item-title>
              Profile
            </v-list-item-title>
          </v-list-item>
          <v-list-item nuxt to="/about">
            <v-list-item-title>
              About us
            </v-list-item-title>
          </v-list-item>
          <v-list-item nuxt to="/settings">
            <v-list-item-title>
              Settings
            </v-list-item-title>
          </v-list-item>
          <v-list-item v-if="auth.loggedIn" href @click="signOut">
            <v-list-item-title>
              Sign Out
            </v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar> 
  </div>
</template>

<script>
import { mapState } from 'vuex';
import SearchBar from '~/components/SearchBar';

export default {
  components: {
    SearchBar,
  },
  data () {
    return {
      drawer: false,
      navObjects: [
        {
          title: 'Home',
          nav: '/',
          icon: 'mdi-home',
          requiresAuth: false,
          requiresAppleAuth: false,
        },
        {
          title: 'Tracks',
          nav: '/tracks',
          icon: 'mdi-waveform',
          requiresAuth: false,
          requiresAppleAuth: false,
        },
        {
          title: 'Albums',
          nav: '/albums',
          icon: 'mdi-record-circle-outline',
          requiresAuth: false,
          requiresAppleAuth: false,
        },
        {
          title: 'Playlists',
          nav: '/playlists',
          icon: 'mdi-playlist-music',
          requiresAuth: false,
          requiresAppleAuth: false,
        },
        {
          title: 'People',
          nav: '/people',
          icon: 'mdi-account',
          requiresAuth: false,
          requiresAppleAuth: false,
        },
        {
          title: 'Settings',
          nav: '/settings',
          icon: 'mdi-cogs',
          requiresAuth: false,
          requiresAppleAuth: false,
        },
      ],
      tags: [
        'About', 'Legal', 'Contact', 'Careers',
      ],
    };
  },
  computed: {
    ...mapState(['auth', 'isAuthorized']),
    currentRouteName () {
      return 'DRUMROSE';
    },
    filteredNavObjects () {
      return this.navObjects.filter(
        navObject => (
          (
            !this.auth.loggedIn && !navObject.requiresAuth
          ) || this.auth.loggedIn
        ) && (
          (
            !this.$store.state.isAuthorized && !navObject.requiresAppleAuth
          ) || this.$store.state.isAuthorized
        )
      );
    },
    getAuthHandle () {
      return this.auth.user['https://django-server:8000/handle'];
    },
  },
  methods: {
    login () {
      this.$auth.loginWith('auth0');
    },
    async signOut () {
      await this.$auth.logout();
      if (process.client) {
        const AUTH0_DOMAIN = 'drumrose.auth0.com';
        const AUTH0_CLIENT_ID = 'nA1RUMeTG88LVxGeEJc9Xu4PhWPHQRTg';
        window.location.href = `https://${AUTH0_DOMAIN}/v2/` +
                               `logout?returnTo=` +
                               `https%3A%2F%2Fteton.drumrose.io` +
                               `&client_id=${AUTH0_CLIENT_ID}`;
      }
    },
  },
};
</script>

<style scoped>
.search-bar__contain {
  margin: 0 auto;
  opacity: 0.9;
  margin-right: 1.2rem;
}
@media screen and (prefers-reduced-motion: reduce) {
  .search-bar__contain:hover, .search-bar__contain:focus {
    color: black;
    opacity: 1;
    transition: none;
  }
}
.search-bar__contain:hover, .search-bar__contain:focus {
  color: black;
  opacity: 1;
  transition: opacity 0.2s ease-out;
}
.activeListItem {
  color: var(--primary-yellow) !important;
}
>>>.needs-apple-auth {
  margin-top: 50px !important;
}
.drumrose-title {
  color: #ccc;
  font-size: 1rem;
  padding-left: 5px;
  font-family: 'Drumrose', monospace !important;
}
.drumrose-title:hover, .drumrose-title:focus {
  color: white;
}
.menu-navigation:hover, .menu-navigation:focus {
  color: white;
}
.toolbar-title {
  display: flex;
  align-items: center !important;
  justify-content: center;
}
</style>