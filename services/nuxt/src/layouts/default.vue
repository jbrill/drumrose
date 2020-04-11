<template>
  <div class="app"><navbar /> <nuxt /></div>
</template>

<script>
import Navbar from '~/components/Navbar';
import ProfileNav from '~/components/ProfileNav';
import MenuOptions from '~/components/MenuOptions';
import PostFeed from '~/components/PostFeed';
import AddPostButton from '~/components/AddPostButton';
import TopBody from '~/components/TopBody';
import AudioPlayer from '~/components/AudioPlayer';

export default {
  components: {
    ProfileNav,
    MenuOptions,
    PostFeed,
    AddPostButton,
    TopBody,
    Navbar,
    AudioPlayer
  }
}
</script>

<style>
.app {
  font-family: Menlo, Monaco, "Droid Sans Mono", Consolas, "Lucida Console",
    "Courier New", monospace;
  margin: 0 auto;
  background-color: #f6f6f6;
}
</style>
