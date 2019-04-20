<template>
  <div class="discover--feed__contain">
    <topBody /> <post-feed :posts="posts" />
  </div>
</template>

<script>
import { mapGetters } from "vuex";

import AddPostButton from "~/components/AddPostButton";
import PostFeed from "~/components/PostFeed";
import TopBody from "~/components/TopBody";
import UnloggedContent from "~/components/UnloggedContent";

import { getPosts, parsePosts } from "~/utils/post_util.js";

export default {
  computed: mapGetters(["isAuthenticated", "loggedUser"]),
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
  }
};
</script>

<style scoped></style>
