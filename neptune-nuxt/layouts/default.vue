<template>
  <div class="app">
    <div class="main">
      <navbar /> <topBody />
      <div class="main-body"><nuxt /></div>
      <audioPlayer />
    </div>
  </div>
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
        // hid is used as unique identifier. Do not use `vmid` for it as it will not work
        // {
        //   name: "apple-music-developer-token",
        //   content: this.$store.state.music_token
        // },
        // { name: "apple-music-app-name", content: "Neptune" },
        // { name: "apple-music-app-build", content: "0.0.1" }
      ]
    };
  }
};
</script>

<style scoped>
.app {
  font-family: Menlo, Monaco, "Droid Sans Mono", Consolas, "Lucida Console",
    "Courier New", monospace;
}
.main {
  margin: 0 auto;
  background-color: var(--primary-red--dark);
}
.main-body {
  margin-top: -2rem;
}

.menuContain {
  width: 80%;
  float: left;
}
</style>
