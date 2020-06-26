<template>
  <div>
    <v-chip-group
			mandatory
			active-class="primary--text"
		>
			<v-chip v-for="tag in musicSelections" :key="tag">
				{{ tag }}
			</v-chip>
		</v-chip-group>
    <ul>
      <v-card
				:color="item.color"
				dark
        v-for="item in collection"
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
</template>

<script>
import Raven from 'raven-js';
import { mergeWith } from 'lodash';


export default {
  data () {
    return {
      error: null,
      loading: true,
      collection: [],
      musicSelections: [
				'Artists',
				'Tracks',
				'Albums',
				'Playlists',
			],
    };
  },
  async created () {
      // Load the collection
      this.loading = true;
      this.error = null;
      this.collection = [];
      let options = {
        limit: 100
      };
      try {
        for (var offset = 0, res = null; res === null || res.length !== 0; offset += options.limit) {
          res = await this.$store.getters.get(true, 'artists', null, mergeWith(options, { offset: offset }));
          this.collection = this.collection.concat(res);
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
</style>
