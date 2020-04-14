<template>
  <div>
    <TopBody />
    <div class="post-feed">
      <Post v-for="post in posts" :key="post.id" :post="post" />
    </div>
  </div>
</template>

<script>
import Post from '~/components/Post';
import TopBody from '~/components/TopBody';
import { getPosts } from '~/utils/post_util.js';

export default {
  components: {
    Post,
    TopBody,
  },
  async asyncData () {
    const postResponse = await getPosts();
    console.dir(postResponse);
    return { "posts":  postResponse.data };
    //    const postsToRender = await parsePosts(posts);
    //    this.posts = postsToRender;
  },
  destroyed () {
    /* We should set index here on page */
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
