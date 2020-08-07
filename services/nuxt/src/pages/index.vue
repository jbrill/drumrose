<template>
  <div>
    <v-tabs
			v-model="tab"
			centered
      background-color="transparent"
      color="white"
		>
			<v-tab
				v-for="tab in tabs"
				:key="tab"
			>
        {{ tab }}
			</v-tab>
		</v-tabs>
    <LoadingCircle v-if="loading" />
    <CarouselSection v-if="auth.loggedIn" title="Listen with Friends" :carouselItems="favorites" />
    <v-divider v-if="auth.loggedIn"></v-divider>
    <CarouselSection title="Popular Reviews" :carouselItems="reviews" />
    <v-divider></v-divider>
    <CarouselSection title="Recent Reviews" :carouselItems="reviews" />
    <v-divider></v-divider>
    <CarouselSection v-if="auth.loggedIn" title="Fresh Reviews From Friends" :carouselItems="favorites" />
  </div>
</template>

<script>
import CarouselSection from '~/components/CarouselSection';
import LoadingCircle from '~/components/LoadingCircle';

import { getFavorites, postFavorite, getReviews } from '~/api/api';
import { mapState, mapMutations } from 'vuex';


export default {
  components: {
    CarouselSection,
    LoadingCircle,
  },
  data () {
    return {
      tab: null,
      tabs: ['Social', 'Activity'],
      loading: false,
      favorites: [],
      reviews: [],
      slides: [
        { 'title': 'Social', 'description': 'Share music with your friends.' },
        { 'title': 'Smart', 'description': 'Find new music with state of the art recommendation systems.'},
      ],
    }
  },
  computed: {
    ...mapState(['isAuthorized', 'auth']),
  },
  methods: {
    ...mapMutations({
      setSnack: 'snackbar/setSnack'
    })
  },
  async asyncData ({ store, $auth }) {
    if (store.auth && store.auth.loggedIn) {
      const favoritesResponse = await getFavorites(
        $auth.getToken('auth0')
      )
      const reviewsResponse = await getReviews(
        $auth.getToken('auth0')
      )
      return {
        "favorites": favoritesResponse.data,
        "reviews": reviewsResponse.data,
      }
    }
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
