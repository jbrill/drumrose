<template>
  <v-container>
    <v-tabs
      v-model="tab"
      centered
      background-color="transparent"
      color="white"
    >
      <v-tab
        v-for="(tabOption, index) in activeTabs"
        :key="index"
        :href="'#' + tabOption.link"
      >
        {{ tabOption.name }}
      </v-tab>
    </v-tabs>
    
    <v-tabs-items v-model="tab">
      <v-tab-item
        key="social"
        value="social"
      >
        <LoadingCircle
          v-if="loading" 
        />
        <v-responsive
          v-else
          class="overflow-y-auto"
        >
          <v-row no-gutters>
            <CarouselSection
              v-if="auth.loggedIn"
              title="Listen with Friends"
              :carousel-items="favorites"
            />
          </v-row>
          <v-divider />
          <CarouselSection
            title="Just Rated"
            :carousel-items="recentReviews"
          />
          <v-divider />
          <CarouselSection
            title="Popular Reviews"
            :carousel-items="recentReviews"
            type="reviews"
          />
        <!-- <Post
          v-for="(carouselItem, index) in recentReviews"
          :key="carouselItem.id"
          :index="index"
          :post="carouselItem"
        /> -->
          <!-- <MusicReview
            :key="carouselItem.id"
            :index="index"
            :post="carouselItem"
          /> -->
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
          <v-lazy
            v-for="(personalRecommendation, index) in recommendations"
            :key="`recommendation-${index}`"
            v-model="isActive"
            :options="{
              threshold: .5
            }"
            min-height="200"
            transition="fade-transition"
          >
            <CarouselSection
              :title="
                personalRecommendation.attributes.title.stringForDisplay
              "
              :carousel-items="
                personalRecommendation.relationships.contents.data
              "
            />
          </v-lazy>
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
    let reviewsResponse = [];
    let favoritesResponse = [];

    if (this.$store.state.auth && this.$store.state.auth.loggedIn) {
        try {
            favoritesResponse = await getFavorites(
              this.$auth.getToken('auth0')
            );
            reviewsResponse = await getTrackReviews(
              this.$auth.getToken('auth0')
            );
            this.loading = false;
        } catch (err) {
            console.error(err);
            this.loading = false;
            this.$toast.error(err.message);
        }
    }
    console.log("this.$auth.getToken('auth0')")
    console.log(this.$auth.getToken('auth0'))

    try {
      reviewsResponse = await getTrackReviews(
        this.$auth.getToken('auth0')
      );
      const reviewTrackList = await Promise.all(
        reviewsResponse.data.track_reviews.map( async review => {
            const attributes = await this.$store.getters.fetch(
              `/v1/catalog/us/songs/${review.track__apple_music_id}`
            );
            review.attributes = attributes.data[0].attributes;
            review.type = "songs";
            review.id = attributes.data[0].id;
            review.user = review.user__username;
            return review;
        })
      );
      this.recentReviews = reviewTrackList;
    } catch (err) {
        console.error(err);
        this.loading = false;
        this.$toast.error(err.message);
    }
    console.log(reviewsResponse)
    
    try {
        let storefront = `${this.$store.state.storefront}` || 'us';
        const trendingResponse = await this.$store.getters.fetch(
          `/v1/catalog/${storefront}/` +
          `charts?types=playlists,songs,albums`
        );
        this.trendingAlbumGroups = trendingResponse.results.albums;
        this.trendingPlaylistGroups = trendingResponse.results.playlists;
        this.trendingSongGroups = trendingResponse.results.songs;
    } catch (err) {
        this.loading = false;
        console.error(err);
        this.$toast.error(err.message);
    }

    if (this.$store.state.isAuthorized) {
        try {
            this.recommendations = await this.$store.getters['recommendations'];
        } catch (err) {
            console.error(err);
            this.loading = false;
            this.$toast.error(err.message);
        }
        try {
            this.listeningHistory = await this.$store.getters.recentlyPlayed;
        } catch(err) {
            console.error(err);
            this.loading = false;
            this.$toast.error(err.message);
        }
    }
    this.loading = false;
  },
  data () {
    return {
      tab: 'Social',
      tabs: [
        {
          'name': 'Social',
          'link': 'social',
        },
        {
          'name': 'Trending',
          'link': 'trending',
        },
        {
          'name': 'For You',
          'link': 'foryou',
        },
      ],
      socialCarousels: [
        {

        },
      ],
      loading: false,
      isActive: false,
      favorites: [],
      reviews: [],
      recentReviews: [],
      listeningHistory: [],
      recommendations: [],
      trendingAlbumGroups: [],
      trendingSongGroups: [],
      trendingPlaylistGroups: [],
    };
  },
  computed: {
    ...mapState(['isAuthorized', 'auth']),
    activeTabs () {
      return this.tabs.filter( tab => {
        return this.isActiveTab(tab.name);
      });
    },
  },
  methods: {
    isActiveTab (name) {
      switch (name) {
        case 'Trending':
          return true;
        case 'Social':
          return true;
        case 'For You':
          return this.$store.state.isAuthorized;
      }
    },
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
