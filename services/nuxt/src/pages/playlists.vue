<template>
  <div class="playlists-contain">
    <p class="playlists-description">Create a playlist of your favorite music...</p>
    <div class="create-playlist-button-contain">
      <v-btn class="add-post-button" color="primary" dark nuxt
to="playlists/new" width="10rem">
        Create playlist
      </v-btn>
    </div>
    <div class="playlist-feed">
      <Playlist v-for="(playlist, index) in playlists" :index="index" :key="playlist.id" :playlist="playlist" />
    </div>
  </div>
</template>

<script>
import Playlist from '~/components/Playlist'
import { getPlaylists } from '~/api/api.js';

export default {
  name: 'Playlists',
  components: {},
  async asyncData () {
    const playlists = await getPlaylists();
    return { "playlists": playlists.data };
  },
};
</script>

<style>
.playlists-contain {
  text-align: center;
  padding-top: 3rem;
}
</style>
