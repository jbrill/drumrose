<template>
  <div :class="{ post: true, activePost: (nowPlayingPost && nowPlayingPost.id === post.id) }">
    <div class="postContain">
      <div class="artistContain">
        <div class="noselect albumContain">
          <img class="albumCover" :src="post.song.album.artwork_url">
        </div>
        <div class="artistTextContain">
          <span ref="songName" class="songName">{{ post.song.name }}</span>
          <span ref="artistName" class="artistName">{{post.song.artist.name
}}</span>
        </div>
      </div>
      <div class="poster">
        <div class="posterDetail">
          <div
              class="posterImg"
              v-bind:style="{ backgroundImage: 'url(' +
                post.user.avatar_url + ')' }"
          >
          </div>
          <nuxt-link class="noselect" :to="'/' + post.user.handle">
            <div class="posterInfo">
              <h3 class="posterName">
                {{ post.user.name }}
              </h3>
              <h5 class="posterHandle">
                @{{ post.user.handle }}
              </h5>
            </div>
          </nuxt-link>
        </div>
        <p class="postCaption">
          {{ post.caption }}
        </p>
        <div class="postBottomContain">
          <i v-ripple="'rgba(255, 255, 255, 0.35)'"
            class="audioAction audioPause material-icons"
            @click="pauseTrack"
            v-if="nowPlayingPost && nowPlayingPost.id === post.id && playbackState === 2"
          >pause</i>
          <i
            class="audioAction audioPlay material-icons"
            @click="playTrack"
            v-else
          >play_arrow</i>
          <PostTimeline />
          <div class="post-action-contain">
            <i v-ripple="'rgba(255, 255, 255, 0.35)'"
              class="audioAction audioFavorite material-icons"
              @click="favoriteTrack"
            >favorite</i>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import PostTimeline from '~/components/PostTimeline';

export default {
  name: 'Post',
  components: {
    PostTimeline
  },
  computed: mapState(['nowPlayingItem', 'nowPlayingPost', 'playbackState']),
  props: ['post', 'index'],
  methods: {
    pauseTrack: async function (event) {
      await this.$store.dispatch("pause");
    },
    playTrack: function (event) {
      console.log("YO");
      const posts = this.$store.state.posts.slice(this.index)
      const tracks = posts.map(a => a.song.apple_music_id);
      this.$store.dispatch("setQueue", { "songs": tracks }).then( () => {
        this.$store.dispatch("play");
        this.$store.dispatch("setNowPlayingPost", this.post);
      });
    },
    favoriteTrack: function (event) {
      console.log('SHOUDL FAV');
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
.postCaption {
  font-size: 1em;
  color: black;
  font-family: 'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  margin-top: 1rem;
}

.post {
  width: 85%;
  margin: 0 auto;
  padding: 1em;
  border-radius: 6px;
  background-color: white;
  box-shadow: var(--shadow-medium);
}
.post:hover, .post:focus {
  cursor: pointer;
  background-color: white;
  box-shadow: var(--shadow-heavy);
}
@media (prefers-color-scheme: dark) {
  .post {
    background-color: black;
  }
  .post:hover, .post:focus {
    background-color: var(--primary-black-light);
  }
  .postCaption {
    color: white;
  }
}
.activePost {
  box-shadow: var(--shadow-heavy-purple);
}
.albumContain {
  z-index: 0;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.albumCover {
  width: 100%;
  max-width: 7em;
  height: auto;
  border-radius: 2px;
  box-shadow: var(--shadow-medium);
}
.postContain {
  display: grid;
  grid-template-columns: 15% 85%;
}
.artistContain {
  display: grid;
}
.artistName {
  font-size: 0.8rem;
  margin-bottom: 0;
  font-weight: 600;
  padding-top: 5px;
  opacity: 0.8;
}
.songName {
  font-size: 0.75rem;
  margin-bottom: 0;
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
.postBottomContain {
  display: flex;
  align-items: center;
}
.post-action-contain {
  display: inline-block;
  margin-left: auto;
}
.artistTextContain {
  display: flex;
  flex-direction: column;
  color: black;
  padding-top: 1rem;
  text-align: left; 
  font-family: 'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif;
}
.poster {
  overflow-wrap: break-word;
  position: relative;
  margin-left: 2rem;
  height: auto;
  display: grid;
  grid-template-rows: 25% 50% 25%;
}
.posterImg {
  border-radius: 4px;
  height: 3rem;
  width: 3rem;
  background-position: center;
  background-size: cover;
  box-shadow: var(--shadow-medium);
}
.posterImg:hover, .posterImg:focus {
  cursor: pointer;
  box-shadow: var(--shadow-heavy);
}
.posterDetail {
  display: flex;
}
.posterInfo {
  display: inline-block;
  color: black;
  padding: 5px;
  padding-left: 1em;
}
.posterName {
  margin-top: 0;
  color: black;
  font-size: 1rem;
  padding-bottom: 0.5rem;
  line-height: 1.5rem;
}
.posterName:hover, .posterName:focus {
  cursor: pointer;
  text-decoration: underline;
}
.posterHandle {
  font-size: 0.5rem;
  color: grey;
  margin-top: -1rem;
}
.postDate {
  margin-top: 0;
  margin-right: 0;
  font-size: 1rem;
  color: grey;
}
.postTime {
  font-size: 1rem;
  margin-top: -2.5rem;
  color: black;
  position: absolute;
}
.timeLoop {
  font-size: 1rem;
}
.postMusicContain {
  margin-top: 1rem;
  height: 20%;
}
.postActionListContain {
  float: right;
  height: 2rem;
  width: 100%;
}
.audioAction {
  color: black;
  opacity: 0.8;
  font-size: 100%;
}
.audioAction:hover, .audioAction:focus {
  opacity: 1;
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
.audioPause {
  font-size: 2rem;
}
.audioPause:hover, .audioPause:focus {
  color: var(--primary-purple);
}
.audioPlay {
  font-size: 2rem;
}
.audioPlay:hover, .audioPlay:focus {
  opacity: 1;
  color: var(--primary-purple);
}
</style>
