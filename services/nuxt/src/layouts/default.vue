<template>
  <div class="app">
    <Navbar />
    <nuxt />
    <transition name="fade">
      <AudioPlayer v-if="queuePosition >= 0" />
    </transition>
  </div>
</template>

<script>
import Navbar from '~/components/Navbar';
import AudioPlayer from '~/components/AudioPlayer';
import { mapState } from 'vuex';


export default {
  computed: mapState(['queuePosition']),
  components: {
    Navbar,
    AudioPlayer,
  },
};
</script>

<style>
.app {
  font-family: Menlo, Monaco, 'Droid Sans Mono', Consolas, 'Lucida Console',
    'Courier New', monospace;
  margin: 0 auto;
  background-color: #f6f6f6;
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
