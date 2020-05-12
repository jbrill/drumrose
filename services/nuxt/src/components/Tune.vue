<template>
  <div>
    <p class="home-description">Log a track or an album.</p>
		<v-text-field
			label="Tune"
			placeholder="Search for a track or album"
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
      <v-btn class="add-post-button" color="primary" dark nuxt
to="playlists/new" width="10rem">
        Log music
      </v-btn>
    </div>
  </div>
</template>

<script>
export default {
  components: {
  },
	data () {
		return {
			caption: '',
      rules: [v => v.length <= 25 || 'Max 25 characters'],
		}
	},
};
</script>

<style scoped>
.home-description {
  color: black;
  width: 100%;
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
