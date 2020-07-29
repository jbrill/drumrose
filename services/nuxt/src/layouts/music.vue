<template>
  <v-app dark class="app">
    <v-content>
      <v-app-bar><Navbar /></v-app-bar>
      <v-container fluid d-flex>
        <nuxt class="center-contain" />
      </v-container>
      <transition name="fade">
        <AudioPlayer v-if="queuePosition >= 0" />
      </transition>
    </v-content>
  </v-app>
</template>

<script>
import { mapState } from 'vuex';
import Navbar from '~/components/Navbar';
import AudioPlayer from '~/components/AudioPlayer/AudioPlayer';


export default {
  components: {
    Navbar,
    AudioPlayer,
  },
  computed: mapState(['queuePosition']),
};
</script>

<style scoped>
.app {
  font-family: Menlo, Monaco, 'Droid Sans Mono', Consolas, 'Lucida Console',
    'Courier New', monospace;
  margin: 0 auto;
  background-color: #252525;
}
.library-menu-contain {
  list-style: none;
}
@media (prefers-color-scheme: dark) {
  .app {
    background-color: black;
  }
}
@media screen and (prefers-reduced-motion: reduce) {
  .fade-enter-active, .fade-leave-active {
    transition: none;
    margin-bottom: 0;
  }
  .app {
    background-color: var(--primary-black-light);
  }
}
.fade-enter-active, .fade-leave-active {
  transition: margin-bottom .3s ease-out;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  margin-bottom: -2rem;
}
</style>
