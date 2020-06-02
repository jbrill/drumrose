<template>
  <div v-if="!isLoading">
    <div class="artistContain">
      <div class="noselect albumContain" @mouseenter="isHovering = true" @mouseleave = "isHovering = false">
        <img class="albumCover" :src="artworkUrl">
        <div ref="albumOverlay" :class="{ albumOverlay: true, albumOverlayActive: isHovering }">
          <div class="album-overlay-actions-contain">
						<v-btn
							icon
							dark
						>
							<v-icon small color="white" class="album-overlay-more">mdi-heart</v-icon>
            </v-btn>
            <v-menu dark offset-y>
							<template v-slot:activator="{ on }">
								<v-btn
									icon
									dark
									v-on="on"
								>
									<v-icon small color="white" class="album-overlay-more">mdi-dots-horizontal</v-icon>
								</v-btn>
							</template>
							<v-list>
								<v-list-item
									@click=""
								>
									<v-list-item-title><v-icon>mdi-playlist-plus</v-icon> Add to queue</v-list-item-title>
								</v-list-item>
								<v-list-item
									@click=""
								>
									<v-list-item-title><v-icon>mdi-music-box-multiple</v-icon> Add to playlist</v-list-item-title>
								</v-list-item>
								<v-list-item
									@click=""
								>
									<v-list-item-title><v-icon>mdi-music-box</v-icon> Add to library</v-list-item-title>
								</v-list-item>
							</v-list>
						</v-menu>
          </div>
        </div>
        <div ref="audioAction" :class="{ audioActionContain: true, audioActionContainActive: isHovering }">
          <v-icon
            class="audioAction audioPlay material-icons"
            @click="playTrack"
            v-if="nowPlayingPost && nowPlayingPost.id === post.id && playbackState === 2"
            color="var(--primary-red--dark)"
          >mdi-pause</v-icon>
          <v-icon
            class="audioAction audioPlay material-icons"
            @click="playTrack"
            v-else
            color="white"
          >mdi-play</v-icon>
        </div>
      </div>
    </div>
    <div class="textContain">
      <span ref="songName" class="songName">{{ name }}</span>
      <span v-if="type === 'playlist'" ref="playlistName" class="artistName">{{ curatorName }}</span>
      <span v-else ref="artistName" class="artistName">{{ artistName }}</span>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  props: {
    type: String,
    apple_music_id: String
  },
  data () {
    return {
      isLoading: true,
      albumName: '',
      curatorName: '',
      artistName: '',
      artworkUrl: '',
      name: '',
      isHovering: false,
    }
  },
  computed: mapState(['nowPlayingItem', 'nowPlayingPost', 'playbackState']),
  methods: {
    pauseTrack: async function (event) {
      await this.$store.dispatch("pause");
    },
    playTrack: async function (event) {
      await this.$store.dispatch("play");
    },
  },
  async mounted () {
    let resp = '';
    if (this.type === 'track') {
      resp = await this.$store.getters.fetch(`/v1/catalog/us/songs/${this.apple_music_id}`)
      this.artistName = resp.data[0].attributes.artistName;
    } else if (this.type === 'album') {
      resp = await this.$store.getters.fetch(`/v1/catalog/us/albums/${this.apple_music_id}`)
      this.artistName = resp.data[0].attributes.artistName;
    } else if (this.type === 'playlist') {
      resp = await this.$store.getters.fetch(`/v1/catalog/us/playlists/${this.apple_music_id}`);
      console.log(resp);
      this.curatorName = resp.data[0].attributes.curatorName;
    }
    this.name = resp.data[0].attributes.name;
    this.artworkUrl = resp.data[0].attributes.artwork.url.replace('{w}', '250').replace('{h}', '250');
    this.isLoading = false;
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
  .textContain {
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

.albumContain {
  z-index: 0;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  border-radius: 1px;
  box-shadow: var(--shadow-medium);
}
.albumContain:hover, .albumContain:focus {
  cursor: pointer;
}
>>>.v-list-item__title, >>>.v-icon {
  font-size: 0.8rem;
}
>>>.v-list-item {
  min-height: 2rem;
}
>>>.v-sheet {
  padding: 0;
}
.albumCover {
  width: 100%;
  height: auto;
  border-radius: 2px;
}
.albumOverlay {
  width:100%;
	height:100%;
	position:absolute;
  background: rgb(255,255,255);
  background: linear-gradient(180deg, rgba(0,0,0,0) 41%, rgba(0,0,0,0.5) 100%);
  opacity: 0;
  border-radius: 2px;
}
.albumOverlayActive {
  opacity: 1;
}
.album-overlay-actions-contain {
  position: absolute;
  width: 100%;
  bottom: 0;
  right: 0;
  display: flex;
}
.album-overlay-more {
  opacity: 1;
  align-self: flex-end;
}
.album-overlay-favorite {
  opacity: 1;
  align-self: flex-start;
}
.album-overlay:hover, .album-overlay:focus {
  opacity:1;
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
  color: white;
  opacity: 1;
}
.artistName:hover, .artistName:focus {
  cursor: pointer;
  color: white;
  opacity: 1;
}
.albumCover:hover, .albumCover:focus {
  cursor: pointer;
  box-shadow: var(--shadow-heavy);
}
.textContain {
  display: flex;
  bottom: 0;
  width: 100%;
  padding-top: 0.5rem;
  flex-direction: column;
  color: var(--primary-black-light);
}
.audioActionContain {
	width: 2.5rem;
	height: 2.5rem;
	position: absolute;
	display: flex;
  opacity: 0;
	border-radius: 50%;
	align-items: center;
	justify-content: center;
}
.audioActionContainActive {
  opacity: 1;
}
.audioAction {
  color: black;
  font-size: 2.5rem;
  background-color: var(--primary-red--dark);
  border-radius: 50%;
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
