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
    <CarouselSection title="Just Rated" :carouselItems="recentReviews" />
    <v-divider></v-divider>
    <CarouselSection v-if="auth.loggedIn" title="Fresh Reviews From Friends" :carouselItems="reviews" />
    <v-divider></v-divider>
    <CarouselSection v-if="listeningHistory" title="Listening History" :carouselItems="listeningHistory" />
  </div>
</template>

<script>
import CarouselSection from '~/components/CarouselSection';
import LoadingCircle from '~/components/LoadingCircle';
import Album from '~/components/MusicItem/Album';

import { getFavorites, postFavorite, getTrackReviews } from '~/api/api';
import { mapState, mapMutations } from 'vuex';


export default {
  components: {
    CarouselSection,
    LoadingCircle,
    Album,
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
  async mounted() {
    try {
			this.listeningHistory = await this.$store.getters.recentlyPlayed;
		} catch(err) {
			console.error(err)
		}
  },
  async asyncData ({ store, $auth }) {
    if (store.auth && store.auth.loggedIn) {
      const favoritesResponse = await getFavorites(
        $auth.getToken('auth0')
      )
      const reviewsResponse = await getTrackReviews(
        $auth.getToken('auth0')
      )
      return {
        "favorites": favoritesResponse.data,
        "recentReviews": reviewsResponse.data,
      }
    }
    const reviewsResponse = await getTrackReviews(
      $auth.getToken('auth0')
    )
    const reviewTrackList = await Promise.all(reviewsResponse.data.track_reviews.map( async (review) => {
      const attributes = await store.getters.fetch(
        `/v1/catalog/us/songs/${review.track.apple_music_id}`
      )
      review.attributes = attributes.data[0].attributes;
      review.type = "songs";
      review.id = attributes.data[0].id;
      return review;
    }))
    console.log(reviewTrackList)
    return {
      "recentReviews": reviewTrackList,
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
