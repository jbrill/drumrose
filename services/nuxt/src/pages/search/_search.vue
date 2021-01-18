<template>
  <v-container fluid>
    <v-responsive v-if="!loading">
      <v-row>
        <v-select
          v-model="selectedItems"
          :items="items"
          style="margin: 2rem"
          attach
          chips
          label="SHOW RESULTS FOR"
          multiple
        />
      </v-row>
      <v-list style="padding: 2rem" two-line>
        <v-subheader>
          {{ search }} - {{ searchNum }} Results
        </v-subheader>
        <span
          v-if="
            selectedItems.includes('Tracks') && searchResults.songs.length
          "
          class="overline"
        >
          Tracks
        </span>
        <v-list-item-group
          v-if="
            selectedItems.includes('Tracks') && searchResults.songs.length
          "
          v-model="selectedSearch"
        >
          <template
            v-for="
              (song, songIdx) in searchResults.songs
            "
          >
            <v-hover
              :key="'song' + songIdx"
            >
              <v-list-item>
                <v-list-item-avatar>
                  <v-img :src="appleImage(song)" />
                </v-list-item-avatar>
                <v-list-item-content>
                  <v-list-item-title>
                    <nuxt-link
                      style="color: white"
                      :to="'/tracks/' + song.id"
                    >
                      {{ song.attributes.name }}
                    </nuxt-link>
                  </v-list-item-title>

                  <v-list-item-subtitle>
                    {{ song.attributes.artistName }}
                  </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-hover>
          </template>
        </v-list-item-group>
        <span
          v-if="
            selectedItems.includes('Albums') && searchResults.albums.length
          "
          class="overline"
        >Albums</span>
        <v-list-item-group
          v-if="
            selectedItems.includes('Albums') && searchResults.albums.length
          "
          v-model="selectedSearch"
        >
          <template
            v-for="
              (album, albumIdx) in searchResults.albums
            "
          >
            <v-hover
              :key="'album' + albumIdx"
            >
              <v-list-item>
                <v-list-item-avatar>
                  <v-img :src="appleImage(album)" />
                </v-list-item-avatar>
                <v-list-item-content>
                  <v-list-item-title>
                    <nuxt-link
                      style="color: white"
                      :to="'/albums/' + album.id"
                    >
                      {{ album.attributes.name }}
                    </nuxt-link>
                  </v-list-item-title>
                  <v-list-item-subtitle>
                    {{ album.attributes.artistName }}
                  </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-hover>
          </template>
        </v-list-item-group>
        <span
          v-if="
            selectedItems.includes('Artists') && searchResults.playlists.length
          "
          class="overline"
        >
          Playlists
        </span>
        <v-list-item-group
          v-if="
            selectedItems.includes('Artists') && searchResults.playlists.length
          "
          v-model="selectedSearch"
        >
          <template
            v-for="
              (playlist, playlistIdx) in searchResults.playlists
            "
          >
            <v-hover
              :key="'playlist' + playlistIdx"
            >
              <v-list-item>
                <v-list-item-avatar>
                  <v-img :src="appleImage(playlist)" />
                </v-list-item-avatar>
                <v-list-item-content>
                  <v-list-item-title>
                    <nuxt-link
                      style="color: white"
                      :to="
                        '/playlists/' + playlist.id
                      "
                    >
                      {{ playlist.attributes.name }}
                    </nuxt-link>
                  </v-list-item-title>
                  <v-list-item-subtitle>
                    {{ playlist.attributes.curatorName }}
                  </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-hover>
          </template>
        </v-list-item-group>
        <span
          v-if="
            selectedItems.includes('Artists') && searchResults.artists.length"
          class="overline"
        >Artists</span>
        <v-list-item-group
          v-if="
            selectedItems.includes('Artists') && searchResults.artists.length
          "
          v-model="selectedSearch"
        >
          <template
            v-for="
              (artist, artistIdx) in searchResults.artists
            "
          >
            <v-hover
              :key="'artist' + artistIdx"
            >
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>
                    <nuxt-link
                      :to="
                        '/artists/' + artist.id
                      "
                      style="color: white"
                    >
                      {{ artist.attributes.name }}
                    </nuxt-link>
                  </v-list-item-title>
                  <v-list-item-subtitle>
                    {{ artist.attributes.curatorName }}
                  </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-hover>
          </template>
        </v-list-item-group>
      </v-list>
    </v-responsive>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    search: null,
    searchResults: {
      'songs': [],
      'artists': [],
      'playlists': [],
      'albums': [],
    },
    loading: true,
    items: ['Tracks', 'Playlists', 'Albums', 'Artists'],
    selectedItems: ['Tracks', 'Playlists', 'Albums', 'Artists'],
    selectedSearch: null,
  }),
  computed: {
    searchNum () {
      console.log(this.selectedItems)
      let total = 0;
      if ('songs' in this.searchResults) {
        total += this.searchResults.songs.length;
      }
      if ('artists' in this.searchResults) {
        total += this.searchResults.artists.length;
      }
      if ('playlists' in this.searchResults) {
        total += this.searchResults.playlists.length;
      }
      if ('albums' in this.searchResults) {
        total += this.searchResults.albums.length;
      }
      return total;
    },
  },
  watch: {
    selectedSearch: function (idx) {
      this.selectTrack(idx);
    },
  },
  async mounted () {
    this.search = this.$route.params.search;
    this.$store.dispatch('getHints', this.search).then(res => {
      if ('songs' in res.results) {
        this.searchResults.songs = res.results.songs.data;
      }
      if ('artists' in res.results) {
        this.searchResults["artists"] = res.results.artists.data;
      }
      if ('albums' in res.results) {
        this.searchResults["albums"] = res.results.albums.data;
      }
      if ('playlists' in res.results) {
        this.searchResults["playlists"] = res.results.playlists.data;
      }
    });
    console.log(this.searchResults);
    this.loading = false;
  },
  methods: {
    async selectTrack (trackIdx) {
      console.log(trackIdx)
      try {
          await this.$store.dispatch("setQueue", {
            'song': this.trackInfo.relationships.tracks.data[trackIdx].id,
          });
          this.$store.dispatch("play");
        } catch (err) {
          console.error(err);
        }
    },
    appleImage (trackObject) {
      return trackObject.attributes.artwork.url.replace(
        '{w}', '250'
      ).replace(
        '{h}', '250'
      );
    },
  },
};
</script>

<style scoped>
</style>
