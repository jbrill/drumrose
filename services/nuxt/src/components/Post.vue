<template>
  <div v-if="post" class="post">
    <div class="postContain">
      <div class="posterDetail">
          <div class="posterInfo">
            <nuxt-link class="handle-select noselect" :to="'/people/' + post.user.handle">
              <div
                  class="posterImg"
                  v-bind:style="{ backgroundImage: 'url(' +
                    post.user.avatar_url + ')' }"
              >
              </div>
              <h3 class="posterName">
                {{ post.user.handle }}
              </h3>
            </nuxt-link>
            <p class="poster-action"><span>favorited</span>
a <span>{{ type }}</span></p>
          </div>
      </div>
    </div>
    <MusicItem v-if="type === 'track'" type="track" :apple_music_id="post.song.apple_music_id" />
    <MusicItem v-else-if="type === 'album'" type="album" :apple_music_id="post.album.apple_music_id" />
    <MusicItem v-else-if="type === 'playlist'" type="playlist" :apple_music_id="post.playlist.apple_music_id" />
  </div>
</template>

<script>
import { mapState } from 'vuex';
import MusicItem from '~/components/MusicItem';

export default {
  name: 'Post',
  props: ['post', 'index', 'type'],
  components: {
    MusicItem
  },
  mounted() {
    console.log(this.post)
    console.log(this.type)
  },
};
</script>

<style>
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
  width: 100%;
  margin: 0 auto;
  padding: 1rem;
  display: inline;
}
.activePost {
  box-shadow: var(--shadow-heavy-purple);
}
.activePost:hover, .activePost:focus {
  box-shadow: var(--shadow-heavy-purple);
}
.post-action-contain {
  display: inline-block;
  margin-left: auto;
}
.poster {
  overflow-wrap: break-word;
  position: relative;
  margin-left: 2rem;
  height: auto;
  display: grid;
  grid-template-rows: 25% 75%;
}
.posterImg {
  border-radius: 50%;
  height: 1.5rem;
  width: 1.5rem;
  background-position: center;
  background-size: cover;
  border: 1px solid #ccc;
}
.posterImg:hover, .posterImg:focus {
  cursor: pointer;
}
.posterDetail {
  display: flex;
  align-items: center;
}
.posterInfo {
  display: inline-block;
  color: #ccc;
}
.posterName {
  margin-bottom: 0;
  color: white;
  padding-left: 0.5rem;
  font-size: 0.7rem;
  font-weight: bold;
}
.posterName:hover, .posterName:focus {
  cursor: pointer;
}
p.poster-action {
  font-size: 0.7rem;
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
.handle-select {
  padding-bottom: 0.5rem;
  display: flex;
  align-items: center;
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
</style>
