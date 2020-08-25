<template>
  <div class="posterInfo">
    <v-tooltip top>
      <template 
        v-slot:activator="{ on }"
      >
        <v-btn
          nuxt
          text
          color="transparent"
          class="handle-select noselect"
          :to="'/people/' + user.username"
          v-on="on"
        >
          <div
            class="posterImg"
            :style="{ backgroundImage: 'url(' + user.picture + ')' }"
          />
          <h3 class="posterName">
            {{ user.username }}
          </h3>
        </v-btn>
      </template>
      <div>Top tooltip</div>
    </v-tooltip>
    <v-icon
      v-if="postType === 'favorite'"
      x-small
    >
      mdi-heart
    </v-icon>
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
    <span>{{ date }}</span>
  </div>
</template>

<script>
export default {
  name: 'PostHeader',
  props: {
    'user': {
      type: Object, 
      default: () => {},
    },
    'date': {
      type: String,
      default: '',
    },
    'type': {
      type: String,
      default: '',
    },
    'rating': {
      type: String,
      default: '',
    },
  },
  created: function () {
    console.log(this.user);
    console.log(this.date);
    console.log(this.type);
    console.log(this.rating);
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
