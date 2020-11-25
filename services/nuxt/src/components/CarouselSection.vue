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
  </div>
</template>

<script>
import { mapState } from 'vuex';
import Post from '~/components/PostItem/Post.vue';

const carouselPixelRanges = {
  '1': {
    'min': 1,
    'max': 500,
  },
  '2': {
    'min': 501,
    'max': 900,
  },
  '3': {
    'min': 901,
    'max': 1600,
  },
  '4': {
    'min': 1601,
    'max': null,
  },
};


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
  data () {
    return {
      windowWidth: window.innerWidth,
      numPerCarousel: 4,
    };
  },
  computed: {
    ...mapState(['auth']),
    validCarouselItems () {
      console.log(this.carouselItems)
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
      console.log(this.numPerCarousel)
    },
  },
  mounted () {
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
