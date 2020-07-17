<template>
  <div v-if="post" class="post">
    <div class="postContain">
      <div class="posterDetail">
        <div class="posterInfo">
          <v-tooltip top>
            <template v-slot:activator="{ on }">
              <v-btn
                nuxt
                text
                color="transparent"
                class="handle-select noselect"
                :to="'/people/' + post.user.username"
                v-on="on"
              >
                <div
                  class="posterImg"
                  :style="{ backgroundImage: 'url(' +
                    post.user.picture + ')' }"
                />
                <h3 class="posterName">
                  {{ post.user.username }}
                </h3>
              </v-btn>
            </template>
            <div>Top tooltip</div>
          </v-tooltip>
          <v-icon x-small v-if="postType === 'favorite'">mdi-heart</v-icon>
          <v-rating
            v-else-if="postType === 'rating'"
            v-model="rating"
            background-color="white"
            color="var(--primary-purple)"
            dense
            half-increments
            hover
            x-small
            size="18"
          />
          <span>February 4</span>
        </div>
      </div>
    </div>
    <MusicItem
      v-if="type === 'track'"
      type="track"
      :postType="postType"
      :apple-music-id="post.song.apple_music_id"
    />
    <MusicItem
      v-else-if="type === 'album'"
      type="album"
      :apple-music-id="post.album.apple_music_id"
    />
    <MusicItem
      v-else-if="type === 'playlist'"
      type="playlist"
      :apple-music-id="post.playlist.apple_music_id"
    />
  </div>
</template>

<script>
import MusicItem from '~/components/MusicItem';
import axios from 'axios';


export default {
  name: 'Post',
  components: {
    MusicItem,
  },
  props: {
    'post': {
      type: Object, 
      default: () => {},
    },
    'postType': {
      type: String,
      default: '',
    },
    'type': {
      type: String,
      default: '',
    },
  },
  data: () => ({
    rating: 4.3,
  }),
  created: function() {
    console.log(this.post)
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
  text-align: center;
  margin-bottom: 1rem;
  width: 100%;
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
  margin-bottom: 0;
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
