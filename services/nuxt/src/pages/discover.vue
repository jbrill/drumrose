<template>
  <v-container>
    <v-tabs
      v-model="tab"
      centered
      background-color="transparent"
      color="white"
    >
      <v-tab
        v-if="isAuthorized"
        key="foryou"
        href="#foryou"
      >
        For you
      </v-tab>
      <v-tab
        key="trending"
        href="#trending"
      >
        Trending
      </v-tab>
    </v-tabs>
    <v-tabs-items v-model="tab">
      <v-tab-item
        key="foryou"
        value="foryou"
      >
        <LoadingCircle v-if="loading" />
        <v-responsive
          v-else
          class="overflow-y-auto"
        >
          <CarouselSection
            v-for="(personalRecommendation, index) in recommendations"
            :key="`recommendation-${index}`"
            :title="personalRecommendation.attributes.title.stringForDisplay"
            :carousel-items="personalRecommendation.relationships.contents.data"
          />
        </v-responsive>
      </v-tab-item>
      <v-tab-item
        key="trending"
        value="trending"
      >
        <LoadingCircle v-if="loading" />
        <v-responsive
          v-else
          class="overflow-y-auto"
        >
          <CarouselSection
            v-for="(trendingAlbumGroup, index) in trendingAlbumGroups"
            :key="`trending-album-${index}`"
            :title="trendingAlbumGroup.name"
            :carousel-items="trendingAlbumGroup.data"
          />
          <CarouselSection
            v-for="(trendingPlaylistGroup, index) in trendingPlaylistGroups"
            :key="`trending-playlist-${index}`"
            :title="trendingPlaylistGroup.name"
            :carousel-items="trendingPlaylistGroup.data"
          />
          <CarouselSection
            v-for="(trendingSongGroup, index) in trendingSongGroups"
            :key="`trending-track-${index}`"
            :title="trendingSongGroup.name"
            :carousel-items="trendingSongGroup.data"
          />
        </v-responsive>
      </v-tab-item>
    </v-tabs-items>
  </v-container>
</template>

<script>
import { mapState } from 'vuex';
import CarouselSection from '~/components/CarouselSection';
import LoadingCircle from '~/components/LoadingCircle';


export default {
  scrollToTop: true,
  components: {
    CarouselSection,
    LoadingCircle,
  },
  async fetch () {
    this.loading = true;
    try {
      const trendingResponse = await this.$store.getters.fetch(
        `/v1/catalog/${this.$store.state.storefront}/` +
        `charts?types=playlists,songs,albums`
      );
      this.trendingAlbumGroups = trendingResponse.results.albums;
      this.trendingPlaylistGroups = trendingResponse.results.playlists;
      this.trendingSongGroups = trendingResponse.results.songs;
    } catch (err) {
      this.$toast.error(err.message);
    }

    if (this.$store.state.isAuthorized) {
      try {
        this.recommendations = await this.$store.getters['recommendations'];
      } catch (err) {
        this.$toast.error(err.message);
      }
    }
    console.log(this.recommendations);
    this.loading = false;
  },
  data () {
    return {
      loading: false,
      recommendations: [],
      trendingAlbumGroups: [],
      trendingSongGroups: [],
      trendingPlaylistGroups: [],
      tab: 'For you',
    };
  },
  computed: {
    ...mapState(['isAuthorized', 'auth']),
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
