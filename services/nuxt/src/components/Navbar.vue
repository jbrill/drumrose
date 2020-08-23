<template>
<div>
	<v-navigation-drawer
		v-model="drawer"
		app
    color="#272727"
    dark
	>
		<v-list nav>
      <v-list-item
        active-class="activeListItem"
        v-for="navObject in navObjects"
        v-if="((!auth.loggedIn && !navObject.requiresAuth) || auth.loggedIn) && ((!isAuthorized && !navObject.requiresAppleAuth) || isAuthorized)"
        :key="navObject.title"
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
       <v-btn @click="signOut" block>Logout</v-btn>
     </div>
  </template>
</v-navigation-drawer>      
<v-app-bar fixed app>
  <v-app-bar-nav-icon @click="drawer=!drawer"></v-app-bar-nav-icon>
	<v-toolbar-title style="padding-left: 25px"><nuxt-link to="/"><span>DRUMROSE</span></nuxt-link></v-toolbar-title>
	<v-spacer></v-spacer>
  <v-btn color="var(--primary-purple)" @click="login" v-if="!auth.loggedIn">Log In</v-btn>
  <v-spacer></v-spacer>
  <SearchBar />
</v-app-bar>  
</div>
</template>

<script>
import { mapState } from 'vuex';
import SearchBar from '~/components/SearchBar';
import LeftContain from '~/components/LeftContain';

export default {
  components: {
    SearchBar,
    LeftContain
  },
  data () {
    return {
      drawer: false,
      navObjects: [
        { title: 'Home', nav: '/', icon: 'mdi-home', requiresAuth: false, requiresAppleAuth: false },
        { title: 'Discover', nav: '/discover', icon: 'mdi-waveform',
requiresAuth: false, requiresAppleAuth: false },
        { title: 'People', nav: '/people', icon: 'mdi-account', requiresAuth: false, requiresAppleAuth: false },
        { title: 'Library', nav: '/library', icon: 'mdi-library', requiresAuth: false, requiresAppleAuth: true },
        { title: 'Settings', nav: '/settings', icon: 'mdi-cogs', requiresAuth: false, requiresAppleAuth: false },
      ],
    }
  },
  computed: {
    ...mapState(['auth', 'isAuthorized']),
    currentRouteName() {
      return 'DRUMROSE'
    },
  },
  methods: {
    login () {
      this.$auth.loginWith('auth0')
    },
    async signOut () {
      await this.$auth.logout();
      if (process.client) {
        const AUTH0_DOMAIN = 'drumrose.auth0.com';
        const AUTH0_CLIENT_ID = 'nA1RUMeTG88LVxGeEJc9Xu4PhWPHQRTg';
        console.log(AUTH0_DOMAIN)
        window.location.href = `https://${AUTH0_DOMAIN}/v2/logout?returnTo=https%3A%2F%2Fteton.drumrose.io&client_id=${AUTH0_CLIENT_ID}`
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
</style>
