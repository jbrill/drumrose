<template>
  <div class="profileContain">
    <div
      v-if="!loading"
      :style="{
        background: `#${trackInfo.attributes.artwork.bgColor}` 
      }"
      class="track-contain"
    >
      <img
        class="album-img"
        :src="trackInfo.attributes.artwork.url.replace(
          '{w}','250'
        ).replace(
          '{h}', '250'
        )"
      >
      <div class="track-info-contain">
        <p class="track-name">
          {{ trackInfo.attributes.name }}
        </p>
        <div class="artist-name">
          {{ trackInfo.attributes.artistName }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  layout: 'music',
  data: () => ({
    trackInfo: {},
    loading: true,
  }),
  async mounted () {
    const resp = await this.$store.getters.fetch(
      `/v1/catalog/us/songs/${this.$route.params.id}`
    );
		this.trackInfo = resp.data[0];
    this.loading = false;
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
  width: 20%;
}
>>>.track-name {
  margin-bottom: 0;
}
</style>
