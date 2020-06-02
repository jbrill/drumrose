<template>
  <div>
    <h4 class="recommended-title">Hi <nuxt-link
to="/users/jbrill">jbrill</nuxt-link>, we've recommended some music for
you.</h4>
    <div class="carousel-contain">
      <v-btn text nuxt to="playlists" color="#ccc" class="carousel-title">Playlists</v-btn>
      <carousel
        :touch-drag=false :loop=true :mouse-drag=false
        :pagination-enabled=false :navigation-enabled=true :per-page="5">
        <slide
            v-for="(playlist, index) in playlists"
            data-index="index"
            data-name="playlist.id"
        >
          <MusicItem :index="index" :key="playlist.id" type="playlist" :apple_music_id="playlist.playlist.apple_music_id" />
        </slide>
      </carousel>
    </div>
    <div class="carousel-contain">
      <v-btn text nuxt to="tracks" color="#ccc" class="new-tracks-title">Tracks</v-btn>
      <carousel
        :touch-drag=false :loop=true :mouse-drag=false
        :pagination-enabled=false :navigation-enabled=true :per-page="5">
        <slide
            v-for="(track, index) in posts"
            data-index="index"
            data-name="track.id"
        >
          <MusicItem :index="index" :key="track.id" type="track" :apple_music_id="track.song.apple_music_id" />
        </slide>
      </carousel>
    </div>
    <div class="new-albums-contain">
      <v-btn text nuxt to="tracks" color="#ccc" class="new-tracks-title">Albums</v-btn>
    </div>
  </div>
</template>

<script>
import Track from '~/components/Track';
import MusicItem from '~/components/MusicItem';
import TopBody from '~/components/TopBody';
import { getFavoritedTracks, getFavoritedPlaylists } from '~/api/api';
import { mapState } from 'vuex';

export default {
  components: {
    Track,
    MusicItem,
    TopBody,
  },
  async asyncData () {
    const posts = await getFavoritedTracks();
    const playlists = await getFavoritedPlaylists();
    return { "posts": posts.data, "playlists": playlists.data };
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
