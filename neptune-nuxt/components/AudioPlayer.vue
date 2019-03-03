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
    <i
      ref="moreMusic"
      @click="moreMusic"
      class="audio-player__more-btn material-icons"
      >more_horiz</i
    >
  </div>
</template>

<script>
export default {
  methods: {
    playMusic() {
      let musicBtn = this.$refs.musicButton;
      if (!process.server) {
        if (musicBtn.innerText === "pause") {
          // we need to pause
          window.MusicKit.getInstance()
            .player.pause()
            .then(function() {
              musicBtn.innerText = "play_arrow";
            });
        } else {
          // we need to play
          window.MusicKit.getInstance()
            .player.play()
            .then(function() {
              console.log("Pausing...");
              // lets change the state of buttons here...
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
  background: rgb(0, 0, 0);
  background: linear-gradient(
    0deg,
    rgba(0, 0, 0, 1) 0%,
    rgba(25, 25, 25, 1) 100%
  );
  border-top: 1px solid var(--primary-black-light);
  height: 3.5rem;
  /* overflow: hidden; */
  position: fixed;
  bottom: 0;
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
  font-size: 2rem;
}
.audio-play {
  font-size: 2.5rem;
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
  margin-top: 5px; /* nudge down a bit */
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
  margin-bottom: 0.5rem;
}
.audio-player__more-btn {
  position: absolute;
  right: 1rem;
  margin-top: 1rem;
  color: white;
  height: 3.5rem;
}
.audio-player__more-btn:hover {
  color: var(--primary-yellow);
}
</style>
