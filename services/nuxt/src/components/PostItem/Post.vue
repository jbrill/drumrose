<template>
  <v-container>
    <PostHeader
      v-if="post.user && (
        post.review || post.rating
      )"
      :user="post.user"
      :date="post.date"
      :type="post.postType"
      :rating="post.rating"
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
</template>

<script>
import Album from '~/components/MusicItem/Album.vue';
import Track from '~/components/MusicItem/Track.vue';
import Playlist from '~/components/MusicItem/Playlist.vue';
import PostHeader from '~/components/PostItem/PostHeader.vue';


export default {
  name: 'Post',
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
    console.log(this.post);
  },
};
</script>

<style scoped>
.post {
  width: 100%;
  margin: 0 auto;
  padding: 1rem;
  border-radius: 4px;
}
</style>
