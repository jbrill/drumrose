<template>
  <v-responsive>
    <MusicPageHeader
      v-if="!loading"
      type="albums"
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
        <span v-if="numReviews === 1" class="overline">{{ numReviews }} Review</span>
        <span v-else class="overline">{{ numReviews }} Reviews</span>
      </h5>
      <v-divider />
    </v-container>
  </v-responsive>
</template>

<script>
import { getAlbumDetail, createAlbum } from '~/api/api';
import MusicPageHeader from '~/components/MusicPageHeader';


export default {
  components: {
    MusicPageHeader,
  },
  data: () => ({
    trackInfo: null,
    loading: true,
    playing: false,
    average: 0.0,
    ratingValues: [],
    numReviews: 0,
    didFavorite: false,
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
      const resp = await getAlbumDetail(
        this.$auth.getToken('auth0'),
        this.$route.params.id,
      );
      this.average = resp.data.album.review_summary.total_reviews > 0 ?
        resp.data.album.review_summary.average_review : 0.0;
      for (let ratingKey in resp.data.album.review_summary.totals_per_rating) {
        this.ratingValues.push(
          resp.data.album.review_summary.totals_per_rating[ratingKey]
        );
      }
      this.didFavorite = resp.data.album.favorited;
      this.loading = false;
      this.numReviews = resp.data.album.review_summary.total_reviews;
    } catch (err) {
      console.log(err.response)
      if (err.response.status === "409") {
        try {
          await createAlbum(
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
        `/v1/catalog/us/albums/${this.$route.params.id}`
      );
      console.log(resp);
      this.trackInfo = resp.data[0];
      this.loading = false;
    } catch (err) {
      this.loading = false;
      console.error(err);
    }
  },
  methods: {
    async playTrack () {
      await this.$store.dispatch("setQueue", {
        'album': this.trackInfo.id,
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
