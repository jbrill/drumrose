<template>
  <div>
    <h3 class="social-title">Social</h3>
    <h6 class="social-title">Listen in with your friends...</h6>
    <div class="carousel-contain">
			<v-btn text dark>TRACKS</v-btn>
      <carousel :touch-drag=false :loop=true :mouse-drag=false :pagination-enabled=false :navigation-enabled=true :per-page="5">
				<slide
						v-for="(favoritedTrack, index) in favoritedTracks"
						data-index="index"
						data-name="favoritedTrack.id"
						@slideclick="handleSlideClick">
					<Post :index="index" :key="favoritedTrack.id" :post="favoritedTrack" type="track" />
				</slide>
			</carousel>
    </div>
    <div class="carousel-contain">
			<v-btn text dark>PLAYLISTS</v-btn>
			<carousel :touch-drag=false :loop=true :mouse-drag=false :pagination-enabled=false :navigation-enabled=true :per-page="5">
				<slide
						v-for="(favoritedPlaylist, index) in favoritedPlaylists"
						data-index="index"
						data-name="favoritedPlaylist.id"
						@slideclick="handleSlideClick">
					<Post :index="index" :key="favoritedPlaylist.id" :post="favoritedPlaylist" type="playlist" />
				</slide>
			</carousel>
    </div>
  </div>
</template>

<script>
import Post from '~/components/Post';
import TopBody from '~/components/TopBody';
import { getFavoritedTracks, getFavoritedAlbums, getFavoritedPlaylists } from '~/api/api';
import { mapState } from 'vuex';


export default {
  components: {
    Post,
    TopBody,
  },
  methods: {
		handleSlideClick (dataset) {
			console.log(dataset.index, dataset.name)
		}
	},
  async asyncData () {
    const favoritedTracksResponse = await getFavoritedTracks()
    const favoritedAlbumsResponse = await getFavoritedAlbums()
    const favoritedPlaylistsResponse = await getFavoritedPlaylists()

    console.log(favoritedAlbumsResponse.data);
    console.log(favoritedTracksResponse.data);
    return {
      "favoritedTracks": favoritedTracksResponse.data,
      "favoritedAlbums": favoritedAlbumsResponse.data,
      "favoritedPlaylists": favoritedPlaylistsResponse.data,
    };
  },
};
</script>

<style scoped>
.VueCarousel-slide {
  width: 25%;
  padding: 1%;
}
.carousel-contain {
  padding: 1rem;
  margin: 0 auto;
  width: 95%;
}
</style>
