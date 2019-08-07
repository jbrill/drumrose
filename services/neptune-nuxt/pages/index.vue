<template>
  <no-ssr>
    <div class="post--feed__contain">
      <div v-if="isAuthenticated" class="post--feed__logged-in__contain">
        <topBody />
        <post-feed :posts="posts" />
      </div>
      <div v-else class="post--feed__not-logged-in__contain"><p>HI</p></div>
    </div>
  </no-ssr>
</template>

<script>
import { mapGetters } from "vuex";

import AddPostButton from "~/components/AddPostButton";
import PostFeed from "~/components/PostFeed";
import TopBody from "~/components/TopBody";
import UnloggedContent from "~/components/UnloggedContent";
import { store } from "~/plugins/localStorage";
import { getFromCookie } from "~/utils/auth.js";
import { getPosts, parsePosts } from "~/utils/post_util.js";

export default {
  components: {
    PostFeed,
    AddPostButton,
    TopBody,
    UnloggedContent
  },
  computed: {
    isAuthenticated: function() {
      return store.getters.isAuthenticated;
    }
  },
  async created() {
    const postResponse = await getPosts(store.state.api_token);
    const posts = postResponse.data;
    const postsToRender = await parsePosts(posts, store.state.apple_token);
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
