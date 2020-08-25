<template>
  <div>
    <v-tabs
      v-model="tab"
      centered
      background-color="transparent"
      color="white"
    >
      <v-tab
        v-for="(tabOption, index) in tabs"
        :key="index"
      >
        {{ tabOption }}
      </v-tab>
    </v-tabs>
    <LoadingCircle v-if="loading" />
    <CarouselSection
      v-if="auth.loggedIn"
      title="Listen with Friends"
      :carousel-items="favorites"
    />
    <v-divider v-if="auth.loggedIn" />
    <CarouselSection
      title="Popular Reviews"
      :carousel-items="reviews"
    />
    <v-divider />
    <CarouselSection
      title="Just Rated"
      :carousel-items="recentReviews"
    />
    <v-divider />
    <CarouselSection
      v-if="auth.loggedIn"
      title="Fresh Reviews From Friends"
      :carousel-items="reviews"
    />
    <v-divider />
    <CarouselSection
      v-if="listeningHistory"
      title="Listening History"
      :carousel-items="listeningHistory"
    />
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex';
import CarouselSection from '~/components/CarouselSection';
import LoadingCircle from '~/components/LoadingCircle';

import { getFavorites, getTrackReviews } from '~/api/api';


export default {
  components: {
    CarouselSection,
    LoadingCircle,
  },
  async asyncData ({ store, $auth }) {
    if (store.auth && store.auth.loggedIn) {
      const favoritesResponse = await getFavorites(
        $auth.getToken('auth0')
      );
      const reviewsResponse = await getTrackReviews(
        $auth.getToken('auth0')
      );
      return {
        "favorites": favoritesResponse.data,
        "recentReviews": reviewsResponse.data,
      };
    }
    const reviewsResponse = await getTrackReviews(
      $auth.getToken('auth0')
    );
    const reviewTrackList = await Promise.all(
      reviewsResponse.data.track_reviews.map( async review => {
        const attributes = await store.getters.fetch(
          `/v1/catalog/us/songs/${review.track.apple_music_id}`
        );
        review.attributes = attributes.data[0].attributes;
        review.type = "songs";
        review.id = attributes.data[0].id;
        return review;
      })
    );
    return {
      "recentReviews": reviewTrackList,
    };
  },
  data () {
    return {
      tab: null,
      tabs: ['Social', 'Activity'],
      loading: false,
      favorites: [],
      reviews: [],
      recentReviews: [],
      listeningHistory: [],
      slides: [
        {
          'title': 'Social',
          'description': 'Share music with your friends.',
        },
        {
          'title': 'Smart',
          'description': 'Find new music with state ' +
                         'of the art recommendation systems.',
        },
      ],
    };
  },
  computed: {
    ...mapState(['isAuthorized', 'auth']),
  },
  async mounted () {
    try {
			this.listeningHistory = await this.$store.getters.recentlyPlayed;
		} catch(err) {
			console.error(err);
		}
  },
  methods: {
    ...mapMutations({
      setSnack: 'snackbar/setSnack',
    }),
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
