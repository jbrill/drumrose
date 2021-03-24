<template>
  <v-container>
    <v-tabs
      v-model="tab"
      centered
      background-color="transparent"
      color="white"
    >
      <v-tab
        v-for="(tabOption, index) in tabs"
        :key="index"
        :href="'#' + tabOption.link"
      >
        {{ tabOption.name }}
      </v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab" style="background-color: transparent">
      <v-tab-item
        key="tracks"
        value="tracks"
      >
        <LoadingCircle
          v-if="loading" 
        />
        <v-responsive
          v-else
          class="overflow-y-auto"
          style="background-color: transparent"
        >
          <v-lazy
            v-for="
              rowIdx in Math.floor(tracks.length / 3)
            "
            :key="rowIdx"
            :options="{
              threshold: .5
            }"
            min-height="300px"
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
                  v-if="(((rowIdx - 1) * 3) + n) <= (tracks.length - 1)"
                  style="
                    padding: 5%;
                    background-color: transparent;
                  "
                  flat
                >
                  <Track
                    :id="tracks[((rowIdx - 1) * 3) + n].apple_music_id"
                    is-playable
                    is-actionable
                  />
                </v-card>
              </v-col>
            </v-row>
          </v-lazy>
        </v-responsive>
      </v-tab-item>
      <v-tab-item
        key="albums"
        value="albums"
      >
        <LoadingCircle v-if="loading" />
        <v-responsive
          v-else
          class="overflow-y-auto"
          color="transparent"
        >
          <v-lazy
            v-for="
              rowIdx in Math.floor(albums.length / 3)
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
                  v-if="(((rowIdx - 1) * 3) + n) <= (albums.length - 1)"
                  style="
                    padding: 5%;
                    background-color: transparent;
                  "
                  flat
                >
                  <Album
                    :id="albums[((rowIdx - 1) * 3) + n].apple_music_id"
                    is-playable
                    is-actionable
                  />
                </v-card>
              </v-col>
            </v-row>
          </v-lazy>
        </v-responsive>
      </v-tab-item>
    </v-tabs-items>
  </v-container>
</template>

<script>
import { getTracks, getAlbums } from '~/api/api.js';
import Track from '~/components/MusicItem/Track.vue';
import Album from '~/components/MusicItem/Album.vue';
import LoadingCircle from '~/components/LoadingCircle';


export default {
  components: {
    Track,
    Album,
    LoadingCircle,
  },
  async asyncData () {
    const trackResponse = await getTracks();
    const albumResponse = await getAlbums();

    let trackData = trackResponse.data['tracks'].filter( track => {
      return track.apple_music_id != null &&
        !track.apple_music_id.includes('-');
    });
    let albumData = albumResponse.data['albums'].filter( album => {
      // parsing to make sure it's clean
      return album.apple_music_id != null &&
        !album.apple_music_id.includes('-');
    });

    return {
      "tracks": trackData,
      "albums": albumData,
    };
  },
  data () {
    return {
      tab: 'Tracks',
      tabs: [
        {
          'name': 'Tracks',
          'link': 'tracks',
        },
        {
          'name': 'Albums',
          'link': 'albums',
        },
      ],
      loading: false,
    };
  },
};
</script>

<style>

</style>
