<template>
  <div id="app">
    <v-app class="app">
      <v-app-bar
        v-if="!isAuthorized"
        color="#f0f0f0"
        sticky
        short
        dense
        class="authorize-apple-music"
        @click="authorizeAppleMusic"
      >
        <span class="authorize-apple-music-text">
          <v-btn
            small
            color="black"
            @click="authorizeAppleMusic"
          >
            Sign in
          </v-btn> 
          to Apple Music to gain full access to tracks and sync your library.
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
          <AudioPlayer />
        </transition>
      </v-content>
    </v-app>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import Navbar from '~/components/Navbar';
import AudioPlayer from '~/components/AudioPlayer/AudioPlayer';
import RegisterBanner from '~/components/RegisterBanner';


export default {
  components: {
    Navbar,
    AudioPlayer,
    RegisterBanner,
  },
  computed: {
    ...mapState(['auth', 'isAuthorized', 'nowPlayingItem']),
    items () {
      return [
        {
          name: 'Artists',
          children: this.artists,
        },
      ];
    },
  },
  methods: {
    async authorizeAppleMusic () {
      try {
        this.$store.commit('authorize');
      } catch (err) {
        console.error(err);
      }
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
