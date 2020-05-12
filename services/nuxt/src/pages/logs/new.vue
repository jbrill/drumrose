<template>
  <div class="home-contain">
    <p class="home-description">Log a track</p>
		<v-text-field
			label="Tune"
			placeholder="Search for a track or album"
      @input="onTuneChange"
			v-model="trackQuery"
			solo
		></v-text-field>
		<v-textarea
			v-model="caption"
			color="teal"
			maxlength="500"
			counter="500"
		>
			<template v-slot:label>
				<div>
					Caption <small>(optional)</small>
				</div>
			</template>
		</v-textarea>
    <div class="create-playlist-button-contain">
      <v-btn class="add-post-button" color="primary" dark nuxt to="/playlists/new" width="10rem">
        Log music
      </v-btn>
    </div>
  </div>
</template>

<script>
import { getTrackHintsFromQuery } from '~/utils/post_util';
import { mapState } from 'vuex';

export default {
  components: {
  },
	data () {
		return {
			caption: '',
      rules: [v => v.length <= 25 || 'Max 25 characters'],
			trackQueryHints: [],
			trackQuery: ''
		}
	},
  methods: {
    onTuneChange: async function (e) {
      console.log("YPOO")
      const searchQuery = this.trackQuery;
			console.log(searchQuery);
      const resp = await this.$store.getters.fetch(`/v1/catalog/us/search/hints?term=${searchQuery}&limit=5&types=songs`)
      console.log(resp);
      this.trackQueryHints = resp
    },
  }
};
</script>

<style scoped>
.home-contain {
  padding-top: 3rem;
}
.home-description {
  color: black;
  width: 100%;
  text-align: center;
}
.create-playlist-button-contain {
  margin: 0 auto;
  align-items: center;
  display: flex;
}
.add-post-button {
  margin: 0 auto;
}
.post-feed {
  padding-top: 3rem;
  display: grid;
  row-gap: 1rem;
}
</style>
