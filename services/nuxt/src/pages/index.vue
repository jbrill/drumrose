<template>
  <div>
    <TopBody />
    <div v-if="" class="post-feed">
      <Post v-for="post in posts" :key="post.id" :post="post" />
    </div>
  </div>
</template>

<script>
import Post from '~/components/Post';
import TopBody from '~/components/TopBody';
import { getPosts } from '~/utils/post_util';
import { mapState } from 'vuex';

export default {
  components: {
    Post,
    TopBody,
  },
  async asyncData () {
    const posts = await getPosts();
    return { "posts":  posts.data };
  },
  mounted () {
    /* lets set the music queue here */
    console.log("SHOULD SET QUEUE...")
    const queue = this.posts.map(a => a.song.apple_music_id);
    this.$store.dispatch("setQueue", { "songs": queue } );
  },
  destroyed () {
    /* We should set post index here on page */
    console.log('DESTROYING...');
  },
};
</script>

<style scoped>
.post-feed {
  display: grid;
  row-gap: 1rem;
}
</style>
