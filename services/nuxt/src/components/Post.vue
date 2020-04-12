<template>
  <div class="post">
    <div class="postContain">
      <div class="artistContain">
        <i
          class="audioAction audioPlay material-icons"
          @click="playSong"
        >play_arrow</i>
        <div class="artistTextContain">
          <h4 class="songName">
            {{ post.track.track_name }}
          </h4>
          <h2 class="artistName">
            {{ post.track.track_artist }}
          </h2>
        </div>

        <div class="noselect albumContain">
          <img class="albumCover" :src="post.track.track_cover_url">
        </div>
      </div>
      <div class="poster">
        <nuxt-link class="noselect" :to="'/' + post.user.handle">
          <img class="posterImg" :src="post.user.avatar_url">
          <div class="posterDetail">
            <h3 class="posterName">
              {{ post.user.name }}
            </h3>
            <h5 class="posterHandle">
              @{{ post.user.handle }}
            </h5>
          </div>
        </nuxt-link>
        <p class="postCaption">
          {{ post.caption }}
        </p>
        <div class="post--action--contain">
          <i
            class="audioAction audioFavorite material-icons"
            @click="favoriteSong"
          >favorite_border</i>
          <i
            class="audioAction audioRepost material-icons"
            @click="repostSong"
          >loop</i>
        </div>
        <div class="postActionContain noselect" />
      </div>
    </div>
    <div class="postMusicContain noselect">
      <!-- <postActionRepost /> <postActionFavorite /> -->
      <!-- <div class="postActionListContain"><postActionList /></div> -->
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  computed: mapGetters(['musicToken', 'isMusicAuthenticated']),
  name: 'Post',
  components: {},
  methods: {
    playSong: function (event) {
      if (!process.client) {
        return;
      }
      const musicKit = window.MusicKit.getInstance();
      // We should reset the queue here
      if (event.target.textContent === 'pause') {
        window.MusicKit.getInstance()
          .player.pause()
          .then(function () {
            console.log('pausing...');
            event.target.textContent = 'play_arrow';
          });
      } else {
        window.MusicKit.getInstance()
          .player.play()
          .then(function () {
            console.log('playing...');
            event.target.textContent = 'pause';
          });
      }
    },
    repostSong: function (event) {
      console.log('SHOULD REPOST');
    },
    favoriteSong: function (event) {
      console.log('SHOUDL FAV');
    },
  },
  props: ['post'],
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
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-image: linear-gradient(to bottom, rgb(255, 255, 255, 0) 0, #000);
  opacity: 0.9;
  border-radius: 2rem;
}
.albumCover {
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  border-radius: 2rem;
  box-shadow: var(--shadow-heavy);
}
.songName:hover, .songName:focus {
  cursor: pointer;
  color: var(--primary-purple);
  opacity: 1;
}
.artistName {
  font-size: 1rem;
  font-weight: 600;
  opacity: 0.8;
}
.songName {
  font-size: 0.8rem;
  opacity: 0.8;
}
.artistName:hover, .artistName:focus {
  cursor: pointer;
  color: var(--primary-yellow);
  opacity: 1;
}
.albumCover:hover, .albumCover:focus {
  cursor: pointer;
}
.playButton {
  z-index: 10;
  margin-left: 4.5em;
  margin-top: 4.5em;
  position: absolute;
  height: 5em;
}
.playButton:hover, .playButton:focus {
  cursor: pointer;
}
.artistTextContain {
  color: white;
  text-align: left;
  padding: 5px;
  position: absolute;
  z-index: 1000;
  left: 0.5rem;
  bottom: 0.3rem;
  font-weight: 100;
  width: auto;
  height: auto;
  font-family: 'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif;
}
.poster {
  overflow-wrap: break-word;
  position: relative;
  margin-left: 1rem;
  height: auto;
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
.posterName:hover, .posterName:focus {
  cursor: pointer;
}
.posterHandle {
  font-size: 0.5rem;
  color: grey;
  margin-top: -1rem;
}
.postDate {
  margin-top: 0;
  margin-right: 0;
  font-size: 10px;
  color: grey;
}
.postCaption {
  font-size: 1em;
  color: white;
  font-family: 'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  margin-top: 1rem;
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
.post--action--contain {
  position: absolute;
  bottom: 2rem;
  right: 0;
}
.audioAction {
  color: white;
  font-size: 1.3rem;
  padding-right: 5px;
  padding-left: 5px;
  opacity: 0.8;
  position: absolute;
  margin-bottom: 0;
}
.audioAction:hover, .audioAction:focus {
  opacity: 1;
}
.audioPlay {
  opacity: 0.7;
  font-size: 6rem;
  z-index: 100;
  position: absolute;
  left: 30%;
  top: 30%;
}
.audioFavorite:hover, .audioFavorite:focus {
  color: var(--red-accent);
}
.audioRepost {
  float: left;
}
.audioRepost:hover, .audioRepost:focus {
  color: var(--primary-purple);
}
.audioFavorite {
  right: 0.5rem;
}
.audioMore {
  float: right;
}
.audioPlay:hover, .audioPlay:focus {
  opacity: 1;
}
</style>
