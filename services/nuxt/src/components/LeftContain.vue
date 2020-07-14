<template>
  <div class="nav-contain">
    <div>
      <v-btn-toggle active-class="button-active" class="button-group-contain" borderless background-color="transparent" mandatory v-model="toggle_exclusive">
        <v-btn @click="toggle_exclusive = 0" rounded class="nav-button" block nuxt to="/" medium text>
          <v-icon small left>mdi-home</v-icon> HOME
        </v-btn>
        <v-btn @click="toggle_exclusive = 1" rounded class="nav-button" block nuxt to="/library" medium text>
          <v-icon small left>mdi-file-music</v-icon> LIBRARY
        </v-btn>
        <v-btn @click="toggle_exclusive = 2" class="nav-button" block nuxt to="/discover" medium text>
          <v-icon small left>mdi-waveform</v-icon> DISCOVER
        </v-btn>
        <v-btn @click="toggle_exclusive = 3" class="nav-button" block nuxt to="/users/" medium text>
          <v-icon small left>mdi-account-music</v-icon> PROFILE
        </v-btn>
        <v-btn @click="toggle_exclusive = 4" class="nav-button" block nuxt to="/settings" medium text>
          <v-icon small left>mdi-cogs</v-icon> SETTINGS
        </v-btn>
      </v-btn-toggle>
    </div>
    <div class="account-contain">
       <v-menu top dark offset-y>
        <template v-slot:activator="{ on }">
          <v-btn
            tile
            dark
            class="profile-menu-button-contain"
            v-on="on"
          >{{ auth.user.nickname }}
            <v-icon
              right
              dark
              v-on="on"
            >
              mdi-chevron-down
            </v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item
            @click="signOut"
          >
            <v-list-item-title>Logout</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex';
import { getFavorites } from '~/api/api';

export default {
 data () {
    return {
      toggle_exclusive: 0,
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
      console.log("YOO")
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
>>>.nav-button:hover, >>>.nav-button:focus {
  color: white !important;
}
.account-contain {
  position: absolute;
  bottom: 10%;
}
.button-active {
  background-color: var(--primary-purple);
}
.button-group-contain {
  padding-top: 5vh;
}
>>>.v-btn {
  border-radius: 2rem;
  padding-bottom: 1rem;
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
