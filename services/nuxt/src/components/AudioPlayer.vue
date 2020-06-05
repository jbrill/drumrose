<template>
  <div class="audioPlayer">
    <div
      v-hotkey="{
        'space': playTrack,
      }" 
      class="nowPlayingContain"
    >
      <i
        ref="volumeButton"
        class="volume-button material-icons"
        @click="changeVolume"
      >volume_up</i>
      <i
        ref="queueButton"
        class="queue-button material-icons"
        @click="showQueue"
      >queue_music</i>
      <div class="audio-player-artwork">
        <span
          :style="{
            backgroundImage:
              'url(' + nowPlayingItem.attributes.artwork.url + ')',
            backgroundSize: 'cover'
          }"
        />
      </div>
      <div class="audio-player__track-info">
        <span ref="trackArtist" class="audio-player__track-info__track-artist">
          {{ nowPlayingItem.attributes.artistName }}
        </span>
        <span ref="songName" class="audio-player__track-info__track-name">
          {{ nowPlayingItem.attributes.name }}
        </span>
      </div>
      <i
        ref="favoriteButton"
        class="favorite-button material-icons"
        @click="favoriteTrack"
      >favorite</i>
    </div>
    <div class="musicControls">
      <i
        ref="musicPrev"
        class="audio-play__previous material-icons"
        @click="prevMusic"
      >skip_previous</i>
      <i
        v-if="playbackState === 3"
        ref="musicButton"
        class="audio-play
material-icons"
        @click="playTrack"
      >play_arrow</i>
      <i
        v-else
        ref="musicButton"
        class="audio-pause
material-icons"
        @click="pauseTrack"
      >pause</i>
      <i
        ref="musicNext"
        class="audio-play__next material-icons"
        @click="nextMusic"
      >skip_next</i>
      <div class="musicNavigationControls">
        <i
          ref="shuffleButton"
          v-tooltip="'Shuffle'"
          class="shuffle-button material-icons"
          @click="shuffleTrack"
        >shuffles</i>
        <i
          ref="repeatButton"
          class="repeat-button material-icons"
          @click="repeatTrack"
        >repeat</i>
      </div>
    </div>
    <PostTimeline />
  </div>
</template>

<script>
import { mapState } from "vuex";
import PostTimeline from "~/components/PostTimeline";

export default {
  components: {
    PostTimeline,
  },
  computed: {
    ...mapState(['nowPlayingItem', 'playbackState']),
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
      console.log("SHUFFLE");
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
  display: grid;
  grid-template-columns: 35% 15% 50%;
}

.nowPlayingContain {
  height: 100%;
  display: grid;
  grid-template-columns: 10% 10% 15% 55% 10%;
  grid-template-rows: 100%;
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
.audio-play__previous,
.audio-play__next {
  font-size: 1rem;
  align-self: center;
  color: white;
}
.audio-play, .audio-pause {
  font-size: 1.8rem;
  padding: 5px;
  align-self: center;
  color: white;
}

.audio-player__track-info {
  color: white;
  display: grid;
  grid-template-rows: 50% 50%;
}

.audio-player__track-info__track-name {
  font-size: 0.5rem;
  margin-bottom: 0;
}

.audio-player__track-info__track-name:hover,
.audio-player__track-info__track-name:focus {
  cursor: pointer;
  color: white;
}

.audio-player__track-info__track-artist {
  font-size: 0.6rem;
  align-self: flex-end;
}

.audio-player__track-info span {
  color: #ccc;
}
.audio-player__track-info__track-artist:hover,
.audio-player__track-info__track-artist:focus {
  cursor: pointer;
  color: white;
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
  margin: 0 auto;
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
