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
  background-color: black;
  height: 3rem;
  overflow: hidden;
  position: fixed;
  bottom: 0;
}

.audio-play__contain {
  padding-left: 2rem;
  display: inline-block;
}

.audio-play__contain i {
  color: white;
  margin-top: 0.5rem;
  font-size: 2rem;
}
.audio-play__contain i:hover {
  color: var(--primary-yellow);
}
.audio-player__track-info {
  float: right;
  padding-left: 3rem;
  color: white;
  padding-top: 0.5rem;
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
  font-size: 0.7rem;
  line-height: 1rem;
  font-weight: bolder;
}

.audio-player__track-info__track-artist {
  font-size: 0.5rem;
  line-height: 1rem;
}
</style>
