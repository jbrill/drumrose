<template>
  <div class="post--feed__logged-in__contain">
    <topBody />
    <post-feed :posts="posts" />
  </div>
</template>

<script>
import PostFeed from '~/components/PostFeed';
import TopBody from '~/components/TopBody';
import { getPosts } from '~/utils/post_util.js';

export default {
  components: {
    PostFeed,
    TopBody,
  },
  data: function () {
    return {
      posts: [],
    };
  },
  async created () {
    const postResponse = await getPosts();
    const posts = postResponse.data;
    console.log(posts);
    //    const postsToRender = await parsePosts(posts);
    //    this.posts = postsToRender;
  },
  destroyed () {
    /* We should set index here on page */
    console.log('DESTROYING...');
  },
};
</script>

<style scoped></style>
