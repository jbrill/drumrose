<template>
  <div><post-feed :posts="posts" /></div>
</template>

<script>
import { mapGetters } from "vuex";

import AddPostButton from "~/components/AddPostButton";
import PostFeed from "~/components/PostFeed";
import TopBody from "~/components/TopBody";
import UnloggedContent from "~/components/UnloggedContent";
import { getFromCookie } from "~/utils/auth.js";
import { getPosts, getTrackInfo } from "~/utils/post_util.js";

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
    let parsedPosts = [];
    console.log("API TOKEN");
    console.log(window.localStorage.api_token);

    console.log("APPLE TOKEN");
    console.log(this.$store.state.music_token);

    for (let post of posts) {
      const track_info = await getTrackInfo(
        post.song.apple_music_id,
        this.$store.state.music_token
      );
      console.log(track_info);
      const postStructure = {
        track: track_info,
        user: post.user,
        caption: post.caption
      };
      if (track_info) parsedPosts.push(postStructure);
    }
    this.posts = parsedPosts;
  },
  data: function() {
    return {
      posts: []
    };
  },
  async destroyed() {
    console.log("DESTROYING...");
  }
};
</script>

<style scoped>
.content {
  max-width: 90%;
  margin: 0 auto;
  margin-top: 8rem;
  text-align: center;
}
.profileContain {
  margin-top: -2rem;
  margin-right: 5%;
  float: right;
}
.feedContain {
  margin-bottom: 10%;
}
.topExtension {
  position: absolute;
  width: 100%;
  height: 90%;
  top: 0;
  background-color: #b7205a;
}
.search-box {
  flex: 1;

  padding: 0;
  border: 0;
  border-bottom: 1px solid rgba(#000, 0.3);
  transition: border 0.2s ease;

  &:focus {
    outline: none;
    border-bottom-color: rgba(#000, 1);
  }
}
</style>
