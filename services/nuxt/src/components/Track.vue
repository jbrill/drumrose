<template>
  <div :class="{ track: true }">
    <div
      class="artistContain"
      @mouseenter="trackHover"
      @mouseleave="trackMouseLeave"
    >
      <div class="noselect albumContain">
        <img class="albumCover" :src="artworkUrl">
        <div ref="audioAction" class="audio-action-contain">
          <i
            class="audioAction audioPlay material-icons"
            @click="playTrack"
          >play_arrow</i>
        </div>
      </div>
    </div>
    <div class="artistTextContain">
      <span ref="songName" class="songName">{{ name }}</span>
      <span ref="artistName" class="artistName">{{ artistName }}</span>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'Track',
  props: {
    'appleMusicId': {
      type: String,
      default: '',
    },
  },
  data () {
    return {
      isLoading: true,
      albumName: '',
      artistName: '',
      artworkUrl: '',
      name: '',
    };
  },
  computed: mapState(
    ['nowPlayingItem', 'nowPlayingPost', 'playbackState']
  ),
  async mounted () {
    const resp = await this.$store.getters.fetch(
      `/v1/catalog/us/songs/${this.appleMusicId}`
    );
    this.artistName = resp.data[0].attributes.artistName;
    this.name = resp.data[0].attributes.name;
    this.artworkUrl = resp.data[0].attributes.artwork.url.replace(
      '{w}', '250'
    ).replace(
      '{h}', '250'
    );
    this.isLoading = false;
  },
  methods: {
    pauseTrack: async function (event) {
      await this.$store.dispatch("pause");
    },
    playTrack: function (event) {
    },
    trackHover: function () {
      this.$refs.audioAction.style.opacity = 1;
    },
    trackMouseLeave: function () {
      this.$refs.audioAction.style.opacity = 0;
    },
  },
};
</script>

<style scoped>
@media screen and (prefers-color-scheme: dark) {
  .songName:hover, .songName:focus {
    color: black;
  }
  .artistName:hover, .artistName:focus {
    color: black;
  }
  .artistTextContain {
    color: grey;
  }
  .posterInfo {
    color: black;
  }
  .posterName {
    color: black;
  }
  .posterHandle {
    color: black;
  }
  .postDate {
    color: black;
  }
  .postTime {
    color: black;
  }
  .audioAction {
    color: black;
  }
  .audioFavorite:hover, .audioFavorite:focus {
    color: grey;
  }
}

.track {
  width: 100%;
  margin: 0 auto;
  display: inline;
}
.albumContain {
  z-index: 0;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}
.albumCover {
  width: 100%;
  height: auto;
  border-radius: 2px;
  border: 1px solid #ccc;
  box-shadow: var(--shadow-medium);
}
.artistName {
  font-size: 0.8rem;
  margin-bottom: 0;
  font-weight: 600;
  padding-top: 5px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  opacity: 0.8;
}
.songName {
  font-size: 0.75rem;
  margin-bottom: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  opacity: 0.8;
}
.songName:hover, .songName:focus {
  cursor: pointer;
  color: black;
  opacity: 1;
}
.artistName:hover, .artistName:focus {
  cursor: pointer;
  color: black;
  opacity: 1;
}
.albumCover:hover, .albumCover:focus {
  cursor: pointer;
  box-shadow: var(--shadow-heavy);
}
.artistTextContain {
  display: flex;
  bottom: 0;
  width: 100%;
  padding-top: 0.5rem;
  flex-direction: column;
  color: var(--primary-black-light);
}
.audio-action-contain {
	width: 3.5rem;
	height: 3.5rem;
	background-color: var(--primary-red);
	position: absolute;
	display: flex;
	border-radius: 50%;
	align-items: center;
	opacity: 0;
	justify-content: center;
}
.audioAction {
  color: white;
  font-size: 3.5rem;
}
.audioFavorite {
  padding-right: 1rem;
}
.audioFavorite:hover, .audioFavorite:focus {
  color: var(--primary-red);
}
.audioMore {
  float: left;
}
.audioPause:hover, .audioPause:focus {
  color: var(--primary-purple);
}
</style>
