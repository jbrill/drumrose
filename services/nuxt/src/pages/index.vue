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
        key="reviews"
        value="reviews"
      >
        <LoadingCircle
          v-if="loading" 
        />
        <v-responsive
          v-else
          class="overflow-y-auto"
        >
          <v-row
            v-if="auth.loggedIn"
            no-gutters
          >
            <span style="text-align: center; width: 100%; font-size: 1.5rem;">
              Hi again, <nuxt-link
                :to="
                  `people/${auth.user['https://django-server:8000/handle']}`
                "
                class="nuxt-link-active"
              >
                {{ auth.user['https://django-server:8000/handle'] }}
              </nuxt-link>! Here's what you may have missed.
            </span>
          </v-row>
          <v-row no-gutters>
            <CarouselSection
              v-if="auth.loggedIn && favorites.length"
              title="Tracks Your Friends Love"
              :carousel-items="favorites"
              type="favorites"
            />
          </v-row>
          <CarouselSection
            v-if="auth.loggedIn && reviews.length"
            title="Fresh Reviews From Friends"
            :carousel-items="reviews"
          />
          <v-divider v-if="recentReviews && recentReviews.length" />
          <p class="font-weight-bold overline">
            Recently reviewed playlists
          </p>
          <v-row
            no-gutters
          >
            <v-col
              v-for="(review, reviewKey) in recentReviews.slice(0, 6)"
              :key="reviewKey"
              cols="12"
              sm="2"
              style="padding: 1vw"
            >
              <v-card>
                <Track
                  :id="review.track__apple_music_id"
                  is-playable
                  type="review"
                  :user="review.user__username"
                  :is-actionable="false"
                />
              </v-card>
            </v-col>
          </v-row>
          <p class="font-weight-bold overline">
            Recently reviewed albums
          </p>
          <v-row
            no-gutters
          >
            <v-col
              v-for="(review, reviewKey) in recentReviews.slice(0, 6)"
              :key="reviewKey"
              cols="12"
              sm="2"
              style="padding: 1vw"
            >
              <v-card>
                <Track
                  :id="review.track__apple_music_id"
                  is-playable
                  type="review"
                  :user="review.user__username"
                  :is-actionable="false"
                />
              </v-card>
            </v-col>
          </v-row>
          <p class="font-weight-bold overline">
            Recently reviewed tracks
          </p>
          <v-row
            no-gutters
          >
            <v-col
              v-for="(review, reviewKey) in recentReviews.slice(0, 6)"
              :key="reviewKey"
              cols="12"
              sm="2"
              style="padding: 1vw"
            >
              <v-card>
                <Track
                  :id="review.track__apple_music_id"
                  is-playable
                  type="review"
                  :user="review.user__username"
                  :is-actionable="false"
                />
              </v-card>
            </v-col>
          </v-row>
          <v-divider v-if="popularTrackReviews && popularTrackReviews.length" />
          <CarouselSection
            v-if="popularTrackReviews && popularTrackReviews.length"
            title="Popular Track Reviews"
            :carousel-items="popularTrackReviews"
            type="reviews"
          />
          <v-divider v-if="popularAlbumReviews && popularAlbumReviews.length" />
          <CarouselSection
            v-if="popularAlbumReviews && popularAlbumReviews.length"
            title="Popular Album Reviews"
            :carousel-items="popularAlbumReviews"
            type="reviews"
          />
          <v-divider v-if="popularPlaylistReviews && popularPlaylistReviews.length" />
          <CarouselSection
            v-if="popularPlaylistReviews && popularPlaylistReviews.length"
            title="Popular Playlist Reviews"
            :carousel-items="popularPlaylistReviews"
            type="reviews"
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
import Track from '~/components/MusicItem/Track';

import { getFavoritedTracks, getTrackReviews } from '~/api/api';


export default {
  components: {
    CarouselSection,
    LoadingCircle,
    Track,
  },
  async asyncData ({ store, $auth }) {
    console.log($auth['https://django-server:8000/handle'])
    let reviewsResponse = [];
    let favoritedTracksResponseList = [];
    let reviewTrackList = [];
    let favoritesResponse = [];
    let trendingAlbumGroups = [];
    let trendingPlaylistGroups = [];
    let trendingSongGroups = [];
    let popularAlbumReviews = [];
    let popularPlaylistReviews = [];
    let popularTrackReviews = [];
    let listeningHistory = [];
    let recommendations = [];
    let recentReviews = [];

    // logged into drumrose
    if ($auth && $auth.loggedIn) {
        try {
          favoritesResponse = await getFavoritedTracks(
            $auth.getToken('auth0')
          );
          console.log(favoritesResponse.data)
          favoritedTracksResponseList = await Promise.all(
            favoritesResponse.data.favorited_tracks.map( async track => {
                const attributes = await store.getters.fetch(
                  `/v1/catalog/us/songs/${track.song.apple_music_id}`
                );
                track.attributes = attributes.data[0].attributes;
                track.type = "songs";
                track.id = attributes.data[0].id;
                track.user = track.user.username;
                return track;
            })
          );
        } catch (err) {
            console.error(err);
            // this.loading = false;
            // this.$toast.error(err.message);
        }
    }
    reviewsResponse = await getTrackReviews();
    reviewTrackList = await Promise.all(
      reviewsResponse.data.track_reviews.map( async review => {
          const attributes = await store.getters.fetch(
            `/v1/catalog/us/songs/${review.track__apple_music_id}`
          );
          review.attributes = attributes.data[0].attributes;
          review.type = "songs";
          review.id = attributes.data[0].id;
          review.user = review.user__username;
          return review;
      })
    );
    recentReviews = reviewTrackList;
    console.log(recentReviews)

    try {
        let storefront = `${store.state.storefront}` || 'us';
        const trendingResponse = await store.getters.fetch(
          `/v1/catalog/${storefront}/` +
          `charts?types=playlists,songs,albums`
        );
        trendingAlbumGroups = trendingResponse.results.albums;
        trendingPlaylistGroups = trendingResponse.results.playlists;
        trendingSongGroups = trendingResponse.results.songs;
    } catch (err) {
        // this.loading = false;
        console.error(err);
        // this.$toast.error(err.message);
    }

    if (store.state.isAuthorized) {
        try {
            recommendations = await store.getters['recommendations'];
        } catch (err) {
            console.error(err);
            // this.loading = false;
            // this.$toast.error(err.message);
        }
        try {
            listeningHistory = await store.getters.recentlyPlayed;
        } catch(err) {
            console.error(err);
            // this.loading = false;
            // this.$toast.error(err.message);
        }
        return {
          'recentReviews': recentReviews,
          'popularTrackReviews': popularTrackReviews,
          'popularAlbumReviews': popularAlbumReviews,
          'popularPlaylistReviews': popularPlaylistReviews,
          'favorites': favoritedTracksResponseList,
          'listeningHistory': listeningHistory,
          'recommendations': recommendations,
          'trendingAlbumGroups': trendingAlbumGroups,
          'trendingSongGroups': trendingSongGroups,
          'trendingPlaylistGroups': trendingPlaylistGroups,
      };
    }
    return {
      'recentReviews': recentReviews,
      'popularTrackReviews': popularTrackReviews,
      'popularAlbumReviews': popularAlbumReviews,
      'popularPlaylistReviews': popularPlaylistReviews,
      'favorites': favoritedTracksResponseList,
      'listeningHistory': listeningHistory,
      'recommendations': recommendations,
      'trendingAlbumGroups': trendingAlbumGroups,
      'trendingSongGroups': trendingSongGroups,
      'trendingPlaylistGroups': trendingPlaylistGroups,
    };
    // this.loading = false;
  },
  data () {
    return {
      tab: 'Reviews',
      tabs: [
        {
          'name': 'Reviews',
          'link': 'reviews',
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
      popularTrackReviews: [],
      popularAlbumReviews: [],
      popularPlaylistReviews: [],
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
        case 'Reviews':
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
.nuxt-link-active {
  color: var(--primary-yellow);
  font-weight: 600;
}
</style>
