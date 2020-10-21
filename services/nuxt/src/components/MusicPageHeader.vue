<template>
  <v-responsive
    v-if="!loading && trackInfo"
    class="track-contain"
  >
    <v-card
      style="padding: 2rem;"
    >
      <v-row flex class="content-contain">
        <v-col cols="12" sm="8">
          <v-layout>
            <v-flex justify-space-between>
              <v-container>
                <v-row flex style="justify-content: space-between; align-items: flex-start; margin-left: 0">
                  <v-layout align-center justify-left>
                    <v-btn v-if="!playing" fab medium @click="playTrack">
                      <v-icon>mdi-play</v-icon>
                    </v-btn>
                    <v-btn v-else fab medium @click="pauseTrack">
                      <v-icon>mdi-pause</v-icon>
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
                  <span class="overline">{{ trackInfo.attributes.playlistType }} Playlist  |  </span>
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
                      <v-btn x-small tile dark @click="favoriteTrack">
                        <v-icon x-small left>
                          mdi-thumb-up
                        </v-icon>
                        More Like This
                      </v-btn>
                    </v-col>
                    <v-col>
                      <v-btn x-small tile dark @click="favoriteTrack">
                        <v-icon x-small left>
                          mdi-thumb-down
                        </v-icon>
                        Less Like This
                      </v-btn>
                    </v-col>
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
                        Add to Queue
                      </v-btn>
                    </v-col>
                    <v-col>
                      <v-btn x-small tile dark>
                        <v-icon x-small left>
                          mdi-playlist-music
                        </v-icon>
                        Add to Playlist
                      </v-btn>
                    </v-col>
                    <v-col>
                      <v-btn x-small tile dark>
                        <v-icon x-small left>
                          mdi-library
                        </v-icon>
                        Add to Library
                      </v-btn>
                    </v-col>
                    <v-col>
                      <v-btn @click="shareLink" x-small tile dark>
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
              width="100%"
              height="auto"
              :src="appleImage"
            />
          </v-badge>
          
          <v-spacer />
          <v-flex>
            <v-layout justify-space-between>
              <span class="overline"><strong>RATINGS</strong></span>
              <span class="overline">433 Total</span>
              <span class="overline"><strong>Average</strong> 4.5</span>
            </v-layout>
          </v-flex>
          <v-divider />
          <v-flex width="100%">
            <v-layout justify-space-between>
              <v-rating
                dense
                readonly
                color="var(--primary-purple)"
                :value="0.5"
                length="1"
                half-increments
                x-small
              />
              <v-rating
                dense
                readonly
                color="var(--primary-purple)"
                :value="5"
                length="5"
                x-small
              />
            </v-layout>
            <v-sparkline
              :value="values"
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
          </v-flex>
        </v-col>
      </v-row>
      <v-row v-if="type === 'albums'">
        <v-list class="track-list" two-line>
          <v-row>
            <v-layout flex>
              <v-subheader
                v-if="trackInfo.relationships.tracks.data.length === 1"
                class="overline"
              >{{ trackInfo.relationships.tracks.data.length }} Track</v-subheader>
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
            <template v-for="(track, index) in trackInfo.relationships.tracks.data">
              <v-hover
                :key="`track-${index}`"
                v-slot:default="{ hover }"
              >
                <v-list-item>
                  <QueueItem :track-object="track" />
                </v-list-item>
              </v-hover>
            </template>
          </v-list-item-group>
        </v-list>
      </v-row>
      <v-row v-else-if="type === 'playlists'">
        <v-list class="track-list" two-line>
          <v-row>
            <v-layout flex>
              <v-subheader
                v-if="trackInfo.relationships.tracks.data.length === 1"
                class="overline"
              >{{ trackInfo.relationships.tracks.data.length }} Track</v-subheader>
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
            <template v-for="(track, index) in trackInfo.relationships.tracks.data">
              <v-hover
                :key="`track-${index}`"
                v-slot:default="{ hover }"
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
import { postFavorite } from '~/api/api';
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
  },
  data: () => ({
    trackInfo: null,
    loading: true,
    playing: false,
    rating: 0.5,
    rules: [v => v.length <= 255 || 'Max 255 characters'],
    selection: null,
    lockSelection: false,
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
    ...mapState(['queue']),
    totalDuration () {
      return this.trackInfo.relationships.tracks.data.reduce( function (a, b) {
        let trackTwoDuration = 0;

        if (b && 'attributes' in b) {
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
      console.log(idx)
      this.selectTrack(idx);
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
      } else if (this.type === 'playlists') {
        const resp = await this.$store.getters.fetch(
          `/v1/catalog/us/playlists/${this.$route.params.id}`
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
      } else if (this.type === 'playlists') {
        await this.$store.dispatch("setQueue", {
          'playlist': this.trackInfo.id,
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
      let dummy = document.createElement('input'),
      text = this.$route.path;

      document.body.appendChild(dummy);
      dummy.value = text;
      dummy.select();
      document.execCommand('copy');
      document.body.removeChild(dummy);
      this.$toast.success('Copied link to clipboard')
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