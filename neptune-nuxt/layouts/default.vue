<template>
  <div class="app"><navbar /> <nuxt /> <audioPlayer /></div>
</template>

<script>
import { mapGetters } from "vuex";
import Navbar from "~/components/Navbar";
import ProfileNav from "~/components/ProfileNav";
import MenuOptions from "~/components/MenuOptions";
import PostFeed from "~/components/PostFeed";
import AddPostButton from "~/components/AddPostButton";
import TopBody from "~/components/TopBody";
import AudioPlayer from "~/components/AudioPlayer";

export default {
  computed: mapGetters(["isAuthenticated", "loggedUser"]),
  components: {
    ProfileNav,
    MenuOptions,
    PostFeed,
    AddPostButton,
    TopBody,
    Navbar,
    AudioPlayer
  },
  head() {
    return {
      meta: [
        {
          name: "apple-music-developer-token",
          content: this.$store.state.music_token
        },
        { name: "apple-music-app-name", content: "Neptune" },
        { name: "apple-music-app-build", content: "0.0.1" }
      ]
    };
  }
};
</script>

<style>
.app {
  font-family: Menlo, Monaco, "Droid Sans Mono", Consolas, "Lucida Console",
    "Courier New", monospace;
  margin: 0 auto;
  background-color: var(--primary-red--dark);
}
</style>
