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
    <v-responsive
      class="overflow-y-auto"
    >
      <v-lazy
        v-for="
          rowIdx in Math.floor(playlists.length / 3)
        "
        :key="rowIdx"
        :options="{
          threshold: .5
        }"
        min-height="200"
        transition="fade-transition"
      >
        <v-row
          no-gutters
        >
          <v-col
            v-for="n in 3"
            :key="n"
            cols="12"
            sm="4"
          >
            <v-card
              v-if="(((rowIdx - 1) * 3) + n) <= (playlists.length - 1)"
              style="
                padding: 5%;
                background-color: transparent;
              "
              flat
            >
              <Playlist
                :id="playlists[((rowIdx - 1) * 3) + n].apple_music_id"
                is-playable
                is-actionable
              />
            </v-card>
          </v-col>
        </v-row>
      </v-lazy>
    </v-responsive>
  </div>
</template>

<script>
import { getPlaylists } from '~/api/api.js';
import Playlist from '~/components/MusicItem/Playlist.vue';


export default {
  components: {
    Playlist,
  },
  async asyncData () {
    const playlists = await getPlaylists();
    return {
      "playlists": playlists.data['playlists'],
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
