<template>
  <div class="audioPlayer">
    <div class="noselect audio-play__contain">
      <i
        ref="musicPrev"
        class="audio-play__previous material-icons"
        @click="prevMusic"
      >skip_previous</i>
      <i
        ref="musicButton"
        class="audio-play
material-icons"
        @click="playMusic"
      >play_arrow</i>
      <i
        ref="musicNext"
        class="audio-play__next material-icons"
        @click="nextMusic"
      >skip_next</i>
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
  data: function () {
    return {
      track_queue: {
        track_name: 'somethin',
        track_artist: 'dr. dre',
      },
    };
  },
  methods: {
    playMusic () {
      const musicBtn = this.$refs.musicButton;
      if (process.client) {
        if (musicBtn.textContent === 'pause') {
          window.MusicKit.getInstance()
            .player.pause()
            .then(function () {
              console.log('pausing...');
              musicBtn.textContent = 'play_arrow';
            });
        } else {
          window.MusicKit.getInstance()
            .player.play()
            .then(function () {
              console.log('playing...');
              musicBtn.textContent = 'pause';
            });
        }
      }
    },
    prevMusic () {
      console.log('PREV');
    },
    nextMusic () {
      console.log('NEXT');
    },
    moreMusic () {
      console.log('MORE...');
    },
  },
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
  padding-top: 5px; /* slight nudge down */
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

.audio-play__previous,
.audio-play__next {
  font-size: 1.5rem;
}
.audio-play {
  font-size: 2rem;
  padding-top: 5;

  /* margin-top: 1rem; */
}
.audio-play:hover, .audio-play:focus {
  color: var(--primary-red);
}
.audio-play__previous:hover,
.audio-play__next:hover, .audio-play__previous:focus,
.audio-play__next:focus {
  color: var(--primary-yellow);
}

.audio-player__track-info {
  float: right;
  padding-left: 3rem;
  color: white;
}

.audio-player__track-info__track-name {
  font-size: 1rem;
  font-weight: bolder;
  margin-bottom: 0;
}

.audio-player__track-info__track-name:hover,
.audio-player__track-info__track-name:focus {
  cursor: pointer;
  color: red;
}

.audio-player__track-info__track-artist {
  font-size: 0.5rem;
}

.audio-player__track-info__track-artist:hover,
.audio-player__track-info__track-artist:focus {
  cursor: pointer;
  color: purple;
}

.audio-player__more-btn {
  right: 1rem;
  color: white;
}
.audio-player__more-btn:hover,
.audio-player__more-btn:focus {
  color: var(--primary-yellow);
}
</style>
