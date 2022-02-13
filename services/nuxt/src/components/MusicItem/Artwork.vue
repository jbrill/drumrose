<template>
  <div style="width: 100%" class="artworkContain">
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
                  v-if="
                    (
                      playbackState === 2 && !nowPlayingPlaylist && !nowPlayingAlbum && (
                        nowPlayingItem.id === id
                      )
                    ) || (
                      playbackState === 2 && nowPlayingAlbum && (
                        nowPlayingAlbum.id === id
                      )
                    ) || (
                      playbackState === 2 && (
                        nowPlayingPlaylist && nowPlayingPlaylist.id === id
                      )
                    )
                  "
                  :class="{ 'not-show-btns': !hover, 'show-btns': hover }"
                  :loading="playbackState === 6 || playbackState === 7 || playbackState === 9"
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
                  v-else-if="playbackState === 2"
                  :class="{ 'not-show-btns': !hover, 'show-btns': hover }"
                  :loading="playbackState === 6 || playbackState === 7 || playbackState === 9"
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
                <v-btn
                  v-else-if="playbackState === 3 || playbackState === 0"
                  :class="{ 'not-show-btns': !hover, 'show-btns': hover }"
                  :loading="playbackState === 6 || playbackState === 7 || playbackState === 9"
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
                <v-btn
                  v-else
                  :class="{ 'not-show-btns': !hover, 'show-btns': hover }"
                  fab
                  medium
                >
                  <v-icon
                    :class="{ 'show-btns': hover }"
                  >
                    mdi-pause
                  </v-icon>
                </v-btn>
              </v-row>
              <v-card-actions class="card-actions">
                <v-tooltip
                  v-if="!auth.loggedIn && isActionable"
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
                  <span>Log In To Favorite</span>
                </v-tooltip>
                <v-btn
                  v-else-if="!isFavorited && isActionable"
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
                <v-btn
                  v-else-if="isActionable"
                  icon
                  @click="unFavoriteItem()"
                  @click.native.stop.prevent
                >
                  <v-icon
                    small
                    color="red"
                  >
                    mdi-heart
                  </v-icon>
                </v-btn>
                <ActionMenu
                  v-if="isActionable"
                  :id="id"
                  :type="type"
                  :artwork-url="artworkUrl"
                  :name="name"
                  :artist-name="artistName"
                  :review="review"
                  :rating="rating"
                />
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
import ActionMenu from '~/components/MusicItem/ActionMenu.vue';
import {
  favoriteTrack,
  favoriteAlbum,
  favoritePlaylist,
  reviewTrack,
  reviewAlbum,
  reviewPlaylist,
  unFavoriteTrack,
  unFavoritePlaylist,
  unFavoriteAlbum,
} from '~/api/api';


export default {
  components: {
    ActionMenu,
  },
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
    name: {
      type: String,
      default: '',
    },
    artistName: {
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
    favorited: {
      type: Boolean,
      default: false,
    },
    rating: {
      type: Number,
      default: 0.0,
    },
    review: {
      type: String,
      default: "",
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
      isFavorited: this.favorited,
    };
  },
  computed: {
    ...mapState(
      [
        'auth',
        'isAuthorized',
        'nowPlayingItem',
        'playbackState',
        'nowPlayingPlaylist',
        'nowPlayingAlbum',
      ]
    ),
  },
  async created () {
    if (this.$store.state.isAuthorized) {
      try {
        let playlistResp = await this.$store.getters.fetch(
         '/v1/me/library/playlists'
        );
        this.playlists = playlistResp.data;
        // const librarySearchResp = await this.$store.dispatch(
        //   "searchLibrary",
        //   {
        //     'type': this.type,
        //     'searchInput': this.name,
        //   }
        // );
      } catch (err) {
        console.error(err);
      }
      
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
        'apple_music_id': this.id,
      };
      try {
        if (this.type === 'song') {
          await reviewTrack(
            this.$auth.getToken('auth0'), this.id, data
          );
        } else if (this.type === 'album') {
          await reviewAlbum(
            this.$auth.getToken('auth0'), this.id, data
          );
        } else if (this.type === 'playlist') {
          await reviewPlaylist(
            this.$auth.getToken('auth0'), this.id, data
          );
        }
      } catch (err) {
        console.error(err);
        this.$toast.error(err);
      }
    },
    async pauseTrack () {
      await this.$store.dispatch("pause");
    },
    async favoriteItem () {
      if (this.type == 'song') {
        try {
          await favoriteTrack(
            this.$auth.getToken('auth0'),
            {
              "apple_music_id": this.id,
            },
          );
          this.isFavorited = true;
          this.$toast.info('Favorited track');
        } catch (err) {
          console.error(err);
          this.$toast.error('Unable to favorite track');
        }
      }
      if (this.type == 'album') {
        try {
          await favoriteAlbum(
            this.$auth.getToken('auth0'),
            {
              "apple_music_id": this.id,
            },
          );
          this.isFavorited = true;
          this.$toast.info('Favorited album');
        } catch (err) {
          console.error(err);
          this.$toast.error('Unable to favorite album');
        }
      }
      if (this.type == 'playlist') {
        try {
          await favoritePlaylist(
            this.$auth.getToken('auth0'),
            {
              "apple_music_id": this.id,
            },
          );
          this.$toast.info('Favorited playlist');
          this.isFavorited = true;
        } catch (err) {
          console.error(err);
          this.$toast.error('Unable to favorite playlist');
        }
      }
    },
    async unFavoriteItem () {
      if (this.type == 'song') {
        try {
          await unFavoriteTrack(
            this.$auth.getToken('auth0'),
            this.id,
          );
          this.isFavorited = false;
          this.$toast.info('Unfavorited track');
        } catch (err) {
          console.error(err);
        }
      }
      if (this.type == 'album') {
        try {
          await unFavoriteAlbum(
            this.$auth.getToken('auth0'),
            this.id,
          );
          this.isFavorited = false;
          this.$toast.info('Unfavorited album');
        } catch (err) {
          console.error(err);
        }
      }
      if (this.type == 'playlist') {
        try {
          await unFavoritePlaylist(
            this.$auth.getToken('auth0'),
            this.id,
          );
          this.isFavorited = false;
          this.$toast.info('Unfavorited playlist');
        } catch (err) {
          console.error(err);
        }
      }
    },
    async login () {
      await this.$auth.loginWith('auth0');
    },
    async playTrack () {
      console.log(this.id)
      if (this.type == 'song') {
        await this.$store.dispatch(
          "setQueue", { 'song': this.id }
        );
        await this.$store.dispatch(
          "setNowPlayingPlaylist", null
        );
        await this.$store.dispatch(
          "setNowPlayingAlbum", null
        );
      }
      if (this.type == 'playlist') {
        await this.$store.dispatch(
          "setQueue", { 'playlist': this.id }
        );
        await this.$store.dispatch(
          "setQueue", { 'playlist': this.id }
        );
        await this.$store.dispatch(
          "setNowPlayingPlaylist", { 'id': this.id }
        );
        await this.$store.dispatch(
          "setNowPlayingAlbum", null
        );
      }
      if (this.type == 'album') {
        await this.$store.dispatch(
          "setQueue", { 'album': this.id }
        );
        await this.$store.dispatch(
          "setNowPlayingPlaylist", null
        );
        await this.$store.dispatch(
          "setNowPlayingAlbum", { 'id': this.id }
        );
      }
      try {
        await this.$store.dispatch("play");
      } catch (err) {
        this.$toast.error('Unable to play');
      }
      if (!this.$store.state.isAuthorized) {
        this.$toast.global.apple_login();
      }
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
  border-radius: 1px;
  outline: 1px solid var(--primary-purple);
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

  /* min-height: 18vh; */
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
  border: 1px solid var(--primary-yellow);
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
