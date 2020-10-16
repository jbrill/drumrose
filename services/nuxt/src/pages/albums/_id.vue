<template>
  <div>
    <div
      v-if="!loading && trackInfo"
      class="track-contain"
    >
      <v-container>
        <v-row>
          <v-col cols="12" sm="8">
            <v-layout>
              <v-flex justify-space-between>
                <div>
                  <v-row>
                    <v-btn fab medium color="var(--primary-purple">
                      <v-icon>mdi-play</v-icon>
                    </v-btn>
                    <v-flex>
                      <h2
                        class="headline"
                      >
                        {{ trackInfo.attributes.name }}
                      </h2>
                      <nuxt-link
                        :to="'/artists/' + 
                          trackInfo.relationships.artists.data[0].id"
                      >
                        <p>{{ trackInfo.attributes.artistName }}</p>
                      </nuxt-link>
                    </v-flex>
                  </v-row>
                  <v-row>
                    <span>Released in <strong>
                      {{ trackInfo.attributes.releaseDate.split('-')[0] }}
                    </strong></span>
                  </v-row>
                  <v-divider />
                  <v-row height="30%" class="fill-height">
                    <v-chip
                      v-for="
                        (genre, genreIdx) in trackInfo.attributes.genreNames
                      "
                      :key="'genre' + genreIdx"
                      :to="'/genres/' + genre.replace(' ', '-').toLowerCase()"
                      nuxt
                      label
                      small
                    >
                      #{{ genre }}
                    </v-chip>
                  </v-row>
                </div>
              </v-flex>
            </v-layout>
          </v-col>
          <v-col cols="12" sm="3">
            <v-img height="auto" :src="appleImage" />
          </v-col>
        </v-row>
      </v-container>
    </div>
    <v-divider />
    <v-btn small tile dark @click="favoriteTrack">
      <v-icon x-small left>
        mdi-heart
      </v-icon> Favorite
    </v-btn>
    <v-btn small tile dark>
      <v-icon x-small left>
        mdi-plus
      </v-icon> Add to Queue
    </v-btn>
    <v-btn small tile dark>
      <v-icon x-small left>
        mdi-plus
      </v-icon> Add to Playlist
    </v-btn>
    <v-btn small tile dark>
      <v-icon x-small left>
        mdi-plus
      </v-icon> Add to Library
    </v-btn>
  </div>
</template>

<script>
import { postFavorite } from '~/api/api';


export default {
  data: () => ({
    trackInfo: null,
    loading: true,
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
    favoriteTrack: async function () {
      try {
        await postFavorite(
          this.$auth.getToken('auth0'),
          { 'type': 'track', 'id': this.trackInfo.id }
        );
      } catch (err) {
        console.error(err);
      }
    },
  },
};
</script>

<style scoped>
.track-contain {
  display: flex;
  padding: 2rem;
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
</style>
