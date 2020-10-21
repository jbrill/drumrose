<template>
  <v-container v-if="!loading">
    <h1>{{ artistData.attributes.name }}</h1>
    <v-chip
      v-for="(genre, idx) in artistData.attributes.genreNames"
      :key="`genre-${idx}`"
      small
      pill
    >
      #{{ genre }}
    </v-chip>
    <v-responsive>
      <CarouselSection
        :key="`album-${index}`"
        title="Albums"
        :carousel-items="attributeData"
      />
    </v-responsive>
  </v-container>
</template>

<script>
import Album from '~/components/MusicItem/Album';
import CarouselSection from '~/components/CarouselSection';

export default {
  components: {
    CarouselSection,
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
      this.attributeData.push(attributeResp.data[0]);
    });
    console.log("!")
    console.log(this.artistData);
    console.log("!!")
    console.log(this.attributeData);
    console.log(resp);
    this.loading = false;
  },
};
</script>

<style scoped></style>
