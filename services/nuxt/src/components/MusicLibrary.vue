<template>
  <div class="music-search-contain">
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
    <div>
      <div>
        <v-btn x-small text color="#ccc">
          LIBRARY
        </v-btn>
        <v-btn tile small text>
          <v-icon small left>mdi-face</v-icon> ARTISTS
        </v-btn>
        <v-btn tile small text>
          <v-icon small left>mdi-album</v-icon> ALBUMS
        </v-btn>
        <v-btn tile small text>
          <v-icon small left>mdi-waveform</v-icon> TRACKS
        </v-btn>
      </div>
      <div>
        <v-btn x-small text color="#ccc">
          PLAYLISTS
        </v-btn>
        <v-btn tile small text>
          <v-icon small left>mdi-plus</v-icon> Create Playlist
        </v-btn>
        <v-btn tile small text>
          <v-icon small left>mdi-timelapse</v-icon> Recently Added
        </v-btn>
      </div>
      <div>
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
      <div>
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
  </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex';


export default {
  data: () => ({
  }),
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
.music-search-contain {
  width: 20%;
  margin: 1rem;
  align-self: flex-start;
}
.library-menu-contain {
  list-style: none;
}
>>>.music-searchbar div {
  padding: 0;
}
>>>.music-searchbar-textfield input {
  font-size: 0.8rem;
}
</style>
