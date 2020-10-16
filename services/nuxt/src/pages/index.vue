<template>
  <v-container>
    <v-tabs
      v-model="tab"
      centered
      background-color="transparent"
      color="white"
    >
      <v-tab
        v-for="(tabOption, index) in tabs"
        :key="index"
        :href="'#' + tabOption.replace(/\s/g, '').toLowerCase()"
      >
        {{ tabOption }}
      </v-tab>
    </v-tabs>
    
    <v-tabs-items v-model="tab">
      <v-tab-item
        key="social"
        value="social"
      >
        <LoadingCircle v-if="loading" />
        <v-responsive
          v-else
          class="overflow-y-auto"
        >
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
          <v-divider v-if="listeningHistory && listeningHistory.length" />
          <CarouselSection
            v-if="listeningHistory && listeningHistory.length"
            title="Listening History"
            :carousel-items="listeningHistory"
          />
        </v-responsive>
      </v-tab-item>
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

import { getFavorites, getTrackReviews } from '~/api/api';


export default {
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
      tab: 'Social',
      tabs: ['Social', 'Trending', 'For you'],
      loading: false,
      favorites: [],
      reviews: [],
      recentReviews: [],
      listeningHistory: [],
      recommendations: [],
      trendingAlbumGroups: [],
      trendingSongGroups: [],
      trendingPlaylistGroups: [],
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
    if (this.$store.state.isAuthorized) {
      this.loading = true;
      try {
        this.listeningHistory = await this.$store.getters.recentlyPlayed;
      } catch(err) {
        console.error(err);
        this.$toast.error(err.message);
      }
      this.loading = false;
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
>>>.v-tabs-items {
  background-color: transparent;
  padding-top: 5vh;
}
</style>
