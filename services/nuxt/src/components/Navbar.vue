<template>
  <div>
    <v-navigation-drawer
      v-model="drawer"
      app
      color="#272727"
      dark
      stateless
    >
      <v-list nav>
        <v-list-item
          v-for="navObject in filteredNavObjects"
          :key="navObject.title"
          active-class="activeListItem"
          link
          :to="navObject.nav"
        >
          <v-list-item-icon>
            <v-icon>{{ navObject.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{ navObject.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <template v-if="auth.loggedIn" v-slot:append>
        <div class="pa-2">
          <v-btn to="/profile" block>
            Profile
          </v-btn>
          <v-btn block @click="signOut">
            Logout
          </v-btn>
        </div>
      </template>
    </v-navigation-drawer>      
    <v-app-bar 
      :class="{ 'needs-apple-auth': !isAuthorized }"
      fixed
      app
    >
      <v-app-bar-nav-icon
        class="menu-navigation"
        color="#ccc"
        @click="drawer=!drawer"
      />
      <v-toolbar-title style="padding-left: 25px">
        <nuxt-link to="/">
          <span class="drumrose-title">DRUMROSE</span>
        </nuxt-link>
      </v-toolbar-title>
      <v-spacer />
      <v-btn
        v-if="!auth.loggedIn"
        color="var(--primary-red)"
        @click="login"
      >
        Log In
      </v-btn>
      <v-spacer />
      <SearchBar />
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
          title: 'Library',
          nav: '/library',
          icon: 'mdi-library',
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
    };
  },
  computed: {
    ...mapState(['auth', 'isAuthorized']),
    currentRouteName () {
      return 'DRUMROSE';
    },
    filteredNavObjects () {
      return this.navObjects.filter( navObject => ((!this.auth.loggedIn &&
        !navObject.requiresAuth) || this.auth.loggedIn) &&
((!this.$store.state.isAuthorized &&
        !navObject.requiresAppleAuth) || this.$store.state.isAuthorized)
      );
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
        console.log(AUTH0_DOMAIN);
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
  font-family: 'Drumrose', monospace !important;
}
.drumrose-title:hover, .drumrose-title:focus {
  color: white;
}
.menu-navigation:hover, .menu-navigation:focus {
  color: white;
}
</style>