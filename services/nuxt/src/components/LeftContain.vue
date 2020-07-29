<template>
<v-layout flex width="100%">
  <v-navigation-drawer
    dark
    color="transparent"
    permanent
  >
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title>
          DRUMROSE
        </v-list-item-title>
        <v-list-item-subtitle>
          AFFECT CULTURE
        </v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>

    <v-divider></v-divider>
      <v-list>
        <v-list-item
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
        <v-spacer></v-spacer>
        <v-list-item v-if="auth.loggedIn" two-line :class="miniVariant && 'px-0'">
					<v-list-item-avatar>
					</v-list-item-avatar>

					<v-list-item-content>
						<v-list-item-title>{{ auth.user.email }}</v-list-item-title>
						<v-list-item-subtitle>Subtext</v-list-item-subtitle>
					</v-list-item-content>
					<div class="pa-2">
						<v-btn
							block
						>LOGOUT</v-btn>
				  </div>
        </v-list-item>

			</v-list>
  </v-navigation-drawer>
</v-layout>
</template>

<script>
import { mapState, mapGetters } from 'vuex';
import { getFavorites } from '~/api/api';

export default {
 data () {
    return {
      navObjects: [
        { title: 'Home', nav: '/', icon: 'mdi-home', requiresAuth: false, requiresAppleAuth: false },
        { title: 'For You', nav: '/foryou', icon: 'mdi-apple', requiresAuth: false, requiresAppleAuth: true },
        { title: 'Trending', nav: '/trending', icon: 'mdi-waveform', requiresAuth: false, requiresAppleAuth: false },
        { title: 'People', nav: '/people', icon: 'mdi-account', requiresAuth: true, requiresAppleAuth: false },
        { title: 'Library', nav: '/library', icon: 'mdi-library', requiresAuth: false, requiresAppleAuth: true },
        { title: 'Profile', nav: '/profile', icon: 'mdi-account', requiresAuth: true, requiresAppleAuth: false },
        { title: 'Settings', nav: '/settings', icon: 'mdi-cogs', requiresAuth: false, requiresAppleAuth: false },
      ],
    }
  }, 
  async asyncData () {
    const favoritesResponse = await getFavorites();
    return {
      "favorites": favoritesResponse.data,
    }    
  },
  watch:{
    $route (to, from){
      this.toggle_exclusive = 4;
    }
  }, 
  computed: {
    ...mapState(['auth', 'isAuthorized']),
    artistInfo () {
      return [
        {
          name: 'Artists',
          children: this.artists
        }
      ]
    },
    trackInfo () {
      return [
        {
          name: 'Tracks',
          children: this.tracks
        }
      ]
    },
    albumInfo () {
      return [
        {
          name: 'Albums',
          children: this.albums
        }
      ]
    },
  }, 
  methods: {
    async signOut () {
      await this.$auth.logout();
      if (process.client) {
        const AUTH0_DOMAIN = 'drumrose.auth0.com';
        const AUTH0_CLIENT_ID = 'nA1RUMeTG88LVxGeEJc9Xu4PhWPHQRTg';
        console.log(AUTH0_DOMAIN)
        window.location.href = `https://${AUTH0_DOMAIN}/v2/logout?returnTo=https%3A%2F%2Fteton.drumrose.io&client_id=${AUTH0_CLIENT_ID}`
      }
    },
    async fetchArtists(item) {
      // Load the collection
      this.loading = true;
      /***this.error = null;
      this.collection = [];
      let options = {
        limit: 100
      };
      try {
        for (var offset = 0, res = null; res === null || res.length !== 0; offset += options.limit) {
          res = await this.$store.getters['musicKit/get'](this.$route.meta.isLibrary, 'artists', null, mergeWith(options, { offset: offset }));
          this.collection = this.collection.concat(res);
        }
      } catch (err) {
        console.error(err);
        Raven.captureException(err);
        this.error = err;
      }
      this.loading = false;
		},***/	
      return fetch('https://jsonplaceholder.typicode.com/users')
				.then(res => res.json())
				.then(json => (item.children.push(...json)))
				.catch(err => console.warn(err))
		},
    async fetchTracks(item) {
			return fetch('https://jsonplaceholder.typicode.com/users')
				.then(res => res.json())
				.then(json => (item.children.push(...json)))
				.catch(err => console.warn(err))
		},
    async fetchAlbums(item) {
			return fetch('https://jsonplaceholder.typicode.com/users')
				.then(res => res.json())
				.then(json => (item.children.push(...json)))
				.catch(err => console.warn(err))
		},
  }, 
};
</script>

<style scoped>
.library-menu-contain {
  list-style: none;
}
>>>.nav-contain {
  justify-content: space-between;
  display: flex;
  flex-direction: column;
  align-items: center;
}
>>>a.nav-button {
  border-radius: 2rem !important;
}
>>>.v-item-group {
  flex-direction: column
}
>>>.music-searchbar div {
  padding: 0;
}
>>>.music-searchbar-textfield input {
  font-size: 0.8rem;
}
</style>
