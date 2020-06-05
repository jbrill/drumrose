<template>
  <v-app dark class="app">
    <v-content>
      <v-app-bar><Navbar /></v-app-bar>
      <v-container fluid d-flex>
        <div class="music-search-contain">
          <v-toolbar
            dense
            flat
            floating
            elevation="0"
            color="transparent"
            class="music-searchbar"
          >
            <v-text-field
              hide-details
              prepend-icon="search"
              placeholder="Search for music"
              single-line
              class="music-searchbar-textfield"
            />
          </v-toolbar>
          <div>
            <v-btn small text color="#ccc">
              LIBRARY
            </v-btn>
            <ul class="library-menu-contain">
              <li>
                <v-btn x-small color="transparent" tile>
                  <v-icon x-small left>
                    mdi-waveform
                  </v-icon> Tracks
                </v-btn>
              </li>
              <li>
                <v-btn x-small color="transparent" tile>
                  <v-icon x-small left>
                    mdi-album
                  </v-icon> Albums
                </v-btn>
              </li>
              <li>
                <v-btn x-small color="transparent" tile>
                  <v-icon x-small left>
                    mdi-face
                  </v-icon> Artists
                </v-btn>
              </li>
            </ul>
          </div>
          <div>
            <v-btn x-small text color="#ccc">
              PLAYLISTS
            </v-btn><v-btn
              color="var(--primary-purple)"
              x-small
            >
              Create a Playlist
            </v-btn>
          </div>
        </div>
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
import AudioPlayer from '~/components/AudioPlayer';


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
.music-search-contain {
  width: 20%;
  margin: 1rem;
  align-self: flex-start;
}
.center-contain {
  width: 80%;
  margin: 1rem;
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
