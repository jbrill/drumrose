<template>
  <div>
    <CarouselSection
      v-if="!loading"
      v-for="(personalRecommendation) in recommendations"
      :title="personalRecommendation.attributes.title.stringForDisplay"
      :carouselItems="personalRecommendation.relationships.contents.data"
    />
    <v-divider></v-divider>
  </div>
</template>

<script>
import CarouselSection from '~/components/CarouselSection';

import { getFavorites, postFavorite } from '~/api/api';
import { mapState } from 'vuex';


export default {
  data () {
    return {
      loading: false,
      recommendations: []
    }
  },
  components: {
    CarouselSection,
  },
  computed: {
    ...mapState(['isAuthorized', 'auth']),
  },
  async fetch () {
    this.loading = true;
    this.recommendations = await this.$store.getters['recommendations'];
    this.loading = false;
  },
};
</script>

<style scoped>
.welcome-contain {
  max-height: 45%;
  overflow: hidden;
  border-bottom: 1px solid var(--primary-red);
}
.welcome-contain-image {
  width: 100%;
  height: auto;
}
</style>
