<template>
  <div>
    <div
      v-if="!loading"
    />
  </div>
</template>

<script>
export default {
  data: () => ({
    searchResults: null,
    loading: true,
  }),
  async mounted () {
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
