<template>
  <div>
    <div v-if="!auth.loggedIn" class="welcome-contain">
      <div><h4>Explore your fandom</h4></div>
      <img class="welcome-contain-image" src="~/assets/welcome-page.png" />
    </div>
    <CarouselSection title="Listen with Friends" :carouselItems="favorites" />
    <CarouselSection title="Fresh Playlists From Friends" :carouselItems="favorites" />
    <CarouselSection title="Popular Reviews" :carouselItems="favorites" />
    <CarouselSection title="Fresh Reviews From Friends" :carouselItems="favorites" />
  </div>
</template>

<script>
import Post from '~/components/Post';
import { getFavorites } from '~/api/api';
import { mapState } from 'vuex';
import CarouselSection from '~/components/CarouselSection';


export default {
  components: {
    Post,
    CarouselSection,
  },
  computed: {
    ...mapState(['isAuthorized', 'auth']),
  },
  async asyncData ({ store, $auth }) {
    const favoritesResponse = await getFavorites(
      $auth.getToken('auth0')
    );
    const trendingPlaylistsResponse = await store.getters.fetch(
      `/v1/catalog/us/charts?types=playlists`
    );
    store.dispatch("setFavoritedPosts", favoritesResponse.data);
    return {
      "favorites": favoritesResponse.data,
      "trendingPlaylists": trendingPlaylistsResponse.data,
    };
  },
  methods: {
		handleSlideClick (dataset) {
			console.log(dataset.index, dataset.name);
		},
	},
};
</script>

<style scoped>
.welcome-contain {
  max-height: 45%;
  overflow: hidden;
  border-bottom: 1px solid var(--primary-red);
}
.welcome-contain-image {
  width: 100%;
  height: auto;
}
</style>
