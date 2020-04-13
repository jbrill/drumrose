<template>
  <div class="post--feed__logged-in__contain">
    <TopBody />
    <PostFeed :posts="posts" />
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
  async fetch () {
    const postResponse = await getPosts();
    this.posts = postResponse.data;
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
