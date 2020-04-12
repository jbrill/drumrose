<template>
  <client-only>
    <div class="post--feed__logged-in__contain">
      <TopBody />
      <PostFeed :posts="posts" />
    </div>
  </client-only>
</template>

<script>
import PostFeed from '~/components/PostFeed';
import TopBody from '~/components/TopBody';
import { getPosts, parsePosts } from '~/utils/post_util.js';

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
  computed: {},
  async created () {
    const postResponse = await getPosts();
    const posts = postResponse.data;
    const postsToRender = await parsePosts(posts);
    this.posts = postsToRender;
  },
  destroyed () {
    /* We should set index here on page */
    console.log('DESTROYING...');
  },
};
</script>

<style scoped></style>
