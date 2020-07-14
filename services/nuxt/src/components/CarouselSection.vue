<template>
	<div class="carousel-contain">
		<div class="top-button-contain">
      <v-btn x-small text dark>{{ title }}</v-btn>
      <v-btn x-small dark>More</v-btn>
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
				v-for="(carouselItem, index) in carouselItems"
				:key="carouselItem.id"
				data-index="index"
				data-name="carouselItem.id"
				@slideclick="handleSlideClick"
			>
				<Post
					v-if="carouselItem.user"
					:key="carouselItem.id"
					:index="index"
					:post="carouselItem"
					post-type="favorite"
					:type="carouselItem.favorite_type"
				/>
			</slide>
		</carousel>
	</div>
</template>

<script>
import Post from '~/components/Post';
import { getFavorites } from '~/api/api';
import { mapState } from 'vuex';


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
  },
  computed: {
    ...mapState(['auth']),
  },
  methods: {
    handleSlideClick (dataset) {
      console.log(dataset.index, dataset.name);
    },
  },
}
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
.carousel-contain {
  padding: 2rem;
  margin: 0 auto;
  width: 95%;
}
>>>.VueCarousel-navigation-prev {
  margin-left: 1rem;
}
>>>.VueCarousel-navigation-next {
  margin-right: 1rem;
}
</style>
