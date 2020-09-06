<template>
  <div class="post">
    <PostHeader
      v-if="post.user"
      :user="post.user"
      :date="post.date"
      :type="post.postType"
    />
    <Album
      v-if="post.type == 'albums'"
      :id="post.id"
      is-playable
      is-actionable
      :attributes="post.attributes"
    />
    <Track
      v-if="post.type == 'songs'"
      is-playable
      is-actionable
      :id="post.id"
    />
    <Playlist
      v-if="post.type == 'playlists'"
      :id="post.id"
      is-playable
      is-actionable
      :attributes="post.attributes"
    />
  </div>
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
};
</script>

<style scoped>
.post {
  width: 100%;
  margin: 0 auto;
  padding: 1rem;
  display: inline;
}
</style>
