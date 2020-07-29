<template>
	<v-menu dark offset-y>
		<template v-slot:activator="{ on }">
			<v-btn
				icon
				dark
				v-on="on"
			>
				<v-icon small color="white" class="album-overlay-more">
					mdi-dots-horizontal
				</v-icon>
			</v-btn>
		</template>
		<v-list>
			<v-list-item>
				<v-list-item-title>
					<v-btn @click="addToQueue" block tile text><v-icon left>mdi-music-box-multiple</v-icon> Add to queue</v-btn>
				</v-list-item-title>
			</v-list-item>
			<v-dialog
				v-model="playlistDialog"
				width="500"
			>
				<template v-slot:activator="{ on }">
					<v-list-item
						v-on="on"
					>
						<v-list-item-title>
					    <v-btn @click="addToLibrary" block tile text><v-icon left>mdi-playlist-music</v-icon> Add to playlist</v-btn>
						</v-list-item-title>
					</v-list-item>
				</template>

        <v-card>
					<v-card-title
						class="headline grey lighten-2"
						primary-title
						dark
					>
						Add to Playlist
					</v-card-title>

					<v-divider />

					<v-card-actions>
						<v-spacer />
						<v-btn
							color="primary"
							text
							@click="playlistDialog = false"
						>
							Add
						</v-btn>
					</v-card-actions>
				</v-card>
			</v-dialog>
			<v-list-item>
				<v-list-item-title>
				  <v-btn @click="addToLibrary" block tile text><v-icon left>mdi-playlist-music</v-icon> Add to library</v-btn>
				</v-list-item-title>
			</v-list-item>
		</v-list>
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
>>>.v-list-item {
  padding: 0;
}
</style>
