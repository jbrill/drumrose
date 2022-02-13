<template>
  <v-responsive>
    <MusicPageHeader
      v-if="!loading"
      type="songs"
      :avg="average"
      :rating-values="ratingValues"
      :did-favorite="didFavorite"
    />
    <v-skeleton-loader
      v-else
      class="mx-auto"
      type="paragraph"
    />
    <v-container fluid>
      <h5 style="color: #ccc">
        <v-icon x-small>
          mdi-comment  
        </v-icon>
        <span
          v-if="numReviews === 1"
          class="overline"
        >
          {{ numReviews }} Review
        </span>
        <span v-else class="overline">{{ numReviews }} Reviews</span>
      </h5>
      <v-divider />
      <v-container v-if="numReviews === 0">
        <p class="playlists-description">
          No reviews yet... be the first to write one!
        </p>
        <div class="create-playlist-button-contain">
          <v-btn
            class="add-post-button"
            color="primary"
            dark
            nuxt
            width="10rem"
          >
            Write review
          </v-btn>
        </div>
      </v-container>
    </v-container>
  </v-responsive>
</template>

<script>
import {
  postFavorite, getTrackDetail, createTrack,
} from '~/api/api';
import MusicPageHeader from '~/components/MusicPageHeader';


export default {
  components: {
    MusicPageHeader,
  },
  data: () => ({
    trackInfo: null,
    loading: true,
    playing: false,
    average: null,
    didFavorite: false,
    ratingValues: [],
    numReviews: 0,
  }),
  computed: {
    appleImage () {
      return this.trackInfo.attributes.artwork.url.replace(
        '{w}', '2500'
      ).replace(
        '{h}', '2500'
      );
    },
  },
  async created () {
    try {
      this.loading = true;
      const resp = await getTrackDetail(
        this.$auth.getToken('auth0'),
        this.$route.params.id
      );
      this.average = resp.data.track.review_summary.total_reviews > 0 ? 
        resp.data.track.review_summary.average_review : 0.0;
      for (let ratingKey in resp.data.track.review_summary.totals_per_rating) {
        this.ratingValues.push(
          resp.data.track.review_summary.totals_per_rating[ratingKey]
        );
      }
      this.loading = false;
      this.didFavorite = resp.data.track.favorited;
      this.numReviews = resp.data.track.review_summary.total_reviews;
    } catch (err) {
      if (err.response.status === 409) {
        try {
          await createTrack(
            this.$auth.getToken('auth0'),
            {
              'id': this.$route.params.id,
            }
          );
          this.average = 0.0;
        } catch (err) {
          console.error(err);
        }
      }
      this.loading = false;
      console.error(err);
    }
  },
  async mounted () {
    try {
      const resp = await this.$store.getters.fetch(
        `/v1/catalog/us/songs/${this.$route.params.id}`
      );
      console.log(resp);
      this.trackInfo = resp.data[0];
      console.log(this.trackInfo)
      this.loading = false;
    } catch (err) {
      this.loading = false;
      console.error(err);
    }
  },
  methods: {
    async favoriteTrack () {
      try {
        await postFavorite(
          this.$auth.getToken('auth0'),
          { 'type': 'track', 'id': this.trackInfo.id }
        );
      } catch (err) {
        console.error(err);
        this.$toast.error(err.message);
      }
    },
    async playTrack () {
      await this.$store.dispatch("setQueue", {
        'song': this.trackInfo.id,
      });
      await this.$store.dispatch("play");
      this.playing = true;
    },
    async pauseTrack () {
      await this.$store.dispatch("pause");
      this.playing = false;
    },
  },
};
</script>

<style scoped>
.track-contain {
  display: flex;
}
.track-info-contain {
  align-self: center;
  justify-content: flex-end;
  padding-left: 2rem;
}
.album-img {
  width: 100%;
  height: 100%;
}
>>>.track-name {
  margin-bottom: 0;
}
.album-name {
  font-weight: bolder;
  color: #ccc;
}
.buttons-contain {
  display: flex;
}
.content-contain {
  align-items: center;
  justify-content: space-around;
}
.v-chip {
  margin: 5px;
}
.buttons-contain > * {
  margin: 5px;
}
</style>
