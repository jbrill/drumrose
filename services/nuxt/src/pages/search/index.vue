<template>
  <div class="profileContain">
    <div
      v-if="!loading"
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
          <nuxt-link to="artists/">{{ trackInfo.attributes.artistName }}</nuxt-link>
        </div>
      </div>
      <p>{{ trackInfo.attributes.releaseDate }}</p>
      <v-list><v-list-item v-for="genre in trackInfo.attributes.genreNames"><v-chip>{{ genre }}</v-chip></v-list-item></v-list>
    </div>
    <v-divider></v-divider>
			<v-btn @click="favoriteTrack" small tile dark>
					<v-icon x-small left>mdi-heart</v-icon> Favorite
			</v-btn>
			<v-btn small tile dark>
					<v-icon x-small left>mdi-plus</v-icon> Add to Queue
			</v-btn>
			<v-btn small tile dark>
					<v-icon x-small left>mdi-plus</v-icon> Add to Playlist
			</v-btn>
			<v-btn small tile dark>
					<v-icon x-small left>mdi-plus</v-icon> Add to Library
			</v-btn>
  </div>
</template>

<script>
import { postFavorite } from '~/api/api';

export default {
  data: () => ({
    trackInfo: {},
    loading: true,
  }),
  methods: {
    favoriteTrack: async function () {
      const favoritesResponse = await postFavorite(
        this.$auth.getToken('auth0'),
        { 'type': 'track', 'id': this.trackInfo.id }
      );
    }
  },
  async mounted () {
    const resp = await this.$store.getters.fetch(
      `/v1/catalog/us/songs/${this.$route.params.id}`
    );
    console.log(resp)
		this.trackInfo = resp.data[0];
    this.loading = false;
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
  width: auto;
  height: auto;
}
>>>.track-name {
  margin-bottom: 0;
}
</style>
