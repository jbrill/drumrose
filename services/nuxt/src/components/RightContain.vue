<template>
  <div class="right-content-contain">
    <div class="content-contain-right">
      <v-card class="right-snippet">
        <v-card-title class="headline">
          <v-btn width="100%" small text color="#ccc">
            People to Follow
          </v-btn>
        </v-card-title>
        <v-list dense>
          <v-list-item-group>
            <v-list-item v-for="musicItem in favorites">
              <v-list-item-icon>
                <v-icon>mdi-person</v-icon>
              </v-list-item-icon>

              <v-list-item-content>
                <v-list-item-title v-text="musicItem"></v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-card>
      <v-card class="right-snippet">
        <v-card-title class="headline">
          <v-btn width="100%" small text color="#ccc">
            Heavy Rotation
          </v-btn>
        </v-card-title>
        <v-list dense>
          <v-list-item-group>
            <v-list-item link :to="'albums/' + musicItem.id" v-for="musicItem in favorites">
              <v-list-item-icon>
                <v-icon v-if="musicItem.type === 'stations'">mdi-radio-tower</v-icon>
                <v-icon v-if="musicItem.type === 'artists'">mdi-brain</v-icon>
                <v-icon v-if="musicItem.type === 'playlists'">mdi-playlist-music</v-icon>
                <v-icon v-else-if="musicItem.type === 'albums'">mdi-record-circle</v-icon>
                <v-icon v-else-if="musicItem.type === 'songs'">mdi-waveform</v-icon>
              </v-list-item-icon>

              <v-list-item-content>
                <v-list-item-title v-text="musicItem.attributes.name"></v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-card>
      <v-card class="right-snippet">
        <v-card-title class="headline">
          <v-btn width="100%" small text color="#ccc">
            Listening History
          </v-btn>
        </v-card-title>
        <v-list dense>
          <v-list-item-group>
            <v-list-item link :to="'/albums/' + musicItem.id" v-for="musicItem in recents">
              <v-list-item-icon>
                <v-icon v-if="musicItem.type === 'playlists'">mdi-playlist-music</v-icon>
                <v-icon v-else-if="musicItem.type === 'albums'">mdi-record-circle</v-icon>
                <v-icon v-else-if="musicItem.type === 'songs'">mdi-waveform</v-icon>
              </v-list-item-icon>

              <v-list-item-content>
                <v-list-item-title v-text="musicItem.attributes.name"></v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-card>
    </div>
  <div>
    <ul class="outbound-links-contain">
      <li v-for="outboundLink in outboundLinks" :key="outboundLink">
        <v-btn x-small nuxt-link text :to="outboundLink.toLowerCase()" >
          {{ outboundLink }}
        </v-btn>
      </li>
      <li><v-btn target="_blank" href="https://www.twitter.com/getDrumrose" icon dark><v-icon>mdi-twitter</v-icon></v-btn><v-btn target="_blank" href="https://instagram.com/getDrumrose" icon dark><v-icon>mdi-instagram</v-icon></v-btn></li>
      <li><span class="company-text">© 2020 Neptune Technologies Inc.</span></li>
    </ul>
  </div>
  </div>
</div>
</template>

<script>
import { mapState, mapGetters } from 'vuex';
import { getFavorites } from '~/api/api';
import SearchBar from '~/components/SearchBar';

export default {
  async asyncData () {
  },
  async mounted() {
    const recentResponse = await this.$store.getters.recentlyPlayed;
    this.recents = recentResponse.slice(0, 5);
    const favoritesResponse = await this.$store.getters.heavyRotation;
    this.favorites = favoritesResponse.slice(0, 5);
    console.log(this.favorites)
  },
  components: {
    SearchBar
  },
  data: () => ({
    favorites: [],
    recents: [],
    outboundLinks: [
      'Support',
      'Terms of Service',
      'Privacy Policy',
    ],
  }),
  computed: {
    ...mapState(['isAuthorized', 'history']),
  }, 
};
</script>

<style scoped>
.right-content-contain {
  margin: 1rem;
  width: 18vw;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
}
.library-menu-contain {
  list-style: none;
}
.content-contain-right {
  width: 100%;
}
>>>.music-searchbar div {
  padding: 0;
}
>>>.music-searchbar-textfield input {
  font-size: 0.8rem;
}
.outbound-links-contain {
  display: list-item;
  text-align: right;
  height: 100%;
  align-items: flex-end;
  list-style-type: none;
}
.company-text {
  font-size: 0.5rem;
}
.right-snippet {
  margin-top: 1rem;
}
</style>
