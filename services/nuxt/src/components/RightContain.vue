<template>
  <div class="right-content-contain">
    <v-toolbar
      dense
      flat
      floating
      elevation="0"
      color="transparent"
      class="music-searchbar"
    >
      <v-text-field
        hide-details
        prepend-icon="search"
        placeholder="Search for music"
        single-line
        class="music-searchbar-textfield"
      />
    </v-toolbar>
    <div class="content-contain-right">
      <v-btn x-small text color="#ccc">
        People to Follow
      </v-btn>
      <v-list dense>
        <v-list-item-group>
          <v-list-item v-for="musicItem in recentlyPlayed">
            <v-list-item-icon>
              <v-icon>mdi-person</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title v-text="musicItem.attributes.name"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </div>
    <div class="content-contain-right">
      <v-btn x-small text color="#ccc">
        Your Favorites
      </v-btn>
      <v-list dense>
        <v-list-item-group>
          <v-list-item v-for="musicItem in recentlyPlayed">
            <v-list-item-icon>
              <v-icon>mdi-waveform</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title v-text="musicItem.attributes.name"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </div>
    <div class="content-contain-right">
      <v-btn x-small text color="#ccc">
        Listening History
      </v-btn>
      <v-list dense>
        <v-list-item-group>
          <v-list-item v-for="musicItem in favorites">
            <v-list-item-icon>
              <v-icon>mdi-waveform</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title v-text="musicItem"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex';
import { getFavorites } from '~/api/api';

export default {
  async asyncData () {
    const favoritesResponse = await getFavorites();
    return {
      "favorites": favoritesResponse.data,
    }    
  },
  computed: {
    ...mapState(['isAuthorized']),
    ...mapGetters(['recentlyPlayed', 'heavyRotation']),
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
.right-content-contain {
  width: 100%;
}
.library-menu-contain {
  list-style: none;
}
.content-contain-right {
  width: 100%;
}
>>>.music-searchbar div {
  padding: 0;
}
>>>.music-searchbar-textfield input {
  font-size: 0.8rem;
}
</style>
