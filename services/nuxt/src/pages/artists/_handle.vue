<template>
  <div>
    <v-sheet v-if="!loading">
      <p>{{ artistData.attributes.name }}</p>
      <v-list>
        <v-list-item
          v-for="genre in artistData.attributes.genreNames"
          :key="`genre-${genre}`"
        >
          {{ genre }}
        </v-list-item>
      </v-list>
    </v-sheet>
  </div>
</template>

<script>
export default {
  data: () => ({
    artistData: {},
    loading: true,
  }),
  async mounted () {
    console.log(this.$route);
    const handle = this.$route.params.handle;
    const resp = await this.$store.getters.fetch(
			`/v1/catalog/us/artists/${handle}`
		);
    this.loading = false;
    if ('data' in resp) {
      this.artistData = resp.data[0];
    }
    console.log(this.$route.params.slug);
    console.log(resp);
  }, 
};
</script>

<style scoped></style>
