<template>
  <v-menu
    close-on-content-click
    origin="bottom right"
    z-index="1000"
    attach
    top
    left
    dark
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
              v-model="reviewRating"
              background-color="grey"
              color="var(--primary-purple)"
              dense
              readonly
              half-increments
              hover
              size="18"
              @click="changeRating"
            />
          </v-list-item>
        </template>
        <span>Log In To Rate</span>
      </v-tooltip>
      <v-list-item
        v-else
        :style="{
          'justify-content':'center',
          'align-items': 'center',
          'height': '1rem'
        }"
      >
        <v-rating
          v-model="reviewRating"
          background-color="white"
          color="var(--primary-purple)"
          dense
          half-increments
          hover
          size="18"
        />
      </v-list-item>
      <v-tooltip
        v-if="!auth.loggedIn"
        top
      >
        <template v-slot:activator="{ on }">
          <v-list-item
            v-on="on"
            @click.native.stop.prevent
          >
            <v-list-item-icon>
              <v-icon small color="grey">
                mdi-pencil
              </v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title class="grey--text">
                Write a Review
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
        <span>Log In To Review</span>
      </v-tooltip>
      <v-dialog
        v-else
        v-model="reviewDialog"
        scrollable
        max-width="50vw"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-list-item
            v-bind="attrs"
            v-on="on"
            @click.native.stop.prevent
            @click="writeReview"
          >
            <v-list-item-icon>
              <v-icon small>
                mdi-pencil
              </v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title v-if="review && review.length > 0">
                Edit Review
              </v-list-item-title>
              <v-list-item-title v-else>
                Write a Review
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
            <v-tab href="#review-tab-1">
              Write Review
            </v-tab>
          </v-tabs>
          <v-tabs-items v-model="reviewTab">
            <v-tab-item key="1" value="review-tab-1">
              <v-responsive>
                <v-container fluid>
                  <v-form>
                    <v-card rounded>
                      <v-layout>
                        <v-img
                          class="albumCover"
                          width="30%"
                          elevation="12"
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
                        </v-img>
                        <v-container
                          style="
                            display: flex;
                            justify-content: center;
                            flex-direction: column
                          "
                        >
                          <v-card-title class="title" style="padding-bottom: 0">
                            {{ name }}
                          </v-card-title>
                          <v-card-title class="subtitle">
                            {{ artistName }}
                          </v-card-title>
                        </v-container>
                        <v-card-actions>
                          <v-rating
                            background-color="white"
                            color="var(--primary-purple)"
                            dense
                            half-increments
                            hover
                            size="24"
                            @input="reviewRating = $event"
                          />
                        </v-card-actions>
                      </v-layout>
                    </v-card>
                    <v-container>
                      <p
                        class="caption yellow--text overline"
                        style="margin-top: 1vh"
                      >
                        Review
                      </p>
                      {{ reviewRating }}
                      <v-textarea
                        v-if="review"
                        v-model="reviewDescription"
                        :rules="reviewDescriptionRules"
                        label="Edit review"
                      />
                      <v-textarea
                        v-else
                        v-model="reviewDescription"
                        :rules="reviewDescriptionRules"
                        label="Add a review"
                      />
                      <v-btn
                        v-if="review || rating"
                        :disabled="
                          (
                            (
                              reviewDescription &&
                              reviewDescription.length === 0
                            ) ||
                            isCreatingReview ||
                            (
                              reviewDescription &&
                              reviewDescription.length > 255
                            )
                          ) ||
                            (
                              review === reviewDescription &&
                              reviewRating === rating
                            )
                        "
                        color="var(--primary-purple)"
                        @click="editReview"
                      >
                        Update Review
                      </v-btn>
                      <v-btn
                        v-else
                        :disabled="
                          (
                            reviewDescription &&
                            reviewDescription.length === 0
                          ) ||
                            isCreatingReview ||
                            (
                              reviewDescription &&
                              reviewDescription.length > 255
                            )
                        "
                        color="var(--primary-purple)"
                        @click="createReview"
                      >
                        Create Review
                      </v-btn>
                    </v-container>
                  </v-form>
                </v-container>
              </v-responsive>
            </v-tab-item>
          </v-tabs-items>
        </v-card>
      </v-dialog>
      <v-divider />
      <v-tooltip
        v-if="!auth.loggedIn"
        top
      >
        <template v-slot:activator="{ on }">
          <v-list-item
            v-on="on"
            @click.native.stop.prevent
          >
            <v-list-item-icon>
              <v-icon small color="grey">
                mdi-playlist-music
              </v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title class="grey--text">
                Add to Playlist
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
        <span>Log In To Add Or Create Playlist</span>
      </v-tooltip>
      <v-dialog
        v-else
        v-model="playlistDialog"
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
  reviewTrack,
  reviewAlbum,
  reviewPlaylist,
  updateTrackReview,
} from '~/api/api';


export default {
  components: {},
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
      reviewTab: 'review-tab-1',
      isHovering: false,
      isPlaying: false,
      isCreatingPlaylist: false,
      isCreatingReview: false,
      reviewDialog: false,
      reviewDescription: this.review,
      reviewDescriptionRules: [
        v => !!v || 'Review is required',
        v => (
          v && v.length <= 255
        ) || 'Review must be less than 255 characters',
      ],
      reviewRating: this.rating,
      playlistDialog: false,
      playlists: [],
      playlistDescription: '',
      playlistName: '',
      playlistNameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 10) || 'Name must be less than 10 characters',
      ],
      privacyRadio: 'Public',
      itemInUserLibrary: false,
      isReviewed: false,
      loading: true,
    };
  },
  computed: {
    ...mapState(['auth', 'isAuthorized', 'nowPlayingItem', 'playbackState']),
  },
  async mounted () {
    this.loading = true;
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
        this.loading = false;
      } catch (err) {
        console.error(err);
        this.loading = false;
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
        await this.$store.dispatch("playLater", {
          'song': this.id,
        });
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
        this.$toast.success('Created playlist');
      } catch (err) {
        console.error(err);
        this.$toast.error('Failed to create playlist');
      }
    },
    async changeRating (e) {
      console.log(this.id);
      const data = {
        'rating': e,
        'apple_music_id': this.id,
      };
      try {
        if (this.type === 'song') {
          await reviewTrack(
            this.$auth.getToken('auth0'), data
          );
        } else if (this.type === 'album') {
          await reviewAlbum(
            this.$auth.getToken('auth0'), data
          );
        } else if (this.type === 'playlist') {
          await reviewPlaylist(
            this.$auth.getToken('auth0'), data
          );
        }
      } catch (err) {
        console.error(err);
        this.$toast.error(err);
      }
    },
    async createReview () {
      const data = {
        'rating': this.reviewRating,
        'review': this.reviewDescription,
        'apple_music_id': this.id,
      };
      console.log(this.id);
      try {
        if (this.type === 'song') {
          await reviewTrack(
            this.$auth.getToken('auth0'), data
          );
        } else if (this.type === 'album') {
          await reviewAlbum(
            this.$auth.getToken('auth0'), data
          );
        } else if (this.type === 'playlist') {
          await reviewPlaylist(
            this.$auth.getToken('auth0'), data
          );
        }
        this.$toast.info(
          `Successfully reviewed ${this.type}`
        );
      } catch (err) {
        console.error(err);
        this.$toast.error(err);
      }
    },
    async editReview () {
      const data = {
        'rating': this.reviewRating,
        'review': this.reviewDescription,
        'apple_music_id': this.id,
      };
      console.log(this.id);
      try {
        if (this.type === 'song') {
          await updateTrackReview(
            this.$auth.getToken('auth0'), data
          );
        } else if (this.type === 'album') {
          await updateTrackReview(
            this.$auth.getToken('auth0'), data
          );
        } else if (this.type === 'playlist') {
          await updateTrackReview(
            this.$auth.getToken('auth0'), data
          );
        }
        this.$toast.info(
          `Successfully reviewed ${this.type}`
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
    async writeReview () {
      
    },
    shareLink () {
      let dummy = document.createElement('input');
      const text = process.env.baseUrl + this.link;

      document.body.appendChild(dummy);
      dummy.value = text;
      dummy.select();
      document.execCommand('copy');
      document.body.removeChild(dummy);
      this.$toast.info('Copied link to clipboard', {
        closeButton: true,
      });
    },
  },
};
</script>

<style scoped>
.show-btns {
  color: rgba(255, 255, 255, 1) !important;
  display: flex;
}

/* .v-btn__content {
  width: 100%; white-space: normal;
} */
>>.v-list-item--dense {
  min-height: 0;
}
</style>
