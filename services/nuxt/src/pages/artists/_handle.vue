<template>
  <div v-if="!loading">
    <h1>{{ artistData.attributes.name }}</h1>
    <v-chip
      v-for="(genre, idx) in artistData.attributes.genreNames"
      :key="`genre-${idx}`"
    >
      #{{ genre }}
    </v-chip>
    <h6>Albums</h6>
    <Album
      v-for="(album, idx) in artistData.relationships.albums.data"       
      :id="album.id"
      :key="`album-${idx}`"
      :attributes="attributeData[idx]"
      is-playable
      is-actionable
    />
  </div>
</template>

<script>
import Album from '~/components/MusicItem/Album';

export default {
  components: {
    Album,
  },
  data: () => ({
    artistData: {},
    attributeData: [],
    loading: true,
  }),
  async created () {
    this.loading = true;
    const handle = this.$route.params.handle;
    const resp = await this.$store.getters.fetch(
			`/v1/catalog/us/artists/${handle}`
		);
    this.artistData = resp.data[0];
    this.artistData.relationships.albums.data.forEach( async album => {
      const attributeResp = await this.$store.getters.fetch(
        `/v1/catalog/us/albums/${album.id}`
      );
      this.attributeData.push(attributeResp.data[0].attributes);
    });
    console.log(this.artistData);
    console.log(this.attributeData);
    console.log(resp);
    this.loading = false;
  },
};
</script>

<style scoped></style>
