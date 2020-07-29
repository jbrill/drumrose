<template>
  <div class="post">
    <PostHeader
      v-if="post.user"
      :user="post.user"
      :date="post.date"
      :type="post.postType"
      :rating="post.rating"
    />
    <Album
      v-if="post.type == 'albums'"
      isPlayable
      isActionable
      :id="post.id"
      :attributes="post.attributes"
    />
    <Track
      v-if="post.type == 'songs'"
      isPlayable
      isActionable
      :id="post.id"
      :attributes="post.attributes"
    />
    <Artist
      v-if="post.type == 'artists'"
      isPlayable
      isActionable
      :id="post.id"
      :attributes="post.attributes"
    />
    <Station
      v-if="post.type == 'stations'"
      isPlayable
      isActionable
      :id="post.id"
      :attributes="post.attributes"
    />
    <Playlist
      v-if="post.type == 'playlists'"
      isPlayable
      isActionable
      :id="post.id"
      :attributes="post.attributes"
    />
  </div>
</template>

<script>
import Album from '~/components/MusicItem/Album.vue';
import Track from '~/components/MusicItem/Track.vue';
import Artist from '~/components/MusicItem/Artist.vue';
import Station from '~/components/MusicItem/Station.vue';
import Playlist from '~/components/MusicItem/Playlist.vue';
import PostHeader from '~/components/PostItem/PostHeader.vue';

import axios from 'axios';


export default {
  name: 'Post',
  components: {
    PostHeader,
    Album,
    Artist,
    Track,
    Station,
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
  created: function() {
    console.log(this.post)
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
