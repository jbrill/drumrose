<template>
  <v-responsive
    class="track-contain"
  >
    <v-skeleton-loader
      v-if="loading || !trackInfo"
      class="mx-auto"
      type="card"
    />
    <v-card
      v-else
      style="padding: 2rem;"
    >
      <v-row flex class="content-contain">
        <v-col cols="12" sm="8">
          <v-layout>
            <v-flex justify-space-between>
              <v-container>
                <v-row
                  flex
                  style="
                    justify-content: space-between;
                    align-items: flex-start;
                    margin-left: 0
                  "
                >
                  <v-layout align-center justify-left>
                    <v-btn
                      v-if="
                        playing === true && playbackState === 2
                      "
                      :loading="
                        playing === true && playbackState !== 2
                      "
                      fab
                      medium
                      @click="pauseTrack"
                      @click.native.stop.prevent
                    >
                      <v-icon>
                        mdi-pause
                      </v-icon>
                    </v-btn>
                    <v-btn
                      v-else
                      :loading="playing === true && playbackState !== 2"
                      fab
                      medium
                      @click="playTrack"
                      @click.native.stop.prevent
                    >
                      <v-icon>
                        mdi-play
                      </v-icon>
                    </v-btn>
                    <v-flex class="music-title-contain">
                      <h2 class="headline">
                        {{ trackInfo.attributes.name }}
                      </h2>
                      <nuxt-link
                        v-if="type === 'songs' || type === 'albums'"
                        class="subtitle"
                        :to="
                          '/artists/' +
                            trackInfo.relationships.artists.data[0].id
                        "
                      >
                        <span
                          class="white--text subtitle"
                        >
                          {{ trackInfo.attributes.artistName }}
                        </span>
                      </nuxt-link>
                      <a
                        v-else-if="type === 'playlists'"
                        class="subtitle"
                        target="_blank"
                        :href="
                          'https://music.apple.com/profile/' + 
                            trackInfo.attributes.curatorSocialHandle
                        "
                      >
                        <span>{{ trackInfo.attributes.curatorName }}</span>
                      </a>
                    </v-flex>
                  </v-layout>
                </v-row>
                <v-row
                  v-if="type === 'albums'"
                  class="type-contain"
                >
                  <span class="overline">Album  | 
                    Released In   <strong>
                      {{ trackInfo.attributes.releaseDate.split('-')[0] }}
                    </strong>
                  </span>
                </v-row>
                <v-row
                  v-if="type === 'songs'"
                  class="type-contain" 
                >
                  <span class="overline">Track  | 
                    Released In   
                    <strong>
                      {{ trackInfo.attributes.releaseDate.split('-')[0] }}
                    </strong>
                  </span>
                </v-row>
                <v-row
                  v-else-if="type === 'playlists'"
                  class="type-contain"
                >
                  <span
                    class="overline"
                  >
                    {{ trackInfo.attributes.playlistType }} Playlist  |  
                  </span>
                  <h5
                    class="overline"
                    style="text-align: right;"
                  >
                    Last Modified In
                    <strong>
                      {{ trackInfo.attributes.lastModifiedDate.split('-')[0] }}
                    </strong>
                  </h5>
                </v-row>
                <v-row>
                  <span class="overline">
                    <strong v-if="'recordLabel' in trackInfo.attributes">
                      {{ trackInfo.attributes.recordLabel }} 
                    </strong>
                    <span
                      v-if="
                        'recordLabel' in trackInfo.attributes &&
                          'copyright' in trackInfo.attributes
                      "
                    > | </span>
                    <span v-if="'copyright' in trackInfo.attributes">
                      {{ trackInfo.attributes.copyright }}
                    </span>
                  </span>
                </v-row>
              </v-container>
              <v-card-actions>
                <v-container full-width>
                  <v-row dense style="width: 100%">
                    <v-col>
                      <v-tooltip
                        v-if="!auth.loggedIn"
                        top
                      >
                        <template v-slot:activator="{ on }">
                          <div v-on="on">
                            <v-btn
                              x-small
                              tile
                              disabled
                              dark
                            >
                              <v-icon x-small left>
                                mdi-heart
                              </v-icon>
                              Favorite
                            </v-btn>
                          </div>
                        </template>
                        <span>Log In To Favorite</span>
                      </v-tooltip>
                      <v-btn
                        v-else-if="didFavorite"
                        x-small
                        tile
                        color="var(--primary-red)"
                        @click="postFavorite"
                      >
                        <v-icon x-small color="red" left>
                          mdi-heart
                        </v-icon>
                        Favorite
                      </v-btn>
                      <v-btn
                        v-else
                        x-small
                        tile
                        dark
                        @click="postFavorite"
                      >
                        <v-icon x-small left>
                          mdi-heart
                        </v-icon>
                        Favorite
                      </v-btn>
                    </v-col>
                    <v-col>
                      <v-tooltip
                        v-if="!auth.loggedIn"
                        top
                      >
                        <template v-slot:activator="{ on }">
                          <div v-on="on">
                            <v-btn
                              x-small
                              tile
                              disabled
                              dark
                            >
                              <v-icon x-small left>
                                mdi-playlist-music
                              </v-icon>
                              Add to Playlist
                            </v-btn>
                          </div>
                        </template>
                        <span>Log In To Add To Playlist</span>
                      </v-tooltip>
                      <v-btn v-else x-small tile dark>
                        <v-icon x-small left>
                          mdi-playlist-music
                        </v-icon>
                        Add to Playlist
                      </v-btn>
                    </v-col>
                    <v-col>
                      <v-tooltip
                        v-if="!auth.loggedIn"
                        top
                      >
                        <template v-slot:activator="{ on }">
                          <div v-on="on">
                            <v-btn
                              x-small
                              tile
                              disabled
                              dark
                            >
                              <v-icon x-small left>
                                mdi-pencil
                              </v-icon>
                              Write a Review
                            </v-btn>
                          </div>
                        </template>
                        <span>Log In To Write a Review</span>
                      </v-tooltip>
                      <v-btn v-else x-small tile dark>
                        <v-icon x-small left>
                          mdi-pencil
                        </v-icon>
                        Write a Review
                      </v-btn>
                    </v-col>
                    <v-col>
                      <v-btn
                        x-small
                        tile
                        dark
                        @click="addToQueue"
                      >
                        <v-icon x-small left>
                          mdi-playlist-star
                        </v-icon>
                        Add to Queue
                      </v-btn>
                    </v-col>
                    <v-col>
                      <v-btn
                        x-small
                        tile
                        dark
                        @click="shareLink"
                      >
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
              <v-row
                v-if="'description' in trackInfo.attributes"
              >
                <v-flex style="padding-top: 2vh">
                  <p class="caption">
                    {{ trackInfo.attributes.description.standard }}
                  </p>
                </v-flex>
              </v-row>
              <v-row
                v-if="type === 'songs'"
                style="padding-top: 1vh"
              >
                <span class="overline">Track
                  <strong>
                    {{ trackInfo.attributes.trackNumber }}
                  </strong> off
                  <nuxt-link
                    v-if="type === 'songs'"
                    class="album-name overline"
                    style="text-decoration: underline"
                    nuxt
                    :to="
                      '/albums/' + trackInfo.relationships.albums.data[0].id
                    "
                  >
                    {{ trackInfo.attributes.albumName }}
                  </nuxt-link>
                </span>
              </v-row>
              <v-row>
                <v-flex
                  v-if="
                    'genreNames' in trackInfo.attributes &&
                      trackInfo.attributes.genreNames.length
                  "
                  style="width: 100%; padding-top: 1vh"
                >
                  <v-chip
                    v-for="
                      (genre, genreIdx) in trackInfo.attributes.genreNames
                    "
                    :key="'genre-' + genreIdx"
                    label
                    x-small
                  >
                    #{{ genre }}
                  </v-chip>
                </v-flex>
              </v-row>
              <v-row
                v-if="'editorialNotes' in trackInfo.attributes"
              >
                <v-flex style="padding-top: 2vh">
                  <p class="caption">
                    {{ trackInfo.attributes.editorialNotes.short }}
                  </p>
                </v-flex>
              </v-row>
            </v-flex>
          </v-layout>
        </v-col>
        <v-col cols="12" sm="3">
          <v-card dark class="rounded-0" elevation="12">
            <v-badge
              avatar
              bordered
              overlap
              style="width: 100%"
              icon="mdi-waveform"
              color="var(--primary-purple)"
            >
              <v-img
                v-if="'artwork' in trackInfo.attributes"
                style="margin: 0 auto"
                width="100%"
                height="auto"
                :src="appleImage"
                class="fill-height"
                gradient="
                  to top right, rgba(100,115,201,.0), rgba(25,32,72,.34)
                "
              >
                <template v-slot:placeholder>
                  <v-row
                    class="fill-height ma-0"
                    align="center"
                    justify="center"
                  >
                    <v-progress-circular
                      indeterminate
                      color="grey lighten-5"
                    />
                  </v-row>
                </template>
              </v-img>
            </v-badge>
          </v-card>
          <v-layout
            justify-center
          >
            <v-fade-transition leave-absolute>
              <v-tooltip
                v-if="!auth.loggedIn"
                top
              >
                <template v-slot:activator="{ on }">
                  <v-list-item
                    :style="{
                      'justify-content':'center',
                      'align-items': 'center',
                      'height': '1rem'
                    }"
                    v-on="on"
                  >
                    <v-rating
                      v-model="rating"
                      readonly
                      empty-icon="mdi-star-outline"
                      full-icon="mdi-star"
                      half-icon="mdi-star-half-full"
                      background-color="grey"
                      color="var(--primary-red)"
                      style="padding-top: 2rem"
                      dense
                      half-increments
                      hover
                      size="24"
                      @input="changeRating($event)"
                      @click.native.stop.prevent
                    />
                  </v-list-item>
                </template>
                <span>Log In To Rate</span>
              </v-tooltip>
              <v-rating
                v-model="rating"
                empty-icon="mdi-star-outline"
                full-icon="mdi-star"
                half-icon="mdi-star-half-full"
                background-color="white"
                color="var(--primary-red)"
                style="padding-top: 2rem"
                dense
                half-increments
                hover
                size="24"
                @input="changeRating($event)"
                @click.native.stop.prevent
              />
            </v-fade-transition>
          </v-layout>
          <v-spacer />
          <v-container v-if="totalRatings > 0">
            <v-flex>
              <v-layout justify-space-between>
                <v-flex>
                  <span class="overline"><strong>RATINGS</strong></span>
                  <span class="overline">{{ totalRatings }} Total</span>
                </v-flex>
                <v-flex>
                  <span class="overline"><strong>Average</strong></span>
                  <span class="overline">{{ avg }} / 5.0</span>
                </v-flex>
              </v-layout>
            </v-flex>
            <v-divider />
            <v-flex width="100%">
              <v-sparkline
                :value="ratingValues"
                color="white"
                line-width="3"
                padding="16"
                :gradient="
                  [
                    'var(--primary-purple)',
                    'var(--primary-yellow)',
                    'var(--primary-red)'
                  ]
                "
                auto-draw
                type="bar"
              />
              <v-layout justify-space-between>
                <span class="overline">0.0</span>
                <span class="overline">5.0</span>
              </v-layout>
            </v-flex>
          </v-container>
        </v-col>
      </v-row>
    </v-card>
    <v-skeleton-loader
      v-if="loading || !trackInfo"
      class="mx-auto"
    />
    <v-card
      v-else-if="type === 'albums' || type === 'playlists'"
      style="padding: 2rem; margin-top: 2rem"
    >
      <v-row v-if="type === 'albums'">
        <v-list class="track-list" two-line>
          <v-row>
            <v-layout flex>
              <v-subheader
                v-if="trackInfo.relationships.tracks.data.length === 1"
                class="overline"
              >
                {{ trackInfo.relationships.tracks.data.length }} Track
              </v-subheader>
              <v-subheader v-else class="overline">
                {{ trackInfo.relationships.tracks.data.length }} Tracks
              </v-subheader>
              <v-subheader class="overline">
                {{ totalDuration }} Minutes
              </v-subheader>
            </v-layout>
          </v-row>
          <v-list-item-group
            v-model="selection"
          >
            <template
              v-for="
                (track, index) in trackInfo.relationships.tracks.data
              "
            >
              <v-hover
                :key="`track-${index}`"
              >
                <v-list-item>
                  <QueueItem :track-object="track" />
                </v-list-item>
              </v-hover>
            </template>
          </v-list-item-group>
        </v-list>
      </v-row>
      <v-row
        v-else-if="
          type === 'playlists'
        "
      >
        <v-list class="track-list" two-line>
          <v-row>
            <v-layout flex>
              <v-subheader
                v-if="trackInfo.relationships.tracks.data.length === 1"
                class="overline"
              >
                {{ trackInfo.relationships.tracks.data.length }} Track
              </v-subheader>
              <v-subheader v-else class="overline">
                {{ trackInfo.relationships.tracks.data.length }} Tracks
              </v-subheader>
              <v-subheader class="overline">
                {{ totalDuration }} Minutes
              </v-subheader>
            </v-layout>
          </v-row>
          <v-list-item-group
            v-model="selection"
          >
            <template
              v-for="
                (track, index) in trackInfo.relationships.tracks.data
              "
            >
              <v-hover
                :key="`track-${index}`"
              >
                <v-list-item>
                  <QueueItem :track-object="track" />
                </v-list-item>
              </v-hover>
            </template>
          </v-list-item-group>
        </v-list>
      </v-row>
    </v-card>
  </v-responsive>
</template>

<script>
import { mapState } from 'vuex';
import {
  favoriteAlbum, favoriteTrack, favoritePlaylist,
  reviewTrack, reviewAlbum, reviewPlaylist,
} from '~/api/api';
import QueueItem from '~/components/AudioPlayer/QueueItem';

export default {
  components: {
    QueueItem,
  },
  props: {
    type: {
      type: String,
      default: '',
    },
    avg: {
      type: Number,
      default: 0.0,
    },
    ratingValues: {
      type: Array,
      default: () => [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    },
    didFavorite: {
      type: Boolean,
      default: false,
    },
  },
  data: () => ({
    trackInfo: null,
    loading: true,
    playing: false,
    rating: 0.0,
    rules: [v => v.length <= 255 || 'Max 255 characters'],
    selection: null,
    lockSelection: false,
    value: '',
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
  }),
  computed: {
    appleImage () {
      return this.trackInfo.attributes.artwork.url.replace(
        '{w}', '2500'
      ).replace(
        '{h}', '2500'
      );
    },
    totalRatings () {
      return this.ratingValues.reduce((a, b) => a + b, 0);
    },
    ...mapState(['queue', 'playbackState', 'auth']),
    totalDuration () {
      return this.trackInfo.relationships.tracks.data.reduce( function (a, b) {
        let trackTwoDuration = 0;

        if (b && 'attributes' in b) {
          // eslint-disable-next-line
          trackTwoDuration = MusicKit.formattedMilliseconds(
            b.attributes.durationInMillis
          ).minutes;
        }
        return (
          a + trackTwoDuration
        );
      }, 0);
    },
  },
  watch: {
    selection: function (idx) {
      this.selectTrack(idx);
    },
  },
  async mounted () {
    try {
      if (this.type === 'songs') {
        const resp = await this.$store.getters.fetch(
          `/v1/catalog/us/songs/${this.$route.params.id}`
        );
        this.trackInfo = resp.data[0];
      } else if (this.type === 'albums') {
        const resp = await this.$store.getters.fetch(
          `/v1/catalog/us/albums/${this.$route.params.id}`
        );
        this.trackInfo = resp.data[0];
      } else if (this.type === 'playlists') {
        const resp = await this.$store.getters.fetch(
          `/v1/catalog/us/playlists/${this.$route.params.id}`
        );
        this.trackInfo = resp.data[0];
      } else if (this.type === 'library-playlists') {
        const resp = await this.$store.getters.fetch(
          `/v1/me/library/playlists/${this.$route.params.id}`
        );
        this.trackInfo = resp.data[0];
      }
      
      this.loading = false;
    } catch (err) {
      this.loading = false;
      console.error(err);
    }
  },
  methods: {
    async addToQueue () {
      if (this.type == 'songs') {
        await this.$store.dispatch("setQueue", { 'song': this.id });
        this.$toast.show(`Added track to queue`);
      }
      if (this.type == 'playlists') {
        await this.$store.dispatch("setQueue", { 'playlist': this.id });
        this.$toast.show(`Added playlist to queue`);
      }
      if (this.type == 'albums') {
        await this.$store.dispatch("setQueue", { 'album': this.id });
        this.$toast.show(`Added album to queue`);
      }
    },
    async selectTrack (trackIdx) {
      try {
          await this.$store.dispatch("setQueue", {
            'song': this.trackInfo.relationships.tracks.data[trackIdx].id,
          });
          this.$store.dispatch("play");
        } catch (err) {
          console.error(err);
        }
    },
    async postFavorite () {
      try {
        if (this.type === 'songs') {
          try {
            await favoriteTrack(
              this.$auth.getToken('auth0'),
              {
                'type': 'song', 'apple_music_id': this.trackInfo.id,
              }
            );
            this.$toast.show('Favorited track');
          } catch (err) {
            console.error(err);
            this.$toast.error(err.message);
          }
        } else if (this.type === 'albums') {
          try {
            await favoriteAlbum(
              this.$auth.getToken('auth0'),
              {
                'type': 'album', 'apple_music_id': this.trackInfo.id,
              }
            );
            this.$toast.success('Favorited album');
          } catch (err) {
            console.error(err);
            this.$toast.error(err.message);
          }
        } else if (this.type === 'playlists') {
          try {
            await favoritePlaylist(
              this.$auth.getToken('auth0'),
              {
                'type': 'playlist', 'apple_music_id': this.trackInfo.id,
              }
            );
            this.$toast.success('Favorited playlist');
          } catch (err) {
            console.error(err);
            this.$toast.error(err.message);
          }
        }
      } catch (err) {
        console.error(err);
        this.$toast.error(err.message);
      }
    },
    async changeRating (e) {
      const data = {
        'rating': e,
        'apple_music_id': this.trackInfo.id,
      };
      try {
        if (this.type === 'songs') {
          await reviewTrack(
            this.$auth.getToken('auth0'), data
          );
        } else if (this.type === 'albums') {
          await reviewAlbum(
            this.$auth.getToken('auth0'), data
          );
        } else if (
          this.type === 'playlists' || this.type === 'library-playlists'
        ) {
          await reviewPlaylist(
            this.$auth.getToken('auth0'), data
          );
        }
        this.$toast.info(`Rated ${this.trackInfo.attributes.name} ${e} stars`);
      } catch (err) {
        console.error(err);
        this.$toast.error(err);
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
      } else if (this.type === 'playlists') {
        await this.$store.dispatch("setQueue", {
          'playlist': this.trackInfo.id,
        });
      }
      else if (this.type === 'library-playlists') {
        await this.$store.dispatch("setQueue", {
          'library-playlist': this.trackInfo.id,
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
    shareLink () {
      let dummy = document.createElement('input');
      const text = process.env.baseUrl + this.$route.path;

      document.body.appendChild(dummy);
      dummy.value = text;
      dummy.select();
      document.execCommand('copy');
      document.body.removeChild(dummy);
      this.$toast.info('Copied link to clipboard');
    },
    moreLikeThis () {
      try {
        this.$store.dispatch("love", {
          'id': this.trackInfo.id, 'type': this.type,
        });
        this.$toast.success(
          "More like this will be recommended."
        );
      } catch (err) {
        console.error(err);
      }
    },
    lessLikeThis () {
      try {
        this.$store.dispatch("dislike", {
          'id': this.trackInfo.id, 'type': this.type,
        });
        this.$toast.success(
          "Less like this will be recommended."
        );
      } catch (err) {
        console.error(err);
      }
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
  justify-content: space-around;
}
.v-chip {
  margin: 5px;
}
.buttons-contain > * {
  margin: 5px;
}
.type-contain {
  margin-top: 2vh;
}
.music-title-contain {
  padding-left: 2vw;
}
.track-list {
  width: 100%;
  overflow-y: scroll;
  overflow-x: hidden;
  max-height: 20vh;
}
</style>