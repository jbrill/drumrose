<template>
  <div class="post">
    <div class="postContain">
      <div class="artistContain">
        <div class="noselect albumContain">
          <img class="albumCover" :src="post.track.track_cover_url" />
        </div>
        <div class="artistTextContain">
          <h2 class="artistName">{{ post.track.track_artist }}</h2>
          <h4 class="songName">{{ post.track.track_name }}</h4>
        </div>
      </div>
      <div class="poster">
        <nuxt-link class="noselect" v-bind:to="'/' + post.user.handle">
          <img class="posterImg" :src="post.user.avatar_url" />
          <div class="posterDetail">
            <h3 class="posterName">{{ post.user.name }}</h3>
            <h5 class="posterHandle">@{{ post.user.handle }}</h5>
          </div>
        </nuxt-link>
        <p class="postCaption">{{ post.caption }}</p>
        <div class="postActionContain noselect">
          <postActionRepost /> <postActionFavorite />
        </div>
      </div>
    </div>
    <div class="postMusicContain noselect">
      <i @click="playSong" class="audioPlay material-icons">play_arrow</i>
      <postActionList />
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import PostActionFavorite from "~/components/postActions/PostActionFavorite";
import PostActionRepost from "~/components/postActions/PostActionRepost";
import PostActionList from "~/components/postActions/PostActionList";

export default {
  computed: mapGetters(["musicToken", "isMusicAuthenticated"]),
  components: {
    PostActionList,
    PostActionFavorite,
    PostActionRepost
  },
  methods: {
    playSong: function(event) {
      if (!process.server) {
        // client
        let musicKit = window.MusicKit.getInstance();
        musicKit.setQueue(this.post.track.track_playback);
        this.$store.commit("SET_PLAYING", this.post.track);
      }
    }
  },
  name: "post",
  props: ["post"]
};
</script>

<style scoped>
.post {
  width: 83%; /* 83 percent of grid width */
  margin: 0 auto;
  box-shadow: var(--shadow-heavy);
}
.postContain {
  background-color: black;
  border-top: 2px solid var(--red-accent);
  height: 15rem;
  overflow: hidden;
}
.artistContain {
  position: relative;
  width: auto;
  height: 100%;
  float: left;
}
.albumCover {
  width: auto;
  height: 100%;
  float: left;
}
.albumContain::before {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-image: linear-gradient(to bottom, rgb(255, 255, 255, 0) 0, #000);
  opacity: 0.6;
}
.albumContain {
  z-index: 0;
}
.songName:hover {
  cursor: pointer;
  text-decoration: underline;
  color: #c0102c;
}
.artistName:hover {
  cursor: pointer;
  text-decoration: underline;
  color: #f3f367;
}
.albumCover:hover {
  cursor: pointer;
}
.playButton {
  z-index: 10;
  margin-left: 4.5em;
  margin-top: 4.5em;
  position: absolute;
  height: 5em;
}
.playButton:hover {
  cursor: pointer;
}
.artistTextContain {
  color: white;
  position: absolute;
  text-align: left;
  padding: 7px;
  left: 0;
  bottom: 0;
  font-weight: 100;
  width: auto;
  height: auto;
}
.poster {
  overflow-wrap: break-word;
  margin: 10px;
  position: relative;
  height: 100%;
  margin-left: 16rem;
}
.posterImg {
  width: 2rem;
  border-radius: 50%;
}
.posterDetail {
  display: inline-block;
  color: white;
}
.posterName {
  margin-top: 0;
  color: white;
  font-size: 1rem;
  padding-bottom: 0.5rem;
  line-height: 1.5rem;
}
.posterName:hover {
  cursor: pointer;
  color: #c0102c;
}
.posterHandle {
  font-size: 0.5rem;
  color: grey;
  margin-top: -1rem;
}
.postDate {
  margin-top: 0px;
  margin-right: 0px;
  font-size: 10px;
  color: grey;
}
.postCaption {
  font-size: 1em;
  color: white;
  font-family: "Proxima Nova", "Helvetica Neue", Helvetica, Arial, sans-serif;
  margin-left: 1rem;
  margin-top: 1rem;
}
.postActionContain {
  position: absolute;
  bottom: 1rem;
  right: 0;
}
.postActionContain i {
  font-size: 1.5em;
}
.postTime {
  font-size: 1rem;
  margin-top: -2.5rem;
  color: white;
  position: absolute;
}
.timeLoop {
  font-size: 1rem;
}
.postMusicContain {
  height: 3rem;
  width: 100%;
  position: relative;
  background-color: black;
  border-top: 1px solid var(--red-accent);
}
.audioPlay {
  color: white;
  margin-left: 1rem;
  margin-top: 0.5rem;
  font-size: 2rem;
}
.audioPlay:hover {
  color: #772ce6;
}
</style>
