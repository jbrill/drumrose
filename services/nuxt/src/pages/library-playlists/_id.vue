<template>
  <v-responsive>
    <MusicPageHeader
      type="library-playlists"
    />
    <MusicPageRating />
    <v-container fluid>
      <h5 style="color: #ccc">
        <v-icon x-small>
          mdi-comment
        </v-icon>
        102 Reviews
      </h5>
      <v-divider />
    </v-container>
  </v-responsive>
</template>

<script>
import { postFavorite } from '~/api/api';
import MusicPageHeader from '~/components/MusicPageHeader';
import MusicPageRating from '~/components/MusicPageRating';

export default {
  components: {
    MusicPageHeader,
    MusicPageRating,
  },
  data: () => ({
    trackInfo: null,
    loading: true,
    playing: false,
    rating: 0.5,
    rules: [v => v.length <= 255 || 'Max 255 characters'],
    value: '',
    avg: 2.5,
    labels: [
      '0',
      '0.5',
      '1',
      '1.5',
      '2',
      '2.5',
      '3',
      '3.5',
      '4',
      '4.5',
      '5',
    ],
    values: [
      200,
      675,
      410,
      390,
      310,
      460,
      250,
      240,
      250,
      240,
      740,
    ],
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
  async mounted () {
    try {
      const resp = await this.$store.getters.fetch(
        `/v1/catalog/us/playlists/${this.$route.params.id}`
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
        'paylist': this.trackInfo.id,
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
