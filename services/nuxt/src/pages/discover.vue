<template>
  <client-only>
    <div class="post--feed__logged-in__contain">
      <topBody />
      <post-feed :posts="posts" />
    </div>
  </client-only>
</template>

<script>
import AddPostButton from "~/components/AddPostButton";
import PostFeed from "~/components/PostFeed";
import TopBody from "~/components/TopBody";
import UnloggedContent from "~/components/UnloggedContent";
import { getPosts, parsePosts } from "~/utils/post_util.js";

export default {
  components: {
    PostFeed,
    AddPostButton,
    TopBody,
    UnloggedContent
  },
  computed: {
  },
  async created() {
    const postResponse = await getPosts();
    const posts = postResponse.data;
    const postsToRender = await parsePosts(posts);
    this.posts = postsToRender;
  },
  data: function() {
    return {
      posts: []
    };
  },
  async destroyed() {
    /* We should set index here on page */
    console.log("DESTROYING...");
  }
};
</script>

<style scoped></style>
