<template>
  <div width="100%" class="artworkContain">
    <v-hover v-slot:default="{ hover }" class="albumContain">
      <v-card
        :elevation="hover ? 12 : 2"
        :class="{ 'on-hover': hover }"
      >
        <nuxt-link style="width: 100%" :to="link">
          <v-img
            class="albumCover"
            dark
            :src="artworkUrl"
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
            <div
              v-if="hover"
              style="position: absolute"
              class="fill-height bottom-gradient"
            />
            <v-container fill-height fluid align="center">
              <v-row align="center" justify="center">
                <v-btn
                  v-if="isPlaying === true && playbackState === 2"
                  :class="{ 'not-show-btns': !hover, 'show-btns': hover }"
                  :loading="isPlaying === true && playbackState !== 2"
                  fab
                  medium
                  @click="pauseTrack"
                  @click.native.stop.prevent
                >
                  <v-icon
                    :class="{ 'show-btns': hover }"
                  >
                    mdi-pause
                  </v-icon>
                </v-btn>
                <v-btn
                  v-else
                  :class="{ 'not-show-btns': !hover, 'show-btns': hover }"
                  :loading="isPlaying === true && playbackState !== 2"
                  fab
                  medium
                  @click="playTrack"
                  @click.native.stop.prevent
                >
                  <v-icon
                    :class="{ 'show-btns': hover }"
                  >
                    mdi-play
                  </v-icon>
                </v-btn>
              </v-row>
              <v-card-actions class="card-actions">
                <v-tooltip
                  v-if="!auth.loggedIn"
                  top
                >
                  <template v-slot:activator="{ on }">
                    <div v-on="on">
                      <v-btn
                        icon
                        disabled
                        :class="{ 'show-btns': hover }"
                        @click.native.stop.prevent
                      >
                        <v-icon
                          small
                          :class="{ 'show-btns': hover }"
                          color="transparent"
                        >
                          mdi-heart
                        </v-icon>
                      </v-btn>
                    </div>
                  </template>
                  <span>LOG IN TO FAVORITE</span>
                </v-tooltip>
                <v-btn
                  v-else
                  icon
                  :class="{ 'show-btns': hover }"
                  @click="favoriteItem()"
                  @click.native.stop.prevent
                >
                  <v-icon
                    small
                    :class="{ 'show-btns': hover }"
                    color="transparent"
                  >
                    mdi-heart
                  </v-icon>
                </v-btn>
                <v-menu
                  close-on-content-click
                  origin="bottom right"
                  z-index="10000"
                  attach
                  top
                  left
                  dark
                  two-line
                  max-width="25rem"
                  transition="scale-transition"
                >
                  <template v-slot:activator="{ on }">
                    <v-btn
                      icon
                      dark
                      :class="{ 'show-btns': hover }"
                      @click.native.stop.prevent
                      v-on="on"
                    >
                      <v-icon
                        small
                        color="transparent"
                        :class="{ 'show-btns': hover }"
                        class="album-overlay-more"
                      >
                        mdi-dots-horizontal
                      </v-icon>
                    </v-btn>
                  </template>
                  <v-list dense>
                    <v-list-item 
                      :style="{
                        'justify-content':'center'
                      }"
                    >
                      <v-rating
                        background-color="white"
                        color="var(--primary-purple)"
                        dense
                        half-increments
                        hover
                        size="18"
                        @input="changeRating"
                        @click.native.stop.prevent
                      />
                    </v-list-item>
                    <v-dialog v-model="dialog" scrollable max-width="300px">
                      <template v-slot:activator="{ on, attrs }">
                        <v-list-item
                          v-bind="attrs"
                          v-on="on"
                          @click.native.stop.prevent
                        >
                          <v-list-item-icon>
                            <v-icon small>
                              mdi-playlist-music
                            </v-icon>
                          </v-list-item-icon>
                          <v-list-item-content>
                            <v-list-item-title>
                              Add to playlist
                            </v-list-item-title>
                          </v-list-item-content>
                        </v-list-item>
                      </template>
                      <v-card>
                        <v-tabs>
                          <v-tab>Add to playlist</v-tab>
                          <v-tab>Create a playlist</v-tab>
                        </v-tabs>
                      </v-card>
                    </v-dialog>
                    <v-divider />
                    <v-list-item @click.native.stop.prevent @click="addToQueue">
                      <v-list-item-icon>
                        <v-icon small>
                          mdi-thumb-up
                        </v-icon>
                      </v-list-item-icon>
                      <v-list-item-content>
                        <v-list-item-title>More like this</v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                    <v-divider />
                    <v-list-item @click.native.stop.prevent @click="addToQueue">
                      <v-list-item-icon>
                        <v-icon small>
                          mdi-thumb-down
                        </v-icon>
                      </v-list-item-icon>
                      <v-list-item-content>
                        <v-list-item-title>Less like this</v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                    <v-divider />
                    <v-list-item @click.native.stop.prevent @click="addToQueue">
                      <v-list-item-icon>
                        <v-icon small>
                          mdi-playlist-star
                        </v-icon>
                      </v-list-item-icon>
                      <v-list-item-content>
                        <v-list-item-title>Add to queue</v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                    <v-divider />
                    <v-list-item
                      @click.native.stop.prevent
                      @click="
                        addToLibrary()
                      "
                    >
                      <v-list-item-icon>
                        <v-icon small>
                          mdi-library
                        </v-icon>
                      </v-list-item-icon>
                      <v-list-item-content>
                        <v-list-item-title>Add to library</v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list>
                </v-menu>
              </v-card-actions>
            </v-container>
          </v-img>
        </nuxt-link>
      </v-card>
    </v-hover>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import {
  favoriteTrack,
  postReview,
} from '~/api/api';

export default {
  props: {
    id: {
      type: String,
      default: '',
    },
    isActionable: {
      type: Boolean,
      default: false,
    },
    isPlayable: {
      type: Boolean,
      default: false,
    },
    artworkUrl: {
      type: String,
      default: '',
    },
    type: {
      type: String,
      default: '',
    },
    link: {
      type: String,
      default: '',
    },
  },
  data () {
    return {
      isHovering: false,
      isPlaying: false,
      dialog: false,
    };
  },
  computed: {
    ...mapState(['auth', 'isAuthorized', 'nowPlayingItem', 'playbackState']),
  },
  methods: {
		async addToQueue () {
      if (this.type == 'song') {
        await this.$store.dispatch("playNext", { 'song': this.id });
      }
      if (this.type == 'playlist') {
        await this.$store.dispatch("playNext", { 'playlist': this.id });
      }
      if (this.type == 'album') {
        await this.$store.dispatch("playNext", { 'album': this.id });
      }
      this.$toast.show(`Added ${this.type} to queue`);
    },
		async addToLibrary () {
      try {
        await this.$store.dispatch(
          "addToLibrary", {
            'id': this.id, 'type': this.type,
          }
        );
      } catch(err) {
        this.$toast.error(err);
        // this.$sentry.captureException(err);
      }
    },
		addToPlaylist: function (name, items) {
      // TODO
      this.$store.dispatch("addToPlaylist", {
        "name": name,
        "items": items,
      });
    },
    createPlaylist: function (name, items) {
      // TODO
      this.$store.dispatch("newPlaylist", {
        "name": name,
        "items": items,
      });
    },
    changeRating (e) {
      console.log(e);
      const data = {
        'rating': e,
        'type': this.type,
        'id': this.id,
      };
      postReview(this.$auth.getToken('auth0'), data);
      // TODO: Change rating via api
    },
    async pauseTrack () {
      await this.$store.dispatch("pause");
      this.isPlaying = false;
    },
    async favoriteItem () {
      if (this.type == 'song') {
        try {
          await favoriteTrack(this.id);
        } catch (err) {
          this.$toast.error(err.message);
        }
      }
    },
    async login () {
      await this.$auth.loginWith('auth0');
    },
    async playTrack () {
      if (this.type == 'song') {
        await this.$store.dispatch(
          "setQueue", { 'song': this.id }
        );
      }
      if (this.type == 'playlist') {
        await this.$store.dispatch(
          "setQueue", { 'playlist': this.id }
        );
      }
      if (this.type == 'album') {
        await this.$store.dispatch(
          "setQueue", { 'album': this.id }
        );
      }
      await this.$store.dispatch("play");
      if (!this.$store.state.isAuthorized) {
        this.$toast.show('Sign into Apple Music for full track access.');
      }
      this.isPlaying = true;
    },
  },
};
</script>

<style scoped>
@media screen and (prefers-reduced-motion: reduce) {
.v-card {
  transition: none;
}
}
.v-card {
  transition: opacity .4s ease-in-out;
  border-radius: 2px;
  outline: 2px solid var(--primary-purple);
}
.bottom-gradient {
  height: 100%;
  width: 100%;
  background-image: linear-gradient(
    to top, rgba(0, 0, 0, 0.8) 0%, transparent 72px
  );
}
.v-card:not(.on-hover) {
  opacity: 0.8;
  outline: none;
}
.card-actions {
  position: absolute;
  bottom: 0;
  right: 0;
}
.not-show-btns {
  display: none;
}
.show-btns {
  color: rgba(255, 255, 255, 1) !important;
  display: flex;
}
.albumContain {
  z-index: 0;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  box-shadow: var(--shadow-medium);
  border-radius: 2px;
}
.albumContain:hover, .albumContain:focus {
  cursor: pointer;
}
.albumCover {
  width: 100%;
  overflow: visible !important;
  height: auto;
  min-height: 15vh;
  border-radius: 2px;
}
.albumCover:hover, .albumCover:focus {
  cursor: pointer;
  box-shadow: var(--shadow-heavy);
}
.albumOverlay {
  width:100%;
  height:100%;
  position:absolute;
  background: rgb(255,255,255);
  background: linear-gradient(180deg, rgba(0,0,0,0) 41%, rgba(0,0,0,0.5) 100%);
  opacity: 0;
}
.albumOverlayActive {
  opacity: 1;
  border: 2px solid var(--primary-yellow);
}
.album-overlay-actions-contain {
  position: absolute;
  width: 100%;
  bottom: 0;
  right: 0;
  display: flex;
}
.album-overlay-more {
  opacity: 1;
  align-self: flex-end;
}
.album-overlay-favorite {
  opacity: 1;
  align-self: flex-start;
}
.album-overlay:hover, .album-overlay:focus {
  opacity:1;
}
.audioFavorite {
  padding-right: 1rem;
}
.audioMore {
  float: left;
}
</style>
