<template>
  <div>
    <v-divider v-if="auth.loggedIn"></v-divider>
    <CarouselSection v-for="trendingAlbumGroup in trendingAlbumGroups" :title="trendingAlbumGroup.name" :carouselItems="trendingAlbumGroup.data" />
    <v-divider></v-divider>
    <CarouselSection v-for="trendingPlaylistGroup in trendingPlaylistGroups" :title="trendingPlaylistGroup.name" :carouselItems="trendingPlaylistGroup.data" />
    <v-divider></v-divider>
    <CarouselSection v-for="trendingSongGroup in trendingSongGroups" :title="trendingSongGroup.name" :carouselItems="trendingSongGroup.data" />
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
      trendingAlbumGroups: [],
      trendingSongGroups: [],
      trendingPlaylistGroups: [],
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
  async created () {
    this.loading = true;
    const trending = await this.$store.getters.fetch(
      `/v1/catalog/us/charts?types=playlists,songs,artists,albums,stations`
    )
    console.log(trending)
    this.trendingAlbumGroups = trending.results.albums;
    this.trendingPlaylistGroups = trending.results.playlists;
    this.trendingSongGroups = trending.results.songs;
    this.setSnack("TEST YO")
    this.loading = false;
  },
};

</script>

<style scoped>
.recommended-title {
  padding-left: 1.5rem;
  padding-top: 3rem;
  text-align: center;
}
.tunes-contain {
  text-align: center;
  padding-top: 3rem;
  padding-bottom: 1rem;
}
.new-tracks-contain {
  padding-top: 2rem;
  width: 95%;
  margin: 0 auto;
}
</style>
