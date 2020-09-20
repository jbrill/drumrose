<template>
  <div>
    <v-tabs
      v-model="selectedLibraryItem"
      background-color="transparent"
      dark
      color="white"
    >
      <v-tab
        v-for="(musicItem, index) in musicSelections"
        :key="index"
      >
        {{ item }}
      </v-tab>
    </v-tabs>
  
    <v-tabs-items v-model="musicSelections">
      <v-tab-item
        v-for="musicSelection in musicSelections"
        :key="musicSelection"
      />
    </v-tabs-items>
    <div class="library-contain">
      <LoadingCircle v-if="loading" />
      <v-container
        v-if="activeCollection === 'artists' && !loading"
        fluid
        grid-list-md
      >
        <v-row
          v-for="(artistCollectionGroup, index) in Math.floor(
            artistCollection.length / 3
          )"
          :key="index"
          align="start"
          no-gutters
          style="height: 150px;"
        >
          <v-col
            v-for="n in 3"
            :key="n"
            cols="12"
            md="4"
          >
            <v-card dark>
              <div class="d-flex flex-no-wrap justify-space-between">
                <div>
                  <v-card-title
                    class="headline"
                    v-text="artistCollection[
                      artistCollectionGroup + n
                    ].attributes.name"
                  />
                </div>

                <v-avatar
                  class="ma-3"
                  tile
                >
                  <v-img />
                </v-avatar>
              </div>
            </v-card>
            </v-flex>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script>
import { mergeWith } from 'lodash';
import { mapState } from 'vuex';
import LoadingCircle from '~/components/LoadingCircle';

export default {
  components: {
    LoadingCircle,
  },
  data () {
    return {
      item: null,
      error: null,
      loading: true,
      offset: 0,
      collection: [],
      selectedLibraryItem: 'Artists',
      musicSelections: [
				'Artists',
				'Tracks',
				'Albums',
				'Playlists',
			],
      numArtistOptions: 27,
    };
  },
  computed: {
    ...mapState(['activeCollection']),
  },
  async mounted ({ store }) {
    // Load the collection
    this.loading = true;
    this.error = null;
    this.artistCollection = [];
    this.trackCollection = [];
    this.albumCollection = [];
    this.playlistCollection = [];
    this.offset = 0;
    let activeCollection = this.$store.state.activeCollection;
    try {
      const res = await this.$store.getters.get(
        true,
        activeCollection,
        null,
        mergeWith({ limit: 100 }, { offset: this.offset })
      );
      if (this.activeCollection === 'artists') {
        this.artistCollection = this.artistCollection.concat(res);
      }
    } catch (err) {
      this.$toast.show(err);
    }

    this.loading = false;
  },
  methods: {
    changeCollection: function () {
      this.$store.commit('activeCollection', 'songs');
    },
  },
};
</script>

<style scoped>
.library-contain {
  display: flex;
  width: 80%;
  height: 100%;
  margin: 0 auto;
}
>>>.v-btn--fab.v-size--x-small {
  height: 20px;
  width: 20px;
}
>>>.artist-menu-options {
  flex-direction: column;
  position: fixed;
  height: 100vh;
}
>>>.v-slide-group__content {
  justify-content: center;
}
>>>.v-btn {
  border-radius: 2rem !important;
}
</style>
