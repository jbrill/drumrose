<template>
  <div>
    <v-row
      class="fill-height"
      align="center"
      justify="space-between"
    >
      <v-btn
        text
        :href="'/people/' + user"
        color="#ccc"
        :to="'/people/' + user"
      >
        {{ user }}
      </v-btn>
      <v-rating
        v-if="rating"
        v-model="rating"
        background-color="white"
        color="var(--primary-yellow)"
        dense
        half-increments
        readonly
        small
        size="22"
      />
    </v-row>
    <v-row class="review">  
      <p class="body-1 review__text">
        {{ review }}
      </p>
    </v-row>
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
    'review': {
      type: String,
      default: '',
    },
  },
  created: function () {

  },
  methods: {
    addRating (value, id) {
    },
  },
};
</script>

<style scoped>
@media screen and (prefers-color-scheme: dark) {
  .postCaption {
    color: white;
  } 
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
.profile-name {
  color: #ccc;
}
.review__text {
  padding: 2rem;
}
</style>
