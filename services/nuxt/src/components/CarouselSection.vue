<template>
  <div class="carousel-contain">
    <div class="top-button-contain">
      <v-btn x-small text dark>
        {{ title }}
      </v-btn>
      <v-btn v-if="moreLink" x-small dark>
        More
      </v-btn>
    </div>
    <carousel
      :touch-drag="false"
      :loop="true"
      :mouse-drag="false"
      :pagination-enabled="false"
      :navigation-enabled="true"
      :per-page="4"
    >
      <slide
        v-for="(carouselItem, index) in validCarouselItems"
        :key="carouselItem.id"
        data-index="index"
        :data-name="carouselItem.id"
        @slideclick="handleSlideClick"
      >
        <Post
          :key="carouselItem.id"
          :index="index"
          :post="carouselItem"
        />
      </slide>
    </carousel>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import Post from '~/components/PostItem/Post.vue';


export default {
  components: {
    Post,
  },
  props: {
    'title': {
      type: String,
      default: '',
    },
    'carouselItems': {
      type: Array,
      default: () => [],
    },
    'moreLink': {
      type: String,
      default: '',
    },
  },
  computed: {
    ...mapState(['auth']),
    validCarouselItems () {
      return this.carouselItems.filter(
        carouselItem => this.isValid(carouselItem.type)
      );
    },
  },
  methods: {
    handleSlideClick (dataset) {
    },
    isValid (type) {
      return ['songs', 'albums', 'playlists'].includes(type);
    },
  },
};
</script>

<style scoped>
.top-button-contain {
  display: flex;
  justify-content: space-between;
}
.VueCarousel-slide {
  width: 25%;
  padding: 1%;
}
.VueCarousel-wrapper {
  width: 25%;
  overflow: visible !important;
  padding: 1%;
}
.carousel-contain {
  padding: 2rem;
  margin: 0 auto;
  width: 95%;
}
>>>.VueCarousel-navigation-prev {
  margin-left: 1rem;
  margin-top: -1rem;
}
>>>.VueCarousel-navigation-prev:hover,
>>>.VueCarousel-navigation-prev:focus {
  border: 1px solid var(--primary-yellow);
}
>>>.VueCarousel-navigation-next {
  margin-top: -1rem;
  margin-right: 1rem;
}
>>>.VueCarousel-navigation-next:hover,
>>>.VueCarousel-navigation-next:focus {
  border: 1px solid var(--primary-yellow);
}
</style>
