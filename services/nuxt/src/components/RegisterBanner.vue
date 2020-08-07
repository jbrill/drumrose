<template>
  <v-carousel
		height="30vh"
		hide-delimiter-background
		show-arrows-on-hover
		cycle
	>
		<v-carousel-item
			v-for="(image, i) in images"
      :src="image.src"
      eager
      reverse-transition="fade-transition"
      transition="fade-transition"
      align="center"
      justify="center"
	    :key="i"
		>
     <v-card class="register-card" height="100%" color="transparent" background-color="transparent">
        <v-card-title color="white" class="justify-center">
          {{ image.title }}
        </v-card-title>
        <v-card-subtitle style="text-align: center" class="justify-center">
          {{ image.description }}
        </v-card-subtitle>
        <v-card-actions class="justify-center">
          <v-btn @click="login" color="var(--primary-red)">Get Started - IT'S FREE!</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
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
        { 'src':
'https://images.unsplash.com/photo-1553190781-4490b9b6d06b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80', 'title': 'SOCIAL', 'description': 'Share your favorite music with friends.' },
        { 'src':
'https://images.unsplash.com/photo-1530352865347-3c2e277abefe?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2253&q=80',
'title': 'SMART', 'description': 'Explore with our recommendation services.' },
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
.register-card {
  flex-direction: column;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
