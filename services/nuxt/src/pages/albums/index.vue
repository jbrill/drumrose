<template>
  <v-container>
    <v-row
      v-for="
        rowIdx in Math.floor(albums.length / 3)
      "
      :key="rowIdx"
      no-gutters
    >
      <v-col
        v-for="n in 3"
        :key="n"
        cols="12"
        sm="4"
      >
        <v-card
          v-if="(((rowIdx - 1) * 3) + n) <= (albums.length - 1)"
          style="padding: 5%"
        >
          <Album
            :id="albums[((rowIdx - 1) * 3) + n].apple_music_id"
            is-playable
            is-actionable
          />
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { getAlbums } from '~/api/api.js';
import Album from '~/components/MusicItem/Album.vue';

export default {
  components: {
    Album,
  },
  async asyncData () {
    const albums = await getAlbums();
    return {
      "albums": albums.data['albums'],
    };
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
