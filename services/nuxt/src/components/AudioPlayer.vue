<template>
  <div v-if="queue.length" class="audioPlayer">
    <div class="volumeControls">
      <v-slider
				class="volume-slider"
				v-model="volume"
				append-icon="volume_up"
				prepend-icon="volume_down"
				min="0"
				max="100"
			></v-slider>
    </div>
    <div class="musicControls">
      <v-icon
        x-small
        ref="shuffleButton"
        @click="shuffleTrack"
        :class="{ playModeActive: $store.state.shuffleMode === 1 }"
      >mdi-shuffle</v-icon>
      <v-icon
        ref="musicPrev"
        class="audio-play__previous material-icons"
        @click="prevMusic"
      >mdi-skip-previous</v-icon>
      <v-icon
        v-if="playbackState === 3"
        ref="musicButton"
        @click="playTrack"
        large
      >mdi-play-arrow</v-icon>
      <v-icon
        v-else
        ref="musicButton"
        @click="pauseTrack"
        large
      >mdi-pause</v-icon>
      <v-icon
        ref="musicNext"
        @click="nextMusic"
      >mdi-skip-next</v-icon>
      <v-icon
        x-small
        v-if="$store.state.repeatMode === 1"
        ref="repeatButton"
        @click="repeatTrack"
        color="var(--primary-red)"
      >mdi-repeat-once</v-icon>
      <v-icon
        x-small
        v-else-if="$store.state.repeatMode === 2"
        ref="repeatButton"
        @click="repeatTrack"
        color="var(--primary-red)"
      >mdi-repeat</v-icon>
      <v-icon
        x-small
        v-else
        ref="repeatButton"
        @click="repeatTrack"
      >mdi-repeat-off</v-icon>
    </div>
    <PostTimeline />
    <div
      v-hotkey="{
        'space': playTrack,
      }" 
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
        <span
        />
      </div>
      <div v-if="nowPlayingItem">
        <span ref="trackArtist">
          {{ nowPlayingItem.attributes.artistName }}
        </span>
        <span ref="songName">
          {{ nowPlayingItem.attributes.name }}
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
        small
        ref="favoriteButton"
        @click="favoriteTrack"
      >mdi-dots-horizontal</v-icon>
      <v-icon
        small
        ref="queueButton"
        @click="showQueue"
      >queue_music</v-icon>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import PostTimeline from "~/components/PostTimeline";

export default {
  components: {
    PostTimeline,
  },
  data () {
    return {
      volume: 10,
    }
  },
  computed: {
    ...mapState(['nowPlayingItem', 'queue', 'playbackState']),
    isOverflowing () {
      const element = this.$refs.songName;
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
      if (
        this.$store.state.playbackTime.currentPlaybackTime >= 3 || 
        this.$store.state.history.length === 0
      ) {
        this.$store.dispatch("seek", 0);
      } else {
        this.$store.dispatch("previous");
      }
    },
    nextMusic () {
      let vm = this;
      this.$store.dispatch("next").then( function () {
        const idx = vm.$store.state.posts.filter(a => {
          return a.song.apple_music_id === vm.$store.state.nowPlayingItem.id;
        });
        console.log(idx);
        vm.$store.dispatch("setNowPlayingPost", idx[0]);
      });
    },
    moreMusic () {
      console.log('MORE...');
    },
    repeatTrack () {
      console.log("REPEAT");
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
    favoriteTrack () {
      console.log("favorite");
    },
  },
};
</script>

<style scoped>
.audioPlayer {
  width: 100%;
  height: 3rem;
  background: linear-gradient(
    0deg,
    rgba(0, 0, 0, 1) 0%,
    rgba(25, 25, 25, 1) 100%
  );
  position: fixed;
  bottom: 0;
  z-index: 10000;
  display: flex;
}
.volumeControls {
  width: 15%;
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
  width: 25%;
  display: flex;
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
  margin: 0 auto;
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
  width: 25%;
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
