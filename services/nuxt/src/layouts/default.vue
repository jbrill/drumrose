<template>
  <v-app dark class="app">
    <v-content>
      <v-app-bar><Navbar /></v-app-bar>
      <v-app-bar color="#f0f0f0" v-if="!isAuthorized" short dense class="authorize-apple-music">
        <span class="authorize-apple-music-text">
          <v-btn @click="authorizeAppleMusic" small color="black">Sign in</v-btn> to Apple Music to gain full access to tracks, connect with friends, and view your library.
        </span>
      </v-app-bar>
      <v-app-bar color="#f0f0f0" v-if="!isAuthorized" short dense class="authorize-apple-music">
        <span class="authorize-apple-music-text">
          <v-btn small color="black" @click="authorizeAppleMusic">Go Pro</v-btn> to gain stats, advanced discovery algorithms, and ad-free browsing.
        </span>
      </v-app-bar>
      <v-container fluid d-flex>
        <MusicLibrary />
        <nuxt class="center-contain" />
      </v-container>
      <transition name="fade">
        <AudioPlayer v-if="nowPlayingItem" />
      </transition>
    </v-content>
  </v-app>
</template>

<script>
import { mapState } from 'vuex';
import { getUserDetail } from '~/api/api'
import Navbar from '~/components/Navbar';
import AudioPlayer from '~/components/AudioPlayer';
import MusicLibrary from '~/components/MusicLibrary';


export default {
  components: {
    Navbar,
    AudioPlayer,
    MusicLibrary,
  },
  computed: {
    ...mapState(['isAuthorized']),
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
.music-search-contain {
  width: 20%;
  margin: 1rem;
  align-self: flex-start;
}
.center-contain {
  width: 80%;
}
.library-menu-contain {
  list-style: none;
}
>>>.music-searchbar div {
  padding: 0;
}
>>>.music-searchbar-textfield input {
  font-size: 0.8rem;
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
