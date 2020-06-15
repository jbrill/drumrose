<template>
  <div>
    <div class="carousel-contain">
      <v-btn x-small text dark>
        Listen in with friends
      </v-btn>
      <carousel
        :touch-drag="false"
        :loop="true"
        :mouse-drag="false"
        :pagination-enabled="false"
        :navigation-enabled="true"
        :per-page="4"
      >
        <slide
          v-for="(favorite, index) in favorites"
          :key="favorite.id"
          data-index="index"
          data-name="favorite.id"
          @slideclick="handleSlideClick"
        >
          <Post
            :key="favorite.id"
            :index="index"
            :post="favorite"
            post-type="favorite"
            :type="favorite.favorite_type"
          />
        </slide>
      </carousel>
    </div>
    <div v-if="isAuthorized" class="carousel-contain">
      <v-btn x-small text dark>
        Trending Playlists
      </v-btn>
      <carousel
        :touch-drag="false"
        :loop="true"
        :mouse-drag="false"
        :pagination-enabled="false"
        :navigation-enabled="true"
        :per-page="4"
      >
        <slide
          v-for="(playlist, index) in trendingPlaylists"
          :key="playlist.id"
          data-index="index"
          data-name="playlist.id"
          @slideclick="handleSlideClick"
        >
          <Post
            :key="favorite.id"
            :index="index"
            :post="favorite"
            post-type="rating"
            :type="favorite.favorite_type"
          />
        </slide>
      </carousel>
    </div>
    <div class="carousel-contain">
      <v-btn x-small text dark>
        Popular Reviews
      </v-btn>
      <carousel
        :touch-drag="false"
        :loop="true"
        :mouse-drag="false"
        :pagination-enabled="false"
        :navigation-enabled="true"
        :per-page="4"
      >
        <slide
          v-for="(favorite, index) in favorites"
          :key="favorite.id"
          data-index="index"
          data-name="favorite.id"
          @slideclick="handleSlideClick"
        >
          <Post
            :key="favorite.id"
            :index="index"
            :post="favorite"
            post-type="rating"
            :type="favorite.favorite_type"
          />
        </slide>
      </carousel>
    </div>
    <div class="carousel-contain">
      <v-btn x-small text dark>
        Playlists from friends
      </v-btn>
      <carousel
        :touch-drag="false"
        :loop="true"
        :mouse-drag="false"
        :pagination-enabled="false"
        :navigation-enabled="true"
        :per-page="4"
      >
        <slide
          v-for="(favorite, index) in favorites"
          :key="favorite.id"
          data-index="index"
          data-name="favorite.id"
          @slideclick="handleSlideClick"
        >
          <Post
            :key="favorite.id"
            :index="index"
            :post="favorite"
            post-type="rating"
            :type="favorite.favorite_type"
          />
        </slide>
      </carousel>
    </div>
  </div>
</template>

<script>
import Post from '~/components/Post';
import { getFavorites } from '~/api/api';
import { mapState } from 'vuex';


export default {
  components: {
    Post,
  },
  computed: {
    ...mapState(['isAuthorized']),
  },
  async asyncData ({ store }) {
    const favoritesResponse = await getFavorites();
    const trendingPlaylistsResponse = await store.getters.fetch(
      `/v1/catalog/us/charts?types=playlists`
    );
    console.log(trendingPlaylistsResponse)
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
.VueCarousel-slide {
  width: 25%;
  padding: 1%;
}
.carousel-contain {
  padding: 2rem;
  border-bottom: 1px solid var(--primary-black-light);
  margin: 0 auto;
  width: 95%;
}
>>>.VueCarousel-navigation-prev {
  margin-left: 1rem;
  border: 1px solid #ccc;
}
>>>.VueCarousel-navigation-next {
  margin-right: 1rem;
  border: 1px solid #ccc;
}
</style>
