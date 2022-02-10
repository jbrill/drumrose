<template>
  <v-container>
    <!-- favorite -->
    <v-container
      v-if="post.user && !(
        post.review
      )"
    >
      <v-btn
        text
        :href="'/people/' + user"
        color="#ccc"
        :to="'/people/' + user"
      >
        {{ post.user }}
      </v-btn>
      <v-icon
        small
        transparent
        :class="{ 'show-btns': hover }"
      >
        mdi-heart
      </v-icon>
      <PostHeader
        v-if="post.rating"
        :user="post.user"
        :date="post.date"
        :type="post.postType"
        :rating="post.rating"
        :review="post.review"
      />
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
