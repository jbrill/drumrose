<template>
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
        @click.native.stop.prevent
        v-on="on"
      >
        <v-icon
          small
          class="album-overlay-more"
        >
          mdi-dots-horizontal
        </v-icon>
      </v-btn>
    </template>
    <v-list dense>
      <v-list-item 
        :style="{
          'padding': '2px',
          'justify-content':'center'
        }"
      >
        <v-rating
          v-if="auth.loggedIn"
          background-color="white"
          color="var(--primary-purple)"
          dense
          half-increments
          hover
          size="18"
          @input="changeRating($event)"
          @click.native.stop.prevent
        />
        <v-btn
          v-else
          block
          raised
          @click="$auth.loginWith('auth0')"
          @click.native.stop.prevent
        >
          Log In
        </v-btn>
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
</template>

<script>
import { mapState } from 'vuex';
import {
  favoriteTrack,
  favoriteAlbum,
  favoritePlaylist,
  reviewTrack,
  reviewAlbum,
  reviewPlaylist,
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
    name: {
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
    isFavorited: {
      type: Boolean,
      default: false,
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
      console.log("HI")
      const data = {
        'rating': e,
        'apple_music_id': this.id,
      };
      console.log(this.type)
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
      this.isPlaying = false;
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
        } catch (err) {
          console.error(err);
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
        } catch (err) {
          console.error(err);
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
          this.isFavorited = true;
        } catch (err) {
          console.error(err);
        }
      }
    },
    async unFavoriteItem () {
      if (this.type == 'song') {
        try {
          await favoriteTrack(
            this.$auth.getToken('auth0'),
            {
              "apple_music_id": this.id,
            },
          );
          this.isFavorited = true;
        } catch (err) {
          console.error(err);
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
        } catch (err) {
          console.error(err);
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
          this.isFavorited = true;
        } catch (err) {
          console.error(err);
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
  },
};
</script>

<style scoped>
.show-btns {
  color: rgba(255, 255, 255, 1) !important;
  display: flex;
}
</style>
