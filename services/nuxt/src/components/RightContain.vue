<template>
  <div class="right-content-contain">
    <div class="content-contain-right">
      <v-btn x-small text color="#ccc">
        People to Follow
      </v-btn>
      <v-list dense>
        <v-list-item-group>
          <v-list-item v-for="musicItem in recentlyPlayed">
            <v-list-item-icon>
              <v-icon>mdi-person</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title v-text="musicItem.attributes.name"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </div>
    <v-divider></v-divider>
    <div class="content-contain-right">
      <v-btn x-small text color="#ccc">
        Your Favorites
      </v-btn>
      <v-list dense>
        <v-list-item-group>
          <v-list-item v-for="musicItem in recentlyPlayed">
            <v-list-item-icon>
              <v-icon>mdi-waveform</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title v-text="musicItem.attributes.name"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </div>
    <v-divider></v-divider>
    <div class="content-contain-right">
      <v-btn x-small text color="#ccc">
        Listening History
      </v-btn>
      <v-list dense>
        <v-list-item-group>
          <v-list-item v-for="musicItem in history">
            <v-list-item-icon>
              <v-icon>mdi-waveform</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title v-text="musicItem"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
			</v-list-item-group>
		</v-list>
  </div>
  <v-divider></v-divider>
  <ul class="outbound-links-contain">
    <li v-for="outboundLink in outboundLinks" :key="outboundLink">
      <v-btn x-small nuxt-link text :to="outboundLink.toLowerCase()" >
        {{ outboundLink }}
      </v-btn>
    </li>
  </ul>
  </div>
</div>
</template>

<script>
import { mapState, mapGetters } from 'vuex';
import { getFavorites } from '~/api/api';
import SearchBar from '~/components/SearchBar';

export default {
  async asyncData () {
    const favoritesResponse = await getFavorites();
    return {
      "favorites": favoritesResponse.data,
    }    
  },
  components: {
    SearchBar
  },
  data: () => ({
    favorites: [],
    outboundLinks: [
      'About',
      'Terms',
      'Contact',
    ],
  }),
  computed: {
    ...mapState(['isAuthorized', 'history']),
    ...mapGetters(['recentlyPlayed', 'heavyRotation']),
  }, 
};
</script>

<style scoped>
.right-content-contain {
  width: 100%;
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
</style>
