<template>
	<v-menu open-on-hover :close-on-content-click="false" top color="black" :offset-y="true" dark>
		<template v-slot:activator="{ on }">
			<v-btn
				icon
				v-on="on"
			>
				<v-icon color="white" class="album-overlay-more">
					mdi-volume-vibrate
				</v-icon>
			</v-btn>
		</template>
	   <v-slider
      dark
			class="volume-slider"
			v-model="volume"
			append-icon="volume_up"
      vertical
			min="0"
			max="100"
		></v-slider>
  </v-menu>
</template>

<script>
export default {
  props: {
    id: {
      type: String,
      default: '',
    },
  },
  data () {
    return {
      playlistDialog: false,
      volume: 10,
    };
  },
  methods: {
    addToQueue: function () {
      this.$store.dispatch("setQueue", { "playlist": this.id })
    },
    addToLibrary: function () {
      this.$store.dispatch("addToLibrary", { 'playlist': this.id })
    },
  }
}
</script>

<style scoped>
</style>
