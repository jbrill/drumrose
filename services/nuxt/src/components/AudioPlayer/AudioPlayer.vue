<template>
  <div style="z-index: 10" v-if="playbackTime" class="audioPlayer">
    <div class="musicControls">
      <v-btn
        icon
        ref="musicPrev"
        @click="prevMusic"
      >
        <v-icon>mdi-skip-previous</v-icon>
      </v-btn>
      <v-btn
        icon
        v-if="playbackState === 3"
        @click="playTrack"
      >
        <v-icon>mdi-play</v-icon>
      </v-btn>
      <v-btn
        icon
        v-else
        @click="pauseTrack"
      >
        <v-icon>mdi-pause</v-icon>
      </v-btn>
      <v-btn
        icon
        ref="musicNext"
        @click="nextMusic"
      >
        <v-icon>mdi-skip-next</v-icon>
      </v-btn>
      <v-btn
        icon
        small
        @click="shuffleTrack"
      >
        <v-icon x-small>mdi-shuffle</v-icon>
      </v-btn>
      <v-btn
        icon
        small
        v-if="$store.state.repeatMode === 1"
        @click="repeatTrack"
        color="var(--primary-red)"
      >
        <v-icon x-small>mdi-repeat-once</v-icon>
      </v-btn>
      <v-btn
        icon
        small
        v-else-if="$store.state.repeatMode === 2"
        @click="repeatTrack"
        color="var(--primary-red)"
      >
        <v-icon x-small>mdi-repeat</v-icon>
      </v-btn>
      <v-btn
        icon
        small
        v-else
        @click="repeatTrack"
      >
        <v-icon x-small>mdi-repeat-off</v-icon>
      </v-btn>
    </div>
    <PostTimeline />
    <VolumeSlider />
    <Queue />
  </div>
</template>

<script>
import PostTimeline from "~/components/AudioPlayer/PostTimeline";
import Queue from "~/components/AudioPlayer/Queue";
import VolumeSlider from "~/components/AudioPlayer/VolumeSlider";

import { postFavorite, getTrackInfo } from "~/api/api";

import { mapState } from "vuex";


export default {
  components: {
    PostTimeline,
    VolumeSlider,
    Queue,
  },
  computed: {
    ...mapState(['queue', 'playbackState', 'playbackTime']),
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
    repeatTrack () {
      this.$store.dispatch("toggleRepeatMode");
    },
    shuffleTrack () {
      this.$store.dispatch("toggleShuffleMode");
    },
    changeVolume () {
      console.log("VOLUME");
    },
  },
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
>>>.v-icon {
  opacity: 0.8;
  font-size: 1rem;
}
>>>.v-icon:hover, >>>.v-icon:focus {
  opacity: 1;
}
</style>
