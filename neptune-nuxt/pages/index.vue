<template>
  <div class="post--feed__contain">
    <div v-if="isAuthenticated" class="post--feed__logged-in__contain">
      <topBody />
      <post-feed :posts="posts" />
    </div>
    <div v-else class="post--feed__not-logged-in__contain"><p>HI</p></div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

import AddPostButton from "~/components/AddPostButton";
import PostFeed from "~/components/PostFeed";
import TopBody from "~/components/TopBody";
import UnloggedContent from "~/components/UnloggedContent";
import { getFromCookie } from "~/utils/auth.js";
import { getPosts, parsePosts } from "~/utils/post_util.js";

export default {
  computed: mapGetters(["isAuthenticated"]),
  components: {
    PostFeed,
    AddPostButton,
    TopBody,
    UnloggedContent
  },
  async created() {
    const postResponse = await getPosts(window.localStorage.api_token);
    const posts = postResponse.data;
    this.posts = await parsePosts(posts, this.$store.state.music_token);
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
