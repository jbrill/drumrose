<template>
  <v-layout
    flex
    justify-content-space-between
    :class="nowPlaying ? 'nowPlayingContain' : 'queueItemContain'"
    @mouseover="isHovering = true"
    @mouseleave="isHovering = false"
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
      >
        mdi-heart
      </v-icon>
      <v-icon
        class="moreButton"
        x-small
      >
        mdi-dots-horizontal
      </v-icon>
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
        this.$sentry.captureException(err);
      });
    },
    formattedSeconds (milliSeconds) {
      return MusicKit.formattedMilliseconds(
        milliSeconds
      ).minutes;
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
