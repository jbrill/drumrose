<template>
  <v-app dark class="app">
    <v-content>
      <v-app-bar color="#f0f0f0" v-if="!isAuthorized" sticky @click="authorizeAppleMusic" short dense class="authorize-apple-music">
        <span class="authorize-apple-music-text">
          <v-btn @click="authorizeAppleMusic" small color="black">Sign in</v-btn> to Apple Music to gain full access to tracks and sync your library.
        </span>
      </v-app-bar>
      <v-container class="content-contain" justify-space-between fluid d-flex>
        <div class="left-contain"><LeftContain /></div>
        <div class="main-contain">
          <Navbar />
          <RegisterBanner v-if="!auth.loggedIn" />
          <nuxt class="feed-contain" />
        </div>
        <v-divider vertical></v-divider>
        <RightContain />
      </v-container>
      <transition name="fade">
        <Snackbar />
      </transition>
      <transition name="fade">
        <AudioPlayer />
      </transition>
    </v-content>
  </v-app>
</template>

<script>
import { mapState } from 'vuex';
import { getUserDetail } from '~/api/api'
import Navbar from '~/components/Navbar';
import AudioPlayer from '~/components/AudioPlayer/AudioPlayer';
import LeftContain from '~/components/LeftContain';
import RightContain from '~/components/RightContain';
import Snackbar from '~/components/Snackbar';
import RegisterBanner from '~/components/RegisterBanner';


export default {
  components: {
    Navbar,
    AudioPlayer,
    LeftContain,
    RightContain,
    Snackbar,
    RegisterBanner,
  },
  computed: {
    ...mapState(['auth', 'isAuthorized', 'nowPlayingItem']),
    items () {
      return [
        {
          name: 'Artists',
          children: this.artists
        }
      ]
    },
  },
  methods: {
    async authorizeAppleMusic() {
      MusicKit.getInstance().authorize().then( async (resp) => {
        console.log(resp);
        // check to see if user is an authorized apple music user
        const userResp = await getUserDetail('', 'john2');
        if (userResp.data.is_authorized_apple_music_user === false) {
            // send patch to set authorized apple music user
        }
        console.log(userResp);
      });
    },
  }, 
};
</script>

<style scoped>
.app {
  font-family: Menlo, Monaco, 'Droid Sans Mono', Consolas, 'Lucida Console',
    'Courier New', monospace;
  margin: 0 auto;
  background-color: #252525;
}
.left-contain, .main-contain, .right-contain {
  overflow: auto;
	height: auto;
	-webkit-overflow-scrolling: touch;
	-ms-overflow-style: none;
}
.main-contain {
  padding-top: 0;
  width: 65vw;
}
.left-contain {
  width: 15vw;
  justify-content: center;
  display: flex;
  padding: 0;
}
.right-contain {
  width: 20vw;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
}
.feed-contain {
  height: 100%;
}
.left-contain::-webkit-scrollbar, .main-contain::-webkit-scrollbar, .right-contain::-webkit-scrollbar {
  display: none;
}
.content-contain {
  background-image: linear-gradient(180deg,#14181c 0,#14181c 250px,#2c3440);
  background-color: var(--primary-black-light);
  flex: 1;
  display: flex;
  overflow: hidden;
  height: 100vh;
  padding: 0;
  position: relative;
  width: 100%;
  backface-visibility: hidden;
  will-change: overflow;
}
@media (prefers-color-scheme: dark) {
  .app {
    background-color: black;
  }
}

>>>.authorize-apple-music .v-toolbar__content {
  text-align: center;
}
>>>.authorize-apple-music-text {
  width: 100%;
  font-size: small;
  color: black;
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
