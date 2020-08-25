<template>
  <div class="profileContain">
    <div
      v-if="!loading && trackInfo"
      class="track-contain"
    >
      <img
        class="album-img"
        :src="trackInfo.attributes.artwork.url.replace(
          '{w}','250'
        ).replace(
          '{h}', '250'
        )"
      >
      <div class="track-info-contain">
        <p class="track-name">
          {{ trackInfo.attributes.name }}
        </p>
        <div class="artist-name">
          <nuxt-link to="artists/">
            {{ trackInfo.attributes.artistName }}
          </nuxt-link>
        </div>
      </div>
      <p>{{ trackInfo.attributes.releaseDate }}</p>
      <v-list>
        <v-list-item
          v-for="(genre, index) in trackInfo.attributes.genreNames"
          :key="index"
        >
          <v-chip>{{ genre }}</v-chip>
        </v-list-item>
      </v-list>
    </div>
    <v-divider />
    <v-btn small tile dark @click="favoriteTrack">
      <v-icon x-small left>
        mdi-heart
      </v-icon> Favorite
    </v-btn>
    <v-btn small tile dark>
      <v-icon x-small left>
        mdi-plus
      </v-icon> Add to Queue
    </v-btn>
    <v-btn small tile dark>
      <v-icon x-small left>
        mdi-plus
      </v-icon> Add to Playlist
    </v-btn>
    <v-btn small tile dark>
      <v-icon x-small left>
        mdi-plus
      </v-icon> Add to Library
    </v-btn>
  </div>
</template>

<script>
import { postFavorite } from '~/api/api';

export default {
  data: () => ({
    trackInfo: null,
    loading: true,
  }),
  async mounted () {
    try {
      const resp = await this.$store.getters.fetch(
        `/v1/catalog/us/songs/${this.$route.params.id}`
      );
      console.log(resp);
      this.trackInfo = resp.data[0];
      this.loading = false;
    } catch (err) {
      this.loading = false;
      console.error(err);
    }
  },
  methods: {
    favoriteTrack: async function () {
      try {
        await postFavorite(
          this.$auth.getToken('auth0'),
          { 'type': 'track', 'id': this.trackInfo.id }
        );
      } catch (err) {
        console.error(err);
      }
    },
  },
};
</script>

<style scoped>
.track-contain {
  display: flex;
  padding: 2rem;
}
.track-info-contain {
  align-self: center;
  justify-content: flex-end;
  padding-left: 2rem;
}
.album-img {
  width: 100%;
  height: 100%;
}
>>>.track-name {
  margin-bottom: 0;
}
</style>
