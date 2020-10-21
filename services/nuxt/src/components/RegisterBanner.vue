<template>
  <v-carousel
    height="40vh"
    hide-delimiter-background
    show-arrows-on-hover
    cycle
    class="register-carousel"
  >
    <v-carousel-item
      v-for="(image, i) in images"
      :key="i"
      :src="require(`@/assets/img/${image.src}`)"
      gradient="to top right, rgba(100,115,201,.23), rgba(25,32,72,.4)"
      eager
      reverse-transition="fade-transition"
      transition="fade-transition"
      align="center"
      justify="center"
    >
      <v-card
        class="register-card"
        height="100%"
        color="transparent"
        background-color="transparent"
      >
        <v-card-title class="display-1 white--text justify-center">
          {{ image.title }}
        </v-card-title>
        <v-card-subtitle
          background-color="black"
          class="justify-center overline white--text"
        >
          {{ image.description }}
        </v-card-subtitle>
        <v-card-actions class="justify-center">
          <v-btn
            color="var(--primary-red)"
            @click="login"
          >
            JOIN THE PARTY - IT'S FREE!
          </v-btn>
        </v-card-actions>
      </v-card>
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
        {
          'src': "optImage.jpg",
          'placeHolder': "blurredImage.jpg",
          'title': 'SOCIAL',
          'description': 'Share your favorite music with friends.',
        },
        {
          'src': "optImage2.jpg",
          'placeholder': 'blurredImage2.jpg',
          'title': 'SMART',
          'description': 'Explore with our recommendation services.',
        },
      ],
    };
  },
  methods: {
    login () {
      this.$auth.loginWith('auth0');
    },
  },
};
</script>

<style scoped>
.register-card {
  flex-direction: column;
  display: flex;
  justify-content: center;
  align-items: center;
}
.register-carousel {
  border-bottom: 2px solid var(--primary-black-light);
}
.register-subtitle {
  text-align: center;
  padding: 5px;
}
</style>
