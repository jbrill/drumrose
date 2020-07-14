<template>
  <div>
    <v-tabs
        v-model="tab"
        background-color="primary"
        dark
      >
        <v-tab
          v-for="item in musicSelections"
          :key="item"
        >
          {{ item }}
        </v-tab>
      </v-tabs>
  
      <v-tabs-items v-model="tab">
        <v-tab-item
          v-for="item in musicSelections"
          :key="item"
        >
          <v-card flat>
            <v-card-text>{{ item }}</v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs-items>
    <div class="library-contain">
			<v-btn-toggle borderless rounded background-color="transparent" class="artist-menu-options"><v-btn class="artist-option-button" x-small fab v-for="(artistOption, artistIndex) in artistOptions">{{ artistOption }}</v-btn></v-btn-toggle>
			<ul v-if="activeCollection === 'artist'">
				<v-card
					:color="item.color"
					dark
					v-for="item in artisttCollection"
				>
					<div class="d-flex flex-no-wrap justify-space-between">
						<div>
							<v-card-title
								class="headline"
								v-text="item.attributes.name"
							></v-card-title>

							<v-card-subtitle v-text="item.href"></v-card-subtitle>
						</div>

						<v-avatar
							class="ma-3"
							size="125"
							tile
						>
							<v-img :src="item.href"></v-img>
						</v-avatar>
					</div>
				</v-card>
			</ul>
    </div>
  </div>
</template>

<script>
import Raven from 'raven-js';
import { mergeWith } from 'lodash';
import { mapState } from 'vuex';


export default {
  data () {
    return {
      item: null,
      error: null,
      loading: true,
      collection: [],
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
  computed: mapState(['activeCollection']),
  methods: {
    changeCollection: function() {
      console.log("CHANGING")
      this.$store.commit('activeCollection', 'songs')
    }
  },
  async created () {
    // Load the collection
    this.loading = true;
    this.error = null;
    this.artistCollection = [];
    this.trackCollection = [];
    this.albumCollection = [];
    this.playlistCollection = [];
    let options = {
      limit: 100
    };
    try {
      for (var offset = 0, res = null; res === null || res.length !== 0; offset += options.limit) {
        res = await this.$store.getters.get(
          true,
          this.$store.state.activeCollection,
          null,
          mergeWith(options, { offset: offset })
        );
        this.collection = this.collection.concat(res);
        console.log("COLLECTION:\t")
        console.log(this.collection)
      }
    } catch (err) {
      console.error(err);
      Raven.captureException(err);
      this.error = err;
    }
    this.loading = false;
  }
}
</script>

<style scoped>
.library-contain {
  display: flex;
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
>>>.artist-option-button {
  background-color: transparent !important;
}
</style>
