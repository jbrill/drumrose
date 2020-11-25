<template>
  <v-system-bar
    v-if="playbackTime"
    :height="height"
    style="z-index: 10"
    class="audioPlayer"
  >
    <v-container v-if="height === '250vh'">
      <v-flex id="p5Canvas" />
    </v-container>
    <div class="musicControls">
      <v-btn
        ref="musicPrev"
        icon
        @click="prevMusic"
      >
        <v-icon>mdi-skip-previous</v-icon>
      </v-btn>
      <v-btn
        v-if="playbackState === 3"
        icon
        @click="playTrack"
      >
        <v-icon>mdi-play</v-icon>
      </v-btn>
      <v-btn
        v-else
        icon
        @click="pauseTrack"
      >
        <v-icon>mdi-pause</v-icon>
      </v-btn>
      <v-btn
        ref="musicNext"
        icon
        @click="nextMusic"
      >
        <v-icon>mdi-skip-next</v-icon>
      </v-btn>
      <v-btn
        icon
        small
        @click="shuffleTrack"
      >
        <v-icon x-small>
          mdi-shuffle
        </v-icon>
      </v-btn>
      <v-btn
        v-if="$store.state.repeatMode === 1"
        icon
        small
        color="var(--primary-red) !important"
        @click="repeatTrack"
      >
        <v-icon x-small>
          mdi-repeat-once
        </v-icon>
      </v-btn>
      <v-btn
        v-else-if="$store.state.repeatMode === 2"
        icon
        small
        color="var(--primary-red) !important"
        @click="repeatTrack"
      >
        <v-icon x-small>
          mdi-repeat
        </v-icon>
      </v-btn>
      <v-btn
        v-else
        icon
        small
        @click="repeatTrack"
      >
        <v-icon x-small>
          mdi-repeat-off
        </v-icon>
      </v-btn>
    </div>
    <PostTimeline />
    <VolumeSlider />
    <v-spacer />
    <Queue />
  </v-system-bar>
</template>

<script>
import { mapState } from "vuex";
import PostTimeline from "~/components/AudioPlayer/PostTimeline";
import Queue from "~/components/AudioPlayer/Queue";
import VolumeSlider from "~/components/AudioPlayer/VolumeSlider";


export default {
  components: {
    PostTimeline,
    VolumeSlider,
    Queue,
  },
  data () {
    return {
      height: "50vh",
    };
  },
  computed: {
    ...mapState(['queue', 'playbackState', 'playbackTime']),
  },
  created () {
    if (process.browser) {
      window.addEventListener('keydown', e => {
        console.log(e)
        if (e.keyCode === 32 && this.playbackTime) {
          e.preventDefault();
          console.log(this.playbackState)
          if (this.playbackState === 3) {
            this.playTrack();
          } else {
            this.pauseTrack();
          }
        }
      });
    }
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
      this.$store.dispatch("next");
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
    maximize () {
      this.height = "250vh";
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
  >>>.playModeActive {
    color: var(--primary-red);
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
  font-size: 1rem;
}
>>>.v-icon:hover, >>>.v-icon:focus {
  opacity: 1;
}
.v-system-bar .v-icon {
  margin-right: 0 !important;
}
.theme--dark.v-system-bar .v-icon:hover,
.theme--dark.v-system-bar .v-icon:focus {
  color: white;
}
@media screen and (prefers-reduced-motion: reduce) {
.smooth-enter-active, .smooth-leave-active {
  transition: none;
}
}
.smooth-enter-active, .smooth-leave-active {
  transition: opacity .5s;
}
.smooth-enter, .smooth-leave-to {
  opacity: 0
}

</style>
