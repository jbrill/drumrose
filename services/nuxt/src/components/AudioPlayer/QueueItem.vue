<template>
  <v-layout
    flex
    justify-content-space-between
    :class="nowPlaying ? 'nowPlayingContain' : 'queueItemContain'"
    @mouseover="isHovering = true"
    @mouseleave="checkMenuHover"
  >
    <div v-if="trackObject" class="musicItem">
      <v-img
        style="margin: 0 auto"
        width="30px"
        height="30px"
        max-width="30px"
        :src="appleImage"
        gradient="to top right, rgba(100,115,201,.0), rgba(25,32,72,.34)"
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
      <div v-if="artistId" class="nowPlayingItem">
        <nuxt-link
          v-if="artistId"
          class="nowPlayingItemLink artistName overline"
          :to="'/artists/' + artistId"
        >
          {{ trackObject.attributes.artistName }}
        </nuxt-link>
        <span
          v-else
          class="overline"
        />
        <nuxt-link
          class="nowPlayingItemLink songName"
          :to="'/tracks/' + trackObject.id"
        >
          {{ trackObject.attributes.name }}
        </nuxt-link>
      </div>
    </div>
    <v-row
      v-if="isHovering || nowPlaying"
      justify="end"  
    >
      <v-btn icon>
        <v-icon
          v-if="isFavorited"
          x-small
          color="red"
          @click="unFavoriteTrack"
        >
          mdi-heart
        </v-icon>
        <v-icon
          v-else-if="auth.loggedIn"
          x-small
          @click="favoriteTrack"
          @click.stop.prevent
        >
          mdi-heart
        </v-icon>
        <v-tooltip
          v-else
          top
        >
          <template v-slot:activator="{ on }">
            <div v-on="on">
              <v-hover v-slot:default="{ hover }">
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
              </v-hover>
            </div>
          </template>
          <span>Log In To Favorite</span>
        </v-tooltip>
      </v-btn>
      <ActionMenu />
    </v-row>
    <div v-else>
      <span class="overline">
        {{ formattedSeconds(trackObject.attributes.durationInMillis) }} min
      </span>
    </div>
  </v-layout>
</template>

<script>
import { mapState } from 'vuex';
import {
  getTrackDetail, favoriteTrack, createTrack,
} from '~/api/api';
import ActionMenu from '~/components/MusicItem/ActionMenu.vue';

export default {
  components: {
    ActionMenu,
  },
  props: {
    'trackObject': {
      type: Object,
      default: () => {},
    },
    'nowPlaying': {
      type: Boolean,
      default: false,
    },
  },
  data () {
    return {
      isFavorited: false,
      artistId: '',
      track_page_id: '',
      isHovering: false,
      moreModel: false,
      dialog: false,
      inLibrary: false,
    };
  },
  computed: {
		appleImage () {
      return this.trackObject.attributes.artwork.url.replace(
        '{w}', '250'
      ).replace(
        '{h}', '250'
      );
    },
    ...mapState([
      'auth', 'isAuthorized', 'nowPlayingItem', 'playbackState',
    ]),
  },
  async created () {
    try {
      const resp = await this.$store.getters.fetch(
        `/v1/catalog/us/songs/${this.trackObject.id}`
      );
      this.artistId = resp.data[0].relationships.artists.data[0].id;
      this.loading = false;
    } catch (err) {
      this.loading = false;
      console.error(err);
    }
    try {
      const resp = await getTrackDetail(
        this.$auth.getToken('auth0'),
        this.trackObject.id,
      );
      this.isFavorited = resp.data.track.favorited;
    } catch (err) {
      if (err.response.status === 409) {
        try {
          await createTrack(
            this.$auth.getToken('auth0'),
            {
              'id': this.trackObject.id,
            }
          );
        } catch (err) {
          console.error(err);
        }
      }
      this.loading = false;
      console.error(err);
    }
    
    // const librarySearchResp = await this.$store.dispatch(
    //   "searchLibrary",
    //   {
    //     'type': this.trackObject.type,
    //     'searchInput': this.trackObject.attributes.name,
    // //   }
    // ).then( () => {
    //   // set favorite
    //   this.inLibrary = true;
    // }).catch ( err => {
    //   console.error(err);
    //   this.$sentry.captureException(err);
    // });
  },
  async mounted () {
    
  },
  methods: {
    async favoriteTrack () {
      try {
        if (this.trackObject.type === 'songs') {
          await favoriteTrack(
            this.$auth.getToken('auth0'),
            {
              'apple_music_id': this.trackObject.id,
            },
          );
          this.isFavorited = true;
        }
        this.$toast.info('Favorited track');
      } catch (err) {
        console.error(err);
        this.$sentry.captureException(err);
      }
    },
    async unFavoriteTrack () {
      try {
        if (this.trackObject.type === 'song') {
          await favoriteTrack(
            this.$auth.getToken('auth0'),
            {
              'id': this.trackObject.id,
            }
          );
          this.isFavorited = true;
        }
      } catch (err) {
        console.error(err);
        this.$sentry.captureException(err);
      }
    },
    addToLibrary () {
      this.$store.dispatch(
        "addToLibrary",
        {
          'type': this.trackObject.type,
          'id': this.trackObject.id,
        }
      ).then( () => {
        // set favorite
        this.inLibrary = true;
      }).catch ( err => {
        console.error(err);
        this.$toast.error(err);
        this.$sentry.captureException(err);
      });
    },
    formattedSeconds (milliSeconds) {
      // eslint-disable-next-line
      return MusicKit.formattedMilliseconds(
        milliSeconds
      ).minutes;
    },
    changeRating () {
      console.log("CHANGE RATING");
    },
    showMore () {
      this.moreModel = true;
    },
    checkMenuHover () {
      if (this.moreModel) {
        return;
      }
      this.isHovering = false;
    },
    async addToQueue () {
      try {
         if (this.trackObject.type == 'songs') {
          await this.$store.dispatch(
            "playNext",
            {
              'song': this.trackObject.id,
            }
          );
        }
        if (this.trackObject.type == 'playlists') {
          await this.$store.dispatch(
            "playNext",
            {
              'playlist': this.trackObject.id,
            }
          );
        }
        if (this.trackObject.type == 'albums') {
          await this.$store.dispatch(
            "playNext",
            {
              'album': this.trackObject.id,
            }
          );
        }
        this.$toast.show(
          `Added ${this.trackObject.type} to queue`
        );
      } catch (err) {
        console.error(err);
        this.$toast.error(
          `Unable to add ${this.trackObject.type} to queue`
        );
      }
     
    },
  },
};
</script>

<style scoped>
.nowPlayingContain {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  width: 25vw;
}
.queueItemContain {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  min-width: 25vw;
}
.nowPlayingItem {
  display: flex;
  overflow: hidden;
  justify-content: center;
  flex-direction: column;
}
.nowPlayingActions {
  display: flex;
  align-items: center;
}
.musicItem {
  display: flex;
  align-items: center;
  max-width: 85%;
}
.favoriteButton {
  opacity: 0.8;
}
.favoriteButton:hover, .favoriteButton:focus {
  opacity: 1;
}
.nowPlayingItemLink {
  clear: both;
  display: inline-block;
  overflow: hidden;
  white-space: nowrap;
  padding-left: 1rem;
}
.artistName {
  font-size: 0.65rem;
  color: #f2f2f2;
}
.songName {
  font-size: 0.65rem;
  color: #f2f2f2;
  font-weight: bolder;
}
.nowPlayingItemLink:hover, .nowPlayingItemLink:focus {
  color: white;
}
</style>
