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
            :src="artworkUrl"
          >
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
                  color="var(--primary-purple)"
                  @click.native="pauseTrack"
                >
                  <v-icon
                    :class="{ 'show-btns': hover }"
                    color="transparent"
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
                  color="var(--primary-purple)"
                  @click.native="playTrack"
                >
                  <v-icon
                    :class="{ 'show-btns': hover }"
                    color="transparent"
                  >
                    mdi-play
                  </v-icon>
                </v-btn>
              </v-row>
              <v-card-actions class="card-actions">
                <v-btn
                  icon
                  :class="{ 'show-btns': hover }"
                  @click="auth.loggedIn ? favoriteItem() : login()"
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
                  origin="bottom right"
                  z-index="100"
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
                      @click.native.stop.prevent
                      @click="addToPlaylist"
                    >
                      <v-list-item-icon>
                        <v-icon>mdi-playlist-music</v-icon>
                      </v-list-item-icon>
                      <v-list-item-content>
                        <v-list-item-title>Add to playlist</v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                    <v-divider />
                    <v-list-item @click.native.stop.prevent @click="addToQueue">
                      <v-list-item-icon>
                        <v-icon>mdi-playlist-star</v-icon>
                      </v-list-item-icon>
                      <v-list-item-content>
                        <v-list-item-title>Add to queue</v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                    <v-divider />
                    <v-list-item
                      @click.native.stop.prevent
                      @click="
                        (isAuthorized || auth.loggedIn) ? 
                          addToLibrary() : login()
                      "
                    >
                      <v-list-item-icon>
                        <v-icon>mdi-library</v-icon>
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
import { favoriteTrack } from '~/api/api';

export default {
  props: {
    id: {
      type: String,
      default: '',
    },
    link: {
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
  },
  data () {
    return {
      isHovering: false,
      isPlaying: false,
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
    },
		addToLibrary: function () {
      this.$store.dispatch("setQueue", { "playlist": this.id });
    },
		addToPlaylist: function () {
      this.$store.dispatch("setQueue", { "playlist": this.id });
    },
    pauseTrack: async function () {
      await this.$store.dispatch("pause");
      this.isPlaying = false;
    },
    favoriteItem: async function (event) {
      await favoriteTrack(this.appleMusicId);
    },
    async login () {
      await this.$auth.loginWith('auth0');
    },
    playTrack: async function () {
      if (this.nowPlayingItem) {
        if (this.nowPlayingItem.id !== this.id) {
          if (this.type == 'song') {
            await this.$store.dispatch("setQueue", { 'song': this.id });
          }
          if (this.type == 'playlist') {
            await this.$store.dispatch("setQueue", { 'playlist': this.id });
          }
          if (this.type == 'album') {
            await this.$store.dispatch("setQueue", { 'album': this.id });
          }
        }
      } else {
        if (this.type == 'song') {
          await this.$store.dispatch("setQueue", { 'song': this.id });
        }
        if (this.type == 'playlist') {
          await this.$store.dispatch("setQueue", { 'playlist': this.id });
        }
        if (this.type == 'album') {
          await this.$store.dispatch("setQueue", { 'album': this.id });
        }
      }
      await this.$store.dispatch("play");
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
  border-radius: 1px;
  box-shadow: var(--shadow-medium);
}
.albumContain:hover, .albumContain:focus {
  cursor: pointer;
}
.albumCover {
  width: 100%;
  overflow: visible !important;
  height: auto;
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
  border-radius: 2px;
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
