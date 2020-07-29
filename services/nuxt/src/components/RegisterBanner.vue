<template>
  <v-carousel
			height="30vw"
			hide-delimiter-background
		>
		<v-carousel-item
			v-for="(image, i) in images"
      :src="image.src"
      reverse-transition="fade-transition"
      transition="fade-transition"
      align="center"
      justify="center"
	    :key="i"
      flex
		>
				<v-row align="center" justify="center"><div class="slide-title">{{ image.title }}</div></v-row>
				<v-row
					align="center"
					justify="center"
				>
					<div class="slide-description">{{ image.description }}</div>
				</v-row>
				<v-row
					align="center"
					justify="center"
				>
					<v-btn @click="login" color="var(--primary-red)">Get Started - IT'S FREE!</v-btn>
				</v-row>
		</v-carousel-item>
	</v-carousel>
</template>

<script>
export default {
  data () {
    return {
      trendingAlbumGroups: [],
      trendingSongGroups: [],
      trendingPlaylistGroups: [],
      images: [
        { 'src': 'https://images.unsplash.com/photo-1470229722913-7c0e2dbbafd3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80', 'title': 'Social', 'description': 'Share music with your friends.' },
        { 'src': 'https://images.unsplash.com/photo-1524103416206-a67f05a8154b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80', 'title': 'Smart', 'description': 'Share music with your friends.' },
      ],
    }
  },
  methods: {
    login () {
      this.$auth.loginWith('auth0')
    },
  },
}
</script> 
<style scoped>

</style>
