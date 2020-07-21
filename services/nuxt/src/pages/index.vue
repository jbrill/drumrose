<template>
  <div>
    <div v-if="!auth.loggedIn" class="welcome-contain">
        <v-carousel
          height="400"
          hide-delimiter-background
        >
        <v-carousel-item
          v-for="(slide, i) in slides"
          :key="i"
        >
          <v-sheet
            :color="colors[i]"
            height="100%"
          >
            <v-row
              class="fill-height"
              align="center"
              justify="center"
            >
              <div class="slide-title">{{ slide.title }}</div>
              <div class="slide-description">{{ slide.description }}</div>
              <v-btn color="var(--primary-red)">Get Started - IT'S FREE!</v-btn>
            </v-row>
          </v-sheet>
        </v-carousel-item>
      </v-carousel>
    </div>
    <CarouselSection v-if="auth.loggedIn" title="Listen with Friends" :carouselItems="favorites" />
    <v-divider v-if="auth.loggedIn"></v-divider>
    <CarouselSection v-if="auth.loggedIn" title="Fresh Playlists From Friends" :carouselItems="favorites" />
    <v-divider v-if="auth.loggedIn"></v-divider>
    <CarouselSection title="Popular Playlists" :carouselItems="favorites" />
    <v-divider></v-divider>
    <CarouselSection title="Popular Reviews" :carouselItems="favorites" />
    <v-divider></v-divider>
    <CarouselSection v-if="auth.loggedIn" title="Fresh Reviews From Friends" :carouselItems="favorites" />
    <Snackbar />
  </div>
</template>

<script>
import CarouselSection from '~/components/CarouselSection';
import Snackbar from '~/components/Snackbar';

import { getFavorites, postFavorite } from '~/api/api';
import { mapState, mapMutations } from 'vuex';


export default {
  components: {
    CarouselSection,
    Snackbar,
  },
  data () {
    return {
      colors: [
        'indigo',
        'warning',
        'pink darken-2',
        'red lighten-1',
        'deep-purple accent-4',
      ],
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
    console.log($auth.getToken('auth0'))
    const favoritesResponse = await getFavorites(
      $auth.getToken('auth0')
    );
    console.log(favoritesResponse)
    const trendingPlaylistsResponse = await store.getters.fetch(
      `/v1/catalog/us/charts?types=playlists`
    );
    store.dispatch("setFavoritedPosts", favoritesResponse.data);
    return {
      "favorites": favoritesResponse.data,
      "trendingPlaylists": trendingPlaylistsResponse.data,
    };
  },
  async fetch () {
    this.recommendations = await this.$store.getters['recommendations'];
    console.log(this.recommendations)
    this.setSnack("TEST YO")
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
