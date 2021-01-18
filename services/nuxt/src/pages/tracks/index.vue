<template>
  <div class="playlists-contain">
    <v-row
      v-for="
        rowIdx in Math.floor(tracks.length / 3)
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
          v-if="(((rowIdx - 1) * 3) + n) <= (tracks.length - 1)"
        >
          <Track
            :id="tracks[((rowIdx - 1) * 3) + n].apple_music_id"
            is-playable
            is-actionable
          />
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { getTracks } from '~/api/api.js';
import Track from '~/components/MusicItem/Track.vue';


export default {
  components: {
    Track,
  },
  async asyncData () {
    const tracks = await getTracks();
    return {
      "tracks": tracks.data['tracks'],
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
