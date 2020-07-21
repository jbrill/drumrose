<template>
  <div>
    <h4 class="recommended-title">
      Hi <nuxt-link
        to="/users/jbrill"
      >
        jbrill
      </nuxt-link>, we've recommended some music for
      you.
    </h4>
    <div class="carousel-contain">
      <v-btn text nuxt to="playlists" color="#ccc" class="carousel-title">
        Playlists
      </v-btn>
    </div>
    <div class="carousel-contain">
      <v-btn text nuxt to="tracks" color="#ccc" class="new-tracks-title">
        Tracks
      </v-btn>
    </div>
    <div class="new-albums-contain">
      <v-btn text nuxt to="tracks" color="#ccc" class="new-tracks-title">
        Albums
      </v-btn>
    </div>
  </div>
</template>

<script>

export default {
  components: {
  },
  async asyncData () {
    /*const posts = await getRecommendedTracks();
    const playlists = await getRecommendedPlaylists();*/
    return {
      "posts": [],
      "playlists": [],
    };
  },
  mounted () {
    const queue = this.posts.map(a => a.song.apple_music_id);

    this.$store.dispatch("setQueue", { "songs": queue } );
  },
};
</script>

<style scoped>
.recommended-title {
  padding-left: 1.5rem;
  padding-top: 3rem;
  text-align: center;
}
.tunes-contain {
  text-align: center;
  padding-top: 3rem;
  padding-bottom: 1rem;
}
.new-tracks-contain {
  padding-top: 2rem;
  width: 95%;
  margin: 0 auto;
}
</style>
