<template>
<div id="app">
  <v-app class="app">
      <v-app-bar color="#f0f0f0" v-if="!isAuthorized" sticky @click="authorizeAppleMusic" short dense class="authorize-apple-music">
        <span class="authorize-apple-music-text">
          <v-btn @click="authorizeAppleMusic" small color="black">Sign in</v-btn> to Apple Music to gain full access to tracks and sync your library.
        </span>
      </v-app-bar>
      <Navbar />
       <RegisterBanner v-if="!auth.loggedIn" />
       <!-- <div class="left-contain"><LeftContain /></div>-->
      <v-content class="content-contain">
      <v-container class="main-contain">
        <nuxt class="feed-contain" />
      </v-container>
      <transition name="fade">
        <Snackbar />
      </transition>
      <transition name="fade">
        <AudioPlayer />
      </transition>
    </v-content>
  </v-app>
</div>
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
        // check to see if user is an authorized apple music user
        const userResp = await getUserDetail('', 'john2');
        if (userResp.data.is_authorized_apple_music_user === false) {
            // send patch to set authorized apple music user
        }
      });
    },
  }, 
};
</script>

<style scoped>
.app {
  font-family: Menlo, Monaco, 'Droid Sans Mono', Consolas, 'Lucida Console',
    'Courier New', monospace;
  background-color: #252525;
}
.main-contain {
  width: 80vw;
  margin: 0 auto;
  margin-top: 3vh;
}
.feed-contain {
  height: 100%;
}
.content-contain {
  background-image: linear-gradient(180deg,#14181c 0,#14181c 250px,#2c3440);
  background-color: var(--primary-black-light);
  padding: 0;
  position: relative;
  width: 100%;
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
