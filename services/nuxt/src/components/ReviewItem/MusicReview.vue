<template>
  <v-container>
    <!-- favorite -->
    <v-container
      v-if="post.user && !(
        post.review
      )"
    >
      <v-row
        flex
        style="
          align-items: center;
          justify-content: space-between;
          padding: 1rem;
        "
      >
        <v-btn
          text
          :href="'/people/' + post.user"
          color="#ccc"
          :to="'/people/' + post.user"
        >
          {{ post.user }}
        </v-btn>
        <v-icon
          x-small
          transparent
          :class="{ 'show-btns': hover }"
          color="grey"
        >
          mdi-heart
        </v-icon>
        <v-rating
          v-if="post.rating"
          v-model="post.rating"
          background-color="grey"
          color="grey"
          dense
          half-increments
          readonly
          small
          size="22"
        />
      </v-row>
      <Album
        v-if="post.type == 'albums'"
        :id="post.id"
        is-playable
        is-actionable
      />
      <Track
        v-if="post.type == 'songs'"
        :id="post.id"
        is-playable
        is-actionable
      />
      <Playlist
        v-if="post.type == 'playlists'"
        :id="post.id"
        is-playable
        is-actionable
      />
    </v-container>
    <v-row v-else class="review-contain">
      <v-container class="review-contain__music-item">
        <Album
          v-if="post.type == 'albums'"
          :id="post.id"
          is-playable
          is-actionable
        />
        <Track
          v-if="post.type == 'songs'"
          :id="post.id"
          is-playable
          is-actionable
        />
        <Playlist
          v-if="post.type == 'playlists'"
          :id="post.id"
          is-playable
          is-actionable
        />
      </v-container>
      <v-container class="review-contain__review-item">
      </v-container>
    </v-row>
  </v-container>
</template>

<script>
import Album from '~/components/MusicItem/Album.vue';
import Track from '~/components/MusicItem/Track.vue';
import Playlist from '~/components/MusicItem/Playlist.vue';
import PostHeader from '~/components/PostItem/PostHeader.vue';


export default {
  name: 'MusicReview',
  components: {
    PostHeader,
    Album,
    Track,
    Playlist,
  },
  props: {
    'post': {
      type: Object, 
      default: () => {},
    },
    'type': {
      type: String, 
      default: '',
    },
  },
  mounted () {
    console.log(this.post)
  }
};
</script>

<style scoped>
.post {
  width: 100%;
  margin: 0 auto;
  padding: 1rem;
  border-radius: 4px;
}

.review-contain {
  flex-direction: row;
  width: 100%;
}

.review-contain__music-item {
  width: 50%;
}

.review-contain__review-item {
  width: 50%;
}

</style>
