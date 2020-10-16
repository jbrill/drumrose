<template>
  <v-responsive
    v-if="!loading && trackInfo"
    class="track-contain"
  >
    <v-card style="padding: 2rem;">
      <v-row flex class="content-contain">
        <v-col cols="12" sm="8">
          <v-layout>
            <v-flex justify-space-between>
              <v-container>
                <v-row style="margin-left: 0">
                  <v-btn v-if="!playing" fab medium @click="playTrack">
                    <v-icon>mdi-play</v-icon>
                  </v-btn>
                  <v-btn v-else fab medium @click="pauseTrack">
                    <v-icon>mdi-pause</v-icon>
                  </v-btn>
                  <v-flex style="width: 65%; margin-left: 1rem;">
                    <h2 class="headline">
                      {{ trackInfo.attributes.name }}
                    </h2>
                    <nuxt-link
                      :to="
                        '/artists/' +
                          trackInfo.relationships.artists.data[0].id
                      "
                    >
                      <p>{{ trackInfo.attributes.artistName }}</p>
                    </nuxt-link>
                  </v-flex>
                  <v-flex width="100%">
                    <h5 class="overline" style="text-align: right;">
                      <strong>Released    </strong>{{ trackInfo.attributes.releaseDate }}
                    </h5>
                  </v-flex>
                  <span v-if="type === 'songs'">Track Number
                    <strong>
                      {{ trackInfo.attributes.trackNumber }}
                    </strong>
                    from
                    <nuxt-link
                      class="album-name"
                      style="text-decoration: underline"
                      nuxt
                      :to="
                        '/albums/' + trackInfo.relationships.albums.data[0].id
                      "
                    >
                      {{ trackInfo.attributes.albumName }}
                    </nuxt-link>
                  </span>
                  <span v-else-if="type === 'albums'">
                    <strong>
                      {{ trackInfo.attributes.trackCount }}
                    </strong>
                    tracks
                  </span>
                  <v-flex style="width: 100%">
                    <v-chip
                      v-for="(genre, genreIdx) in trackInfo.attributes
                        .genreNames"
                      :key="'genre-' + genreIdx"
                      label
                      x-small
                    >
                      #{{ genre }}
                    </v-chip>
                  </v-flex>
                </v-row>
              </v-container>
              <v-card-actions>
                <v-container full-width>
                  <v-row dense style="width: 100%">
                    <v-col>
                      <v-btn x-small tile dark @click="favoriteTrack">
                        <v-icon x-small left>
                          mdi-heart
                        </v-icon>
                        Favorite
                      </v-btn>
                    </v-col>
                    <v-col>
                      <v-btn x-small tile dark>
                        <v-icon x-small left>
                          mdi-playlist-star
                        </v-icon>
                        Queue
                      </v-btn>
                    </v-col>
                    <v-col>
                      <v-btn x-small tile dark>
                        <v-icon x-small left>
                          mdi-playlist-music
                        </v-icon>
                        Playlist
                      </v-btn>
                    </v-col>
                    <v-col>
                      <v-btn x-small tile dark>
                        <v-icon x-small left>
                          mdi-library
                        </v-icon>
                        Library
                      </v-btn>
                    </v-col>
                    <v-col>
                      <v-btn x-small tile dark>
                        <v-icon x-small left>
                          mdi-share
                        </v-icon>
                        Share
                      </v-btn>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-actions>
              <v-divider />
            </v-flex>
          </v-layout>
        </v-col>
        <v-col cols="12" sm="3">
          <v-badge
            avatar
            bordered
            overlap
            style="width: 100%"
            icon="mdi-waveform"
            color="var(--primary-purple)"
          >
            <v-img
              style="margin: 0 auto"
              width="20vw"
              height="auto"
              :src="appleImage"
            />
          </v-badge>
          <v-spacer />
          <v-sparkline
            :value="values"
            color="white"
            line-width="3"
            padding="16"
            :gradient="['#f72047', '#ffd200', '#1feaea']"
            auto-draw
            stroke-linecap="round"
          />
          <v-row align="start">
            <div class="caption grey--text text-uppercase">
              Average Rating
            </div>
            <div>
              <span class="display-2 font-weight-black" v-text="avg" />
              <span
                v-if="avg"
                class="display-1 font-weight-black"
              >/ 5.0</span>
            </div>
          </v-row>
        </v-col>
      </v-row>
    </v-card>
  </v-responsive>
</template>

<script>
import { postFavorite } from '~/api/api';


export default {
  props: {
    type: {
      type: String,
      default: '',
    },
  },
  data: () => ({
    trackInfo: null,
    loading: true,
    playing: false,
    rating: 0.5,
    rules: [v => v.length <= 255 || 'Max 255 characters'],
    value: '',
    avg: 2.5,
    labels: [
      '0',
      '0.5',
      '1',
      '1.5',
      '2',
      '2.5',
      '3',
      '3.5',
      '4',
      '4.5',
      '5',
    ],
    values: [
      200,
      675,
      410,
      390,
      310,
      460,
      250,
      240,
      250,
      240,
      740,
    ],
  }),
  computed: {
    appleImage () {
      return this.trackInfo.attributes.artwork.url.replace(
        '{w}', '2500'
      ).replace(
        '{h}', '2500'
      );
    },
  },
  async mounted () {
    try {
      if (this.type === 'songs') {
        const resp = await this.$store.getters.fetch(
          `/v1/catalog/us/songs/${this.$route.params.id}`
        );
        console.log(resp);
        this.trackInfo = resp.data[0];
      } else if (this.type === 'albums') {
        const resp = await this.$store.getters.fetch(
          `/v1/catalog/us/albums/${this.$route.params.id}`
        );
        console.log(resp);
        this.trackInfo = resp.data[0];
      }
      
      this.loading = false;
    } catch (err) {
      this.loading = false;
      console.error(err);
    }
  },
  methods: {
    async favoriteTrack () {
      try {
        await postFavorite(
          this.$auth.getToken('auth0'),
          { 'type': 'track', 'id': this.trackInfo.id }
        );
      } catch (err) {
        console.error(err);
        this.$toast.error(err.message);
      }
    },
    async playTrack () {
      if (this.type === 'songs') {
        await this.$store.dispatch("setQueue", {
          'song': this.trackInfo.id,
        });
      } else if (this.type === 'albums') {
        await this.$store.dispatch("setQueue", {
          'album': this.trackInfo.id,
        });
      }
      try {
        await this.$store.dispatch("play");
      } catch (err) {
        console.error(err);
        this.$toast.error(err.message);
      }
      this.playing = true;
    },
    async pauseTrack () {
      await this.$store.dispatch("pause");
      this.playing = false;
    },
  },
};
</script>

<style scoped>
.track-contain {
  display: flex;
}
.track-info-contain {
  align-self: center;
  justify-content: flex-end;
  padding-left: 2rem;
}
.album-img {
  width: 100%;
  height: 100%;
}
>>>.track-name {
  margin-bottom: 0;
}
.album-name {
  font-weight: bolder;
  color: #ccc;
}
.buttons-contain {
  display: flex;
}
.content-contain {
  align-items: center;
  justify-content: space-around;
}
.v-chip {
  margin: 5px;
}
.buttons-contain > * {
  margin: 5px;
}
</style>