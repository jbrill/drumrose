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
    <div>
      <v-btn
        text
        nuxt
        to="playlists/popular&time=week"
        color="#ccc"
        class="playlists-popular"
      >
        Popular playlists this week
      </v-btn>
      <div class="playlist-feed">
        <Playlist
          v-for="(playlist, index) in playlists"
          :key="playlist.id"
          :index="index"
          :playlist="playlist"
        />
      </div>
      <v-btn
        text
        nuxt
        to="playlists/popular&time=week"
        color="#ccc"
        class="playlists-popular"
      >
        Playlists we think you'll enjoy
      </v-btn>
      <div class="playlist-feed">
        <Playlist
          v-for="(playlist, index) in playlists"
          :key="playlist.id"
          :index="index"
          :playlist="playlist"
        />
      </div>
      <v-btn
        text
        nuxt
        to="playlists/popular&time=week"
        color="#ccc"
        class="playlists-popular"
      >
        Playlists we've created for you
      </v-btn>
      <div class="playlist-feed">
        <Playlist
          v-for="(playlist, index) in playlists"
          :key="playlist.id"
          :index="index"
          :playlist="playlist"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Playlist from '~/components/MusicItem/Playlist';
import { getPlaylists } from '~/api/api.js';

export default {
  components: {
    Playlist,
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
