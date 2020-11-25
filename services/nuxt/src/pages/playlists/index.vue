<template>
  <div class="playlists-contain">
    <p class="playlists-description">
      Create a playlist of your favorite music...
    </p>
    <div class="create-playlist-button-contain">
      <v-btn
        class="add-post-button"
        color="primary"
        dark
        nuxt
        to="playlists/new"
        width="10rem"
      >
        Create playlist
      </v-btn>
    </div>
  </div>
</template>

<script>
import { getPlaylists } from '~/api/api.js';

export default {
  components: {
  },
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
.playlist-feed {
  display: grid;
  row-gap: 1rem;
}
</style>
