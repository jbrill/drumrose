<template>
  <div>
    {{ search }} - {{ searchResults.length }} Results
  </div>
</template>

<script>
export default {
  data: () => ({
    search: null,
    searchResults: [],
    loading: true,
  }),
  async mounted () {
    console.log(this.$route.params.search);
    this.search = this.$route.params.search;
    this.$store.dispatch('getHints', this.search).then(res => {
			this.isLoading = false;
			this.searchResults = [
				{
					header: 'Tracks',
				},
			].concat(
				res.results.songs.data
			).concat([
				{
					divider: true,
				},
				{
					header: 'Artists',
				},
			]).concat(
				res.results.artists.data
			).concat([
				{
					divider: true,
				},
				{
					header: 'Albums',
				},
			]).concat(
				res.results.albums.data
			);
		});
    this.loading = false;
  },
  methods: {
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
  width: auto;
  height: auto;
}
>>>.track-name {
  margin-bottom: 0;
}
</style>
