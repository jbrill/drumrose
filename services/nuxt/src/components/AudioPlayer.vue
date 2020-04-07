<template>
  <div class="audioPlayer">
    <div class="noselect audio-play__contain">
      <i
        ref="musicPrev"
        @click="prevMusic"
        class="audio-play__previous material-icons"
        >skip_previous</i
      >
      <i ref="musicButton" @click="playMusic" class="audio-play material-icons"
        >play_arrow</i
      >
      <i
        ref="musicNext"
        @click="nextMusic"
        class="audio-play__next material-icons"
        >skip_next</i
      >
      <div class="audio-player__track-info">
        <p class="audio-player__track-info__track-name">
          {{ track_queue.track_name }}
        </p>
        <p class="audio-player__track-info__track-artist">
          {{ track_queue.track_artist }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    playMusic() {
      let musicBtn = this.$refs.musicButton;
      if (process.client) {
        if (musicBtn.innerText === "pause") {
          window.MusicKit.getInstance()
            .player.pause()
            .then(function() {
              console.log("pausing...");
              musicBtn.innerText = "play_arrow";
            });
        } else {
          window.MusicKit.getInstance()
            .player.play()
            .then(function() {
              console.log("playing...");
              musicBtn.innerText = "pause";
            });
        }
      }
    },
    prevMusic() {
      console.log("PREV");
    },
    nextMusic() {
      console.log("NEXT");
    },
    moreMusic() {
      console.log("MORE...");
    }
  },
  data: function() {
    return {
      track_queue: {
        track_name: "somethin",
        track_artist: "dr. dre"
      }
    };
  }
};
</script>

<style scoped>
.audioPlayer {
  width: 100%;
  background: linear-gradient(
    0deg,
    rgba(0, 0, 0, 1) 0%,
    rgba(25, 25, 25, 1) 100%
  );
  height: 3rem;
  position: fixed;
  bottom: 0;
  z-index: 10000;
}

.audio-play__contain {
  padding-left: 2rem;
  display: inline-block;
  height: 100%;
}

.audio-play__contain i {
  color: white;
  padding-top: 5px; /* slight nudge down*/
  vertical-align: middle;
  margin: 0;
}
.audio-play__previous,
.audio-play__next {
  font-size: 1.5rem;
}
.audio-play {
  font-size: 2rem;
  padding-top: 5;
  /* margin-top: 1rem; */
}
.audio-play:hover {
  color: var(--primary-red);
}
.audio-play__previous:hover,
.audio-play__next:hover {
  color: var(--primary-yellow);
}
.audio-player__track-info {
  float: right;
  padding-left: 3rem;
  color: white;
}
.audio-player__track-info__track-name:hover {
  cursor: pointer;
  color: red;
}

.audio-player__track-info__track-artist:hover {
  cursor: pointer;
  color: purple;
}

.audio-player__track-info__track-name {
  font-size: 1rem;
  font-weight: bolder;
  margin-bottom: 0;
}

.audio-player__track-info__track-artist {
  font-size: 0.5rem;
}
.audio-player__more-btn {
  right: 1rem;
  color: white;
}
.audio-player__more-btn:hover {
  color: var(--primary-yellow);
}
</style>
