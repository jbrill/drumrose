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
        :src="appleImage"
        class="audio-player-artwork"
        height="30px"
        width="30px"
        max-width="30px"
      />
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
    <div v-if="isHovering || nowPlaying">
      <v-icon
        v-if="isFavorited"
        x-small
        color="red"
        @click="favoriteTrack"
      >
        mdi-heart
      </v-icon>
      <v-icon
        v-else
        class="favoriteButton"
        x-small
        @click="favoriteTrack"
        @click.stop.prevent
      >
        mdi-heart
      </v-icon>
      <v-menu
        v-model="moreModel"
        left
        top
        dark
        :close-on-content-click="false"
        offset-y
        max-height="50vh"
        width="45vw"
        nudge-top="25vh"
        transition="slide-y-reverse-transition"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-icon
            class="moreButton"
            x-small
            v-bind="attrs"
            @click="showMore"
            v-on="on"
          >
            mdi-dots-horizontal
          </v-icon>
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
          <v-list-item>
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
          <v-list-item>
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
            v-if="!inLibrary"
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
          <v-list-item
            v-else
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
              <v-list-item-title>Remove from library</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-menu>
    </div>
    <div v-else>
      <span class="overline">
        {{ formattedSeconds(trackObject.attributes.durationInMillis) }} min
      </span>
    </div>
  </v-layout>
</template>

<script>
import { postFavorite } from '~/api/api';


export default {
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
  },
  methods: {
    favoriteTrack () {
      postFavorite(
        this.$auth.getToken('auth0'),
        { 'type': this.trackObject.type, 'id': this.trackObject.id }
      ).then( () => {
        // set favorite
        this.isFavorited = true;
      }).catch ( err => {
        console.error(err);
        this.$toast.error(err);
        this.$sentry.captureException(err);
      });
    },
    addToLibrary () {
      this.$store.dispatch(
        "addToLibrary",
        { 'type': this.trackObject.type, 'id': this.trackObject.id }
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
