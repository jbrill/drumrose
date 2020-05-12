<template>
  <div>
    <div class="playlists-contain">
			<p class="playlists-description">Log some of your favorite music...</p>
			<div class="create-playlist-button-contain">
				<v-btn class="add-post-button" color="primary" dark nuxt
	to="/logs/new" width="10rem">
					Log a track
				</v-btn>
			</div>
		</div>
    <div class="post-feed">
      <Post v-for="(post, index) in posts" :index="index" :key="post.id" :post="post" />
    </div>
  </div>
</template>

<script>
import Post from '~/components/Post';
import TopBody from '~/components/TopBody';
import Tune from '~/components/Tune';
import { getPosts } from '~/utils/post_util';
import { mapState } from 'vuex';

export default {
  components: {
    Post,
    TopBody,
    Tune,
  },
  async asyncData () {
    const posts = await getPosts();
    return { "posts":  posts.data };
  },
  mounted () {
    const queue = this.posts.map(a => a.song.apple_music_id);
    
    this.$store.dispatch("setPosts", this.posts);
    this.$store.dispatch("setQueue", { "songs": queue } );
  },
};
</script>

<style scoped>
.tunes-contain {
  text-align: center;
  padding-top: 3rem;
  padding-bottom: 1rem;
}
.post-feed {
  display: grid;
  row-gap: 1rem;
}
</style>
