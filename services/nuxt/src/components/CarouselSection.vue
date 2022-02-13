<template>
  <div class="carousel-contain">
    <div class="top-button-contain">
      <p class="font-weight-bold overline">
        {{ title }}
      </p>
      <v-btn v-if="moreLink" x-small dark>
        More
      </v-btn>
    </div>
    <carousel
      v-if="
        type === ''
      "
      :touch-drag="false"
      :loop="true"
      :pagination-enabled="false"
      :navigation-enabled="true"
      :per-page="numPerCarousel"
    >
      <slide
        v-for="(carouselItem, index) in validCarouselItems"
        :key="carouselItem.id"
        data-index="index"
        :data-name="carouselItem.id"
        :style="{ maxWidth: 100 / numPerCarousel + '%' }"
        @slideclick="handleSlideClick"
      >
        <Post
          :key="carouselItem.id"
          :index="index"
          :post="carouselItem"
        />
      </slide>
    </carousel>
    <carousel
      v-else
      :touch-drag="false"
      :loop="true"
      :pagination-enabled="false"
      :navigation-enabled="true"
      :per-page="numPerCarousel"
    >
      <slide
        v-for="(carouselItem, index) in validCarouselItems"
        :key="carouselItem.id"
        data-index="index"
        :data-name="carouselItem.id"
        :style="{ maxWidth: 100 / numPerCarousel + '%'}"
        @slideclick="handleSlideClick"
      >
        <MusicReview
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
import MusicReview from '~/components/ReviewItem/MusicReview.vue';

const carouselPixelRanges = {
  '1': {
    'min': 1,
    'max': 700,
  },
  '4': {
    'min': 701,
    'max': 1200,
  },
  '6': {
    'min': 1201,
    'max': 1800,
  },
  '8': {
    'min': 1801,
    'max': null,
  },
};

const carouselPixelRangesSmaller = {
  '1': {
    'min': 1,
    'max': 200,
  },
  '2': {
    'min': 201,
    'max': 300,
  },
  '3': {
    'min': 301,
    'max': 400,
  },
  '4': {
    'min': 401,
    'max': 500,
  },
  '5': {
    'min': 501,
    'max': 600,
  },
  '6': {
    'min': 601,
    'max': 700,
  },
  '7': {
    'min': 701,
    'max': 800,
  },
  '8': {
    'min': 801,
    'max': null,
  },
};

export default {
  components: {
    Post,
    MusicReview,
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
    'type': {
      type: String,
      default: '',
    },
  },
  data () {
    return {
      windowWidth: window.innerWidth,
      numPerCarousel: 8,
    };
  },
  computed: {
    ...mapState(['auth']),
    validCarouselItems () {
      return this.carouselItems.filter(
        carouselItem => this.isValid(carouselItem.type)
      );
    },
  },
  watch: {
    windowWidth (newWidth, oldWidth) {
      let pixelRanges = Object.keys(carouselPixelRanges);
      const numPostsPerCarousel = pixelRanges.filter( pixelRange => {
        return (
          carouselPixelRanges[pixelRange]['min'] < newWidth &&
          (
            carouselPixelRanges[pixelRange]['max'] > newWidth ||
            carouselPixelRanges[pixelRange]['max'] === null
          )
        );
      });
      this.numPerCarousel = parseInt(numPostsPerCarousel[0]);
    },
  },
  mounted () {
    console.log(this.carouselItems)
    console.log(this.validCarouselItems)
    let pixelRanges = Object.keys(carouselPixelRanges);
    const numPostsPerCarousel = pixelRanges.filter( pixelRange => {
      return (
        carouselPixelRanges[pixelRange]['min'] < this.windowWidth &&
        (
          carouselPixelRanges[pixelRange]['max'] > this.windowWidth ||
          carouselPixelRanges[pixelRange]['max'] === null
        )
      );
    });
    this.numPerCarousel = parseInt(numPostsPerCarousel[0]);
    this.$nextTick( () => {
      window.addEventListener('resize', this.onResize);
    });
  },
  beforeDestroy () { 
    window.removeEventListener('resize', this.onResize); 
  },
  methods: {  
    onResize () {
      this.windowWidth = window.innerWidth;
    },
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
.VueCarousel-wrapper {
  overflow: visible !important;
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
>>>.VueCarousel-navigation-next {
  margin-top: -1rem;
  margin-right: 1rem;
}
</style>
