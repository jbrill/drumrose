<template>
  <div :class="nowPlaying ? 'nowPlayingContain' : 'queueItemContain'">
    <div v-if="trackObject" class="musicItem">
      <v-img
        :src="appleImage"
        class="audio-player-artwork"
        height="30px"
        width="30px"
        max-width="30px"
      />
      <div class="nowPlayingItem">
        <nuxt-link
          class="nowPlayingItemLink songName"
          :to="'/tracks/' + trackObject.id"
        >
          {{ trackObject.attributes.name }}
        </nuxt-link>
        <nuxt-link
          class="nowPlayingItemLink artistName"
          :to="'/artists/'"
        >
          {{ trackObject.attributes.artistName }}
        </nuxt-link>
      </div>
    </div>
    <div class="nowPlayingActions">
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
        v-if="!nowPlaying"
        class="moreButton"
        x-small
      >
        mdi-dots-horizontal
      </v-icon>
    </div>
  </div>
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
      artist_page_id: '',
      track_page_id: '',
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
  created () {
    console.log("this.trackObject")
    console.log(this.trackObject)
    /***getTrackDetail(
      this.$auth.getToken('auth0'),
      this.trackObject.id
    ).then( (resp) => {
      console.log(resp)
      this.track_page_id = resp.data.track_detail.page_id;
    }).catch( (err) => {
      this.$sentry.captureException(err);
      console.error(err);
    });***/
  },
  methods: {
    favoriteTrack () {
      postFavorite(
        this.$auth.getToken('auth0'),
        { 'type': this.trackObject.type, 'id': this.trackObject.id }
      ).then( () => {
        // set favorite color
        this.isFavorited = true;
      }).catch ( err => {
        console.error(err);
        this.$sentry.captureException(err);
        });
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
  color: white;
}
.songName {
  font-size: 0.6rem;
  color: #ccc;
}
.nowPlayingItemLink:hover, .nowPlayingItemLink:focus {
  color: white;
}
</style>
