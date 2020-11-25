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
                    <v-dialog
                      v-model="dialog"
                      scrollable
                      max-width="50vw"
                    >
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
                      <v-card
                        style="
                          opacity: 1; padding: 2rem
                        "
                      >
                        <v-tabs
                          v-model="tab"
                          color="var(--primary-yellow)"
                          centered
                        >
                          <v-tabs-slider />
                          <v-tab href="#tab-1">
                            Add to playlist
                          </v-tab>
                          <v-tab href="#tab-2">
                            Create a playlist
                          </v-tab>
                        </v-tabs>
                        <v-tabs-items v-model="tab">
                          <v-tab-item key="1" value="tab-1">
                            <v-responsive>
                              <v-list>
                                <v-list-item
                                  v-for="
                                    (playlist, playlistIdx) in playlists
                                  "
                                  :key="
                                    'playlist' + playlistIdx
                                  "
                                >
                                  <v-list-item-avatar>
                                    <v-img
                                      v-if="'artwork' in playlist.attributes"
                                      :src="appleImage(playlist)"
                                      dark
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
                                  </v-list-item-avatar>
                                  <v-list-item-content>
                                    <v-list-item-title>
                                      <nuxt-link
                                        :to="
                                          '/library-playlists/' + playlist.id
                                        "
                                        style="color: white"
                                      >
                                        {{ playlist.attributes.name }}
                                      </nuxt-link>
                                    </v-list-item-title>
                                    <v-list-item-subtitle>
                                      {{
                                        playlist.attributes.dateAdded.split(
                                          '-'
                                        )[0]
                                      }}
                                    </v-list-item-subtitle>
                                  </v-list-item-content>
                                  <v-list-item-action>
                                    <v-btn
                                      :disabled="!playlist.attributes.canEdit"
                                      x-small
                                    >
                                      Add to playlist
                                    </v-btn>
                                  </v-list-item-action>
                                </v-list-item>
                              </v-list>
                            </v-responsive>
                          </v-tab-item>
                          <v-tab-item key="2" value="tab-2">
                            <v-responsive>
                              <v-container fluid>
                                <v-form>
                                  <v-text-field
                                    v-model="playlistName"
                                    :counter="10"
                                    :rules="playlistNameRules"
                                    label="Playlist Name"
                                    required
                                  />
                                  <v-text-field
                                    v-model="playlistDescription"
                                    label="Playlist Description"
                                  />
                                  <v-radio-group v-model="privacyRadio">
                                    <template v-slot:label>
                                      <div>Choose Your Privacy</div>
                                    </template>
                                    <v-radio value="Public">
                                      <template v-slot:label>
                                        <div>Public</div>
                                      </template>
                                    </v-radio>
                                    <v-radio value="Private">
                                      <template v-slot:label>
                                        <div>Private</div>
                                      </template>
                                    </v-radio>
                                  </v-radio-group>
                                  <v-btn
                                    :disabled="
                                      playlistName.length === 0 ||
                                        isCreatingPlaylist ||
                                        playlistName.length > 10
                                    "
                                    color="var(--primary-purple)"
                                    @click="createPlaylist"
                                  >
                                    Create Playlist
                                  </v-btn>
                                </v-form>
                              </v-container>
                            </v-responsive>
                          </v-tab-item>
                        </v-tabs-items>
                      </v-card>
                    </v-dialog>
                    <v-divider />
                    <v-list-item
                      :disabled="!isAuthorized"
                      @click.native.stop.prevent
                      @click="moreLikeThis"
                    >
                      <v-list-item-icon>
                        <v-icon small :disabled="!isAuthorized">
                          mdi-thumb-up
                        </v-icon>
                      </v-list-item-icon>
                      <v-list-item-content>
                        <v-list-item-title>More like this</v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                    <v-divider />
                    <v-tooltip
                      v-if="!isAuthorized"
                      top
                    >
                      <template v-slot:activator="{ on }">
                        <v-list-item
                          disabled
                          v-on="on"
                          @click.native.stop.prevent
                          @click="lessLikeThis"
                        >
                          <v-list-item-icon>
                            <v-icon small disabled>
                              mdi-thumb-down
                            </v-icon>
                          </v-list-item-icon>
                          <v-list-item-content>
                            <v-list-item-title>
                              Less like this
                            </v-list-item-title>
                          </v-list-item-content>
                        </v-list-item>
                      </template>
                      <span>Sign In To Apple Music</span>
                    </v-tooltip>
                    <v-list-item
                      v-else
                      @click.native.stop.prevent
                      @click="lessLikeThis"
                    >
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
                    <v-list-item
                      @click.native.stop.prevent
                      @click="addToQueue"
                    >
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
                        <v-list-item-title>
                          Add to library
                        </v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                    <v-list-item
                      @click.native.stop.prevent
                      @click="
                        shareLink()
                      "
                    >
                      <v-list-item-icon>
                        <v-icon small>
                          mdi-share
                        </v-icon>
                      </v-list-item-icon>
                      <v-list-item-content>
                        <v-list-item-title>Share</v-list-item-title>
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
  favoriteAlbum,
  favoritePlaylist,
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
    tracks: {
      type: Array,
      default: () => [],
    },
    link: {
      type: String,
      default: '',
    },
  },
  data () {
    return {
      tab: null,
      isHovering: false,
      isPlaying: false,
      isCreatingPlaylist: false,
      dialog: false,
      playlists: [],
      playlistDescription: '',
      playlistName: '',
      playlistNameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 10) || 'Name must be less than 10 characters',
      ],
      privacyRadio: 'Public',
      itemInUserLibrary: false,
    };
  },
  computed: {
    ...mapState(['auth', 'isAuthorized', 'nowPlayingItem', 'playbackState']),
  },
  async created () {
    if (this.$store.state.isAuthorized) {
      let playlistResp = await this.$store.getters.fetch(
        '/v1/me/library/playlists'
      );
      this.playlists = playlistResp.data;
      let isInLibraryResponse = await this.$store.getters.fetch(
        '/v1/me/library/search'
      );
      isInLibraryResponse.data;
    }
  },
  methods: {
    appleImage (playlist) {
      return playlist.attributes.artwork.url.replace(
        '{w}', playlist.attributes.artwork.width || '300'
      ).replace(
        '{h}', playlist.attributes.artwork.height || '300'
      );
    },
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
        this.$toast.success("Added to library");
      } catch(err) {
        console.error(err);
        this.$toast.error(err);
      }
    },
		async addToPlaylist (name, items) {
      await this.$store.dispatch("addToPlaylist", {
        "name": name,
        "items": items,
      });
    },
    async createPlaylist () {
      let name = this.playlistName;
      try {
        await this.$store.dispatch("newPlaylist", {
          "name": name,
          "description": this.playlistDescription,
          "tracks": this.tracks,
        });
        this.$toast.success("Created playlist");
      } catch (err) {
        console.error(err);
        this.$toast.error("Failed to create playlist");
      }
    },
    async changeRating (e) {
      const data = {
        'rating': e,
        'type': this.type,
        'id': this.id,
      };
      try {
        await postReview(
          this.$auth.getToken('auth0'), data
        );
      } catch (err) {
        console.error(err);
        this.$toast.error(err);
      }
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
      if (this.type == 'album') {
        try {
          await favoriteAlbum(this.id);
        } catch (err) {
          this.$toast.error(err.message);
        }
      }
      if (this.type == 'playlist') {
        try {
          await favoritePlaylist(this.id);
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
    shareLink () {
      let dummy = document.createElement('input');
      const text = process.env.baseUrl + this.link;

      document.body.appendChild(dummy);
      dummy.value = text;
      dummy.select();
      document.execCommand('copy');
      document.body.removeChild(dummy);
      this.$toast.success('Copied link to clipboard');
    },
    async moreLikeThis () {
      try {
        await this.$store.dispatch("love", {
          'id': this.id, 'type': this.type,
        });
        this.$toast.success(
          "More like this will be recommended."
        );
      } catch (err) {
        this.$toast.error('Unable to recommend more like this.');
        console.error(err);
      }
    },
    async lessLikeThis () {
      try {
        await this.$store.dispatch("dislike", {
          'id': this.id, 'type': this.type,
        });
        this.$toast.success(
          "Less like this will be recommended."
        );
      } catch (err) {
        this.$toast.error('Unable to recommend less like this.');
        console.error(err);
      }
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
  min-height: 18vh;
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
