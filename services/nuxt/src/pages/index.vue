<template>
  <div>
    <LoadingCircle v-if="loading" />
    <CarouselSection v-if="auth.loggedIn" title="Listen with Friends" :carouselItems="favorites" />
    <v-divider v-if="auth.loggedIn"></v-divider>
    <CarouselSection title="Popular Reviews" :carouselItems="favorites" />
    <v-divider></v-divider>
    <CarouselSection v-if="auth.loggedIn" title="Fresh Reviews From Friends" :carouselItems="favorites" />
  </div>
</template>

<script>
import CarouselSection from '~/components/CarouselSection';
import LoadingCircle from '~/components/LoadingCircle';

import { getFavorites, postFavorite } from '~/api/api';
import { mapState, mapMutations } from 'vuex';


export default {
  components: {
    CarouselSection,
    LoadingCircle,
  },
  data () {
    return {
      loading: false,
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
      );
      store.dispatch("setFavoritedPosts", favoritesResponse.data);
      return {
        "favorites": favoritesResponse.data,
      };
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
