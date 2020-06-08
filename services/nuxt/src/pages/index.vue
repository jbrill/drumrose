<template>
  <div>
    <h3 class="social-title">
      Social
    </h3>
    <h6 class="social-title">
      Listen in with friends
    </h6>
    <div class="carousel-contain">
      <v-btn text dark>
        FAVORITES
      </v-btn>
      <carousel
        :touch-drag="false"
        :loop="true"
        :mouse-drag="false"
        :pagination-enabled="false"
        :navigation-enabled="true"
        :per-page="3"
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
    <div class="carousel-contain">
      <v-btn text dark>
        RATINGS
      </v-btn>
      <carousel
        :touch-drag="false"
        :loop="true"
        :mouse-drag="false"
        :pagination-enabled="false"
        :navigation-enabled="true"
        :per-page="3"
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


export default {
  components: {
    Post,
  },
  async asyncData ({ store }) {
    const favoritesResponse = await getFavorites();

    store.dispatch("setFavoritedPosts", favoritesResponse.data);

    return {
      "favorites": favoritesResponse.data,
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
  width: 33%;
  padding: 1%;
}
.carousel-contain {
  padding: 1rem;
  margin: 0 auto;
  width: 95%;
}
</style>
