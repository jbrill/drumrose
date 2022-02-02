<template>
  <v-system-bar
    v-if="playbackTime"
    :height="height"
    style="z-index: 10"
    class="audioPlayer"
  >
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
import { mapState, mapGetters } from "vuex";
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
    ...mapGetters({
        stateQueue: 'getQueue',
    }),
  },
  watch: {
    async playbackState (oldPlaybackState, newPlaybackState) {
      // Our fancy notification (2).
      if (newPlaybackState === 6) {
        await this.$store.dispatch("play");
      }
      // console.log(`We had ${oldPlaybackState} fruits, aw!`);
      // console.log(`We have ${newPlaybackState} fruits now, yay!`);
    },
  },
  created () {
    if (process.browser) {
      window.addEventListener('keydown', e => { // eslint-disable-line
        console.log(e)
        if (e.defaultPrevented) {
          return; // Do nothing if the event was already processed
        }

        switch (e.code) {
          case "Down": // IE/Edge specific value
          case "ArrowDown":
            // Do something for "down arrow" key press.
            break;
          case "Up": // IE/Edge specific value
          case "ArrowUp":
            // Do something for "up arrow" key press.
            break;
          case "Left": // IE/Edge specific value
          case "ArrowLeft":
            // Do something for "left arrow" key press.
            break;
          case "Right": // IE/Edge specific value
          case "ArrowRight":
            // Do something for "right arrow" key press.
            break;
          case "Enter":
            // Do something for "enter" or "return" key press.
            break;
          case "Esc": // IE/Edge specific value
          case "Escape":
            // Do something for "esc" key press.
            break;
          case "Space":
            if (this.playbackTime) {
              if (this.playbackState === 3) {
                this.playTrack();
              } else {
                this.pauseTrack();
              }
            }
            break;
          default:
            return; // Quit when this doesn't handle the key event.
        }

        // Cancel the default action to avoid it being handled twice
        e.preventDefault();
        
      });
    }
  },
  methods: {
    async playTrack () {
      await this.$store.dispatch("play");
    },
    async pauseTrack () {
      await this.$store.dispatch("pause");
    },
    async prevMusic () {
      await this.$store.dispatch("previous");
    },
    async nextMusic () {
      await this.$store.dispatch("next");
    },
    async repeatTrack () {
      await this.$store.dispatch("toggleRepeatMode");
    },
    async shuffleTrack () {
      await this.$store.dispatch("toggleShuffleMode");
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
