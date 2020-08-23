<template>
  <v-container>
    <v-tabs
      v-model="tab"
      centered
      background-color="transparent"
      color="white"
    >
      <v-tab
        href="#foryou"
        key="foryou"
        v-if="isAuthorized"
      >
        For you
      </v-tab>
      <v-tab
        href="#trending"
        key="trending"
      >
        Trending
      </v-tab>
    </v-tabs>
    <v-tabs-items v-model="tab">
			<v-tab-item
				key="foryou"
				value="foryou"
			>
			  <v-responsive
          class="overflow-y-auto"
        >
          <LoadingCircle v-if="loading" />
          <CarouselSection
            v-if="!loading"
            v-for="(personalRecommendation) in recommendations"
            :title="personalRecommendation.attributes.title.stringForDisplay"
            :carouselItems="personalRecommendation.relationships.contents.data"
          />
        </v-responsive>
      </v-tab-item>
			<v-tab-item
				key="trending"
				value="trending"
			>
				<CarouselSection v-if="!loading" v-for="trendingAlbumGroup in trendingAlbumGroups" :title="trendingAlbumGroup.name" :carouselItems="trendingAlbumGroup.data" />
				<CarouselSection v-if="!loading" v-for="trendingPlaylistGroup in trendingPlaylistGroups" :title="trendingPlaylistGroup.name" :carouselItems="trendingPlaylistGroup.data" />
				<CarouselSection v-if="!loading" v-for="trendingSongGroup in trendingSongGroups" :title="trendingSongGroup.name" :carouselItems="trendingSongGroup.data" />
      </v-tab-item>
    </v-tabs-items>
  </v-container>
</template>

<script>
import CarouselSection from '~/components/CarouselSection';
import LoadingCircle from '~/components/LoadingCircle';

import { getFavorites, postFavorite } from '~/api/api';
import { mapState, mapMutations } from 'vuex';


export default {
  scrollToTop: true,
  components: {
    CarouselSection,
    LoadingCircle,
  },
  data () {
    return {
      loading: false,
      recommendations: [],
      trendingAlbumGroups: [],
      trendingSongGroups: [],
      trendingPlaylistGroups: [],
      tab: 'For you',
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
  async fetch () {
    this.loading = true;
    const trending = await this.$store.getters.fetch(
      `/v1/catalog/us/charts?types=playlists,songs,artists,albums,stations`
    )
    this.trendingAlbumGroups = trending.results.albums;
    this.trendingPlaylistGroups = trending.results.playlists;
    this.trendingSongGroups = trending.results.songs;
    if (this.$store.state.isAuthorized) {
      this.recommendations = await this.$store.getters['recommendations'];
    }
    this.loading = false;
  },
};
</script>

<style scoped>
>>>.v-tabs-items {
  background-color: transparent;
}
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
