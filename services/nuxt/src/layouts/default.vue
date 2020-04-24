<template>
  <div class="app">
    <Navbar /> <nuxt /> <AudioPlayer />
  </div>
</template>

<script>
import Navbar from '~/components/Navbar';
import AudioPlayer from '~/components/AudioPlayer';
import { getAppleMusicDeveloperToken } from '~/utils/post_util';


export default {
  components: {
    Navbar,
    AudioPlayer,
  },
  async mounted () {
      const res = await getAppleMusicDeveloperToken();
      // MusicKit global is now defined
      // eslint-disable-next-line no-undef
      const music = MusicKit.configure({
        developerToken: res.data.token,
        app: {
          name: 'AppleMusicKitExample',
          build: '1978.4.1',
        },
      });

      // expose our instance globally for testing
      window.music = music;
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
</style>
