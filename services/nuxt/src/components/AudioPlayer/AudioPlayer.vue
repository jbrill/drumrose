<template>
  <div v-if="playbackTime" class="audioPlayer">
    <div class="musicControls">
      <v-icon
        ref="musicPrev"
        @click="prevMusic"
      >mdi-skip-previous</v-icon>
      <v-icon
        v-if="playbackState === 3"
        @click="playTrack"
      >mdi-play</v-icon>
      <v-icon
        v-else
        @click="pauseTrack"
      >mdi-pause</v-icon>
      <v-icon
        ref="musicNext"
        @click="nextMusic"
      >mdi-skip-next</v-icon>
      <v-icon
        small
        @click="shuffleTrack"
      >mdi-shuffle</v-icon>
      <v-icon
        small
        v-if="$store.state.repeatMode === 1"
        @click="repeatTrack"
        color="var(--primary-red)"
      >mdi-repeat-once</v-icon>
      <v-icon
        small
        v-else-if="$store.state.repeatMode === 2"
        @click="repeatTrack"
        color="var(--primary-red)"
      >mdi-repeat</v-icon>
      <v-icon
        small
        v-else
        @click="repeatTrack"
      >mdi-repeat-off</v-icon>
    </div>
    <PostTimeline />
    <div class="volumeControls">
      <VolumeSlider />
    </div>
    <div
      class="nowPlayingContain"
    >
      <div v-if="nowPlayingItem" class="audio-player-artwork">
        <span
          :style="{
            backgroundImage:
              'url(' + nowPlayingItem.attributes.artwork.url + ')',
            backgroundSize: 'cover'
          }"
        />
      </div>
      <div v-else class="audio-player-artwork">
        <v-icon>mdi-person
        </v-icon>
      </div>
      <div v-if="nowPlayingItem" class="nowPlayingItem">
        <span ref="songName">
          <v-btn dark text x-small nuxt to="/">{{ nowPlayingItem.attributes.name }}</v-btn>
        </span>
        <span ref="trackArtist">
          <v-btn dark text x-small nuxt to="/">{{ nowPlayingItem.attributes.artistName }}</v-btn>
        </span>
      </div>
      <div v-else>
        <span ref="trackArtist">
          Artist
        </span>
        <span ref="songName">
          Track
        </span>
      </div>
      <v-icon
        @click="favoriteTrack"
        small
      >mdi-heart</v-icon>
      <v-icon
        small
        @click="showQueue"
      >queue_music</v-icon>
    </div>
  </div>
</template>

<script>
import PostTimeline from "~/components/PostTimeline";
import VolumeSlider from "~/components/AudioPlayer/VolumeSlider.vue";

import { postFavorite, getTrackInfo } from "~/api/api";

import { mapState } from "vuex";


export default {
  components: {
    PostTimeline,
    VolumeSlider
  },
  data () {
    return {
    }
  },
  computed: {
    ...mapState(['nowPlayingItem', 'queue', 'playbackState', 'playbackTime']),
    isFavorited () {
      const favorited = this.$refs.songName;
      if (element.offsetWidth < element.scrollWidth) {
        return true;
      }
      return false;
    },
  },
  methods: {
    playTrack () {
      this.$store.dispatch("play");
    },
    pauseTrack () {
      this.$store.dispatch("pause");
    },
    prevMusic () {
      this.$store.dispatch("previous");
    },
    nextMusic () {
      this.$store.dispatch("next")
    },
    moreMusic () {
      console.log('MORE...');
    },
    repeatTrack () {
      this.$store.dispatch("toggleRepeatMode");
    },
    shuffleTrack () {
      this.$store.dispatch("toggleShuffleMode");
    },
    changeVolume () {
      console.log("VOLUME");
    },
    showQueue () {
      console.log("queueueue");
    },
    async favoriteTrack () {
      console.log("favorite");
      if (this.$auth.loggedIn) {
        await postFavorite(this.$auth.getToken('auth0'), { 'type': this.nowPlayingItem.type, 'id': this.nowPlayingItem.id });
        
      }
    },
  },
	watch: {
    count (newCount, oldCount) {
      // Our fancy notification (2).
      console.log(`We have ${newCount} fruits now, yay!`)
    }
  }
};
</script>

<style scoped>
.audioPlayer {
  padding-left: 10vw;
  padding-right: 10vw;
  width: 100%;
  height: 3rem;
  background: linear-gradient(
    0deg,
    rgba(0, 0, 0, 1) 0%,
    rgba(25, 25, 25, 1) 100%
  );
  position: fixed;
  bottom: 0;
  z-index: 1;
  display: flex;
}
.volumeControls {
  width: 5%;
  display: flex;
  align-items: center;
  justify-content: center;
}
>>>.volume-slider i {
  font-size: 1rem;
}
>>>.volume-slider .v-messages {
  display: none;
}
>>>.playModeActive {
  color: var(--primary-red) !important;
}
.nowPlayingContain {
  width: 35%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.nowPlayingItem {
  width: 75%;
  display: flex;
  justify-content: center;
	flex-direction: column;
}

.audio-play__contain i {
  color: white;
  padding-top: 2.5px; /* slight nudge down */
  vertical-align: middle;
  margin: 0;
}
@media screen and (prefers-color-scheme: dark) {
  .audio-play__contain i {
    color: white;
  }
  .audio-play:hover, .audio-play:focus {
    color: var(--primary-yellow);
  }
  .audio-play__previous:hover,
  .audio-play__next:hover,
  .audio-play__previous:focus,
  .audio-play__next:focus {
    color: var(--primary-red);
  }
  .audio-player__track-info {
    color: white;
  }
  .audio-player__track-info__track-name:hover,
  .audio-player__track-info__track-name:focus {
    color: white;
  }
  .audio-player__track-info__track-artist:hover,
  .audio-player__track-info__track-artist:focus {
    color: white;
  }
  .audio-player__more-btn {
    color: white;
  }
  .audio-player__more-btn:hover, .audio-player__more-btn:focus {
    color: white;
  }
}
.audio-player-artwork {
  width: 30px;
  height: 30px;
  align-self: center;
  margin: 0.5rem;
}
.audio-player-artwork span {
  width: 30px;
  height: 30px;
  display: block;
}
.audio-player-artwork:hover, .audio-player-artwork:focus {
  cursor: pointer;
}
.audio-player__more-btn {
  right: 1rem;
  color: white;
}
.audio-player__more-btn:hover,
.audio-player__more-btn:focus {
  color: var(--primary-yellow);
}
.musicControls {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 20%;
}
>>>.musicControls button {
  padding: 5px;
}
.musicNavigationControls {
  display: flex;
  align-items: center;
  padding: 1rem;
}
.musicNavigationControls i {
  color: white;
  font-size: 1rem;
}
.volume-button {
  color: white;
  align-self: center;
  margin: 0 auto;
}
.volume-button:hover, .volume-button:focus {
  color: var(--primary-yellow);
}
.queue-button {
  color: white;
  align-self: center;
  margin: 0 auto;
}
.queue-button:hover, .queue-button:focus {
  color: var(--primary-yellow);
}
.favorite-button {
  color: white;
  align-self: center;
  margin: 0 auto;
  font-size: 0.9rem;
}
.favorite-button:hover, .favorite-button:focus {
  color: var(--primary-red);
}
</style>
