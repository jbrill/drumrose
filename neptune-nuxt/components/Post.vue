<template>
  <div class="post">
    <div class="postContain">
      <div class="artistTextContain">
        <h2 class="artistName">{{ post.track.track_artist }}</h2>
        <h4 class="songName">{{ post.track.track_name }}</h4>
      </div>

      <div class="artistContain">
        <i @click="playSong" class="audioAction audioPlay material-icons"
          >play_arrow</i
        >
        <div class="noselect albumContain">
          <img class="albumCover" :src="post.track.track_cover_url" />
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
        <div class="postActionContain noselect"></div>
      </div>
    </div>
    <div class="postMusicContain noselect">
      <!-- <i @click="viewMoreSong" class="audioAction audioMore material-icons"
        >more_horiz</i
      > -->
      <i @click="favoriteSong" class="audioAction audioFavorite material-icons"
        >favorite_border</i
      >
      <i @click="repostSong" class="audioAction audioRepost material-icons"
        >loop</i
      >
      <!-- <postActionRepost /> <postActionFavorite /> -->
      <!-- <div class="postActionListContain"><postActionList /></div> -->
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
  width: 80%; /* 83 percent of grid width */
  margin: 0 auto;
  display: grid;
}
.postContain {
  display: flex;
  position: relative;
}
.artistContain {
  position: relative;
  width: auto;
  /* height: 2rem; */
  float: left;
}
.albumContain {
  z-index: 0;
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
  opacity: 0.7;
  border-radius: 2rem;
}
.albumCover {
  /* width: auto; */
  /* float: left; */
  /* content: ""; */
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  border-radius: 2rem;
  box-shadow: var(--shadow-heavy);
}
.songName:hover {
  cursor: pointer;
  color: #c0102c;
  opacity: 1;
}
.artistName {
  font-size: 1rem;
  font-weight: 400;
  opacity: 0.8;
}
.songName {
  font-size: 1.2rem;
  opacity: 0.8;
}
.artistName:hover {
  cursor: pointer;
  color: #f3f367;
  opacity: 1;
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
  text-align: left;
  padding: 5px;
  position: absolute;
  z-index: 10000;
  left: 0.5rem;
  bottom: 0.5rem;
  font-weight: 100;
  width: auto;
  height: auto;
  font-family: "Proxima Nova", "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.poster {
  overflow-wrap: break-word;
  /* left: 10px; */
  position: relative;
  height: 100%;
  /* float: right; */
  margin-left: 1rem;
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
  margin-top: 1rem;
  height: 20%;
}
.postActionListContain {
  float: right;
  height: 2rem;
  width: 100%;
}
.audioAction {
  color: white;
  font-size: 1.5rem;
  padding-right: 5px;
}
.audioAction:hover {
  color: var(--primary-yellow);
}
.audioPlay {
  opacity: 0.7;
  font-size: 6rem;
  z-index: 100;
  position: absolute;
  left: 30%;
  top: 30%;
}
.audioRepost {
  float: left;
}
.audioFavorite {
  float: left;
}
.audioMore {
  float: right;
}
.audioPlay:hover {
  opacity: 1;
}
</style>
