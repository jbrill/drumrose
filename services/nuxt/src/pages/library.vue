<template>
  <div>
    <v-tabs
        v-model="selectedLibraryItem"
        background-color="transparent"
        dark
      >
        <v-tab
          v-for="item in musicSelections"
          :key="item"
        >
          {{ item }}
        </v-tab>
      </v-tabs>
  
      <v-tabs-items v-model="musicSelections">
        <v-tab-item
          v-for="item in musicSelections"
          :key="item"
        >
        </v-tab-item>
      </v-tabs-items>
    <div>
			<v-btn-toggle borderless rounded background-color="transparent" class="artist-menu-options">
        <v-hover v-for="(artistOption, artistIndex) in artistOptions">
          <v-btn slot-scope="{ hover }" :class="`${hover ? 'activeArtistOptionButton': 'artistOptionButton'}`" x-small fab>{{ artistOption }}</v-btn>
        </v-hover>
      </v-btn-toggle>
    </div>
    <div class="library-contain">
      <LoadingCircle v-if="loading" />
      <v-container v-if="activeCollection === 'artists' && !loading" fluid grid-list-md>
        <v-row align="start"
          no-gutters
          style="height: 150px;"
          v-for="artistCollectionGroup in Math.floor(artistCollection.length / 3)"
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
											v-text="artistCollection[artistCollectionGroup + n].attributes.name"
										></v-card-title>

									</div>

									<v-avatar
										class="ma-3"
										tile
									>
							    	<v-img ></v-img>
							    </v-avatar>
						    </div>
						  </v-card>
					  </v-flex>
          </v-col>
		    	</v-row>
		    </v-container>
			</v-card>
    </div>
  </div>
</template>

<script>
import Raven from 'raven-js';
import { mergeWith } from 'lodash';
import { mapState } from 'vuex';
import LoadingCircle from '~/components/LoadingCircle';

export default {
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
      artistOptions: [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '#'
      ],
    };
  },
  components: {
    LoadingCircle,
  },
  computed: mapState(['activeCollection']),
  methods: {
    changeCollection: function() {
      console.log("CHANGING")
      this.$store.commit('activeCollection', 'songs')
    }
  },
  async mounted () {
    // Load the collection
    this.loading = true;
    this.error = null;
    this.artistCollection = [];
    this.trackCollection = [];
    this.albumCollection = [];
    this.playlistCollection = [];
    this.offset = 0;
    const res = await this.$store.getters.get(
      true,
      this.$store.state.activeCollection,
      null,
      mergeWith({ limit: 100 }, { offset: this.offset })
    );
    if (this.activeCollection === 'artists') {
      this.artistCollection = this.artistCollection.concat(res);
    }
    this.loading = false;
  }
}
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
>>>.artistOptionButton {
  background-color: transparent !important;
}
>>>.artistOptionButton:hover, >>>.artistOptionButton:focus {
  background-color: transparent !important;
  color: white !important;
}
</style>
