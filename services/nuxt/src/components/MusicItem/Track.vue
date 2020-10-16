<template>
  <div v-if="!loading">
    <v-badge
      avatar
      bordered
      overlap
      style="width: 100%"
      icon="mdi-waveform"
      color="var(--primary-purple)"
    >
      <Artwork
        :id="trackObject.id"
        :is-playable="isPlayable"
        :is-actionable="isActionable"
        :artwork-url="appleImage"
        :link="'/tracks/' + trackObject.id"
        type="song"
      />
    </v-badge>
    <div class="textContain">
      <nuxt-link
        class="songName"
        :to="'/tracks/' + trackObject.id"
      >
        <span
          ref="songName"
          class="songName"
        >{{ trackObject.attributes.name }}</span>
      </nuxt-link>
      <nuxt-link
        :to="'/artists/' + 
          trackObject.relationships.artists.data[0].id"
        class="artistName"
      >
        <span
          ref="curatorName"
          class="artistName"
        >{{ trackObject.attributes.artistName }}</span>
      </nuxt-link>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import Artwork from '~/components/MusicItem/Artwork';

import { favoriteTrack } from '~/api/api';


export default {
  components: {
    Artwork,
  },
  props: {
    id: {
      type: String,
      default: '',
    },
    isActionable: {
      type: Boolean,
      default: false,
    },
    isPlayable: {
      type: Boolean,
      default: false,
    },
  },
  async asyncData ({ store }) {
    try {
       /***await axios.get(
				`https://teton.drumrose.io/api/tracks/${this.trackObject.id}/`,
				{
					headers: {
						Authorization: `Bearer ${this.$auth.getToken('auth0')}`,
					},
				}
			)***/
    } catch (err) {
      console.error("err.response");
      console.error(err.response);
      if (err.response == 409) {
        console.log("409!");
      } 
      console.error(err);
    }
  },
  data () {
    return {
      loading: true,
      playlistDialog: false,
      artistName: '',
      artworkUrl: '',
      name: '',
      trackObject: {},
    };
  },
  computed: {
    ...mapState(['nowPlayingItem', 'playbackState', 'queue']),
    appleImage () {
      console.log("this.trackObject");
      console.log(this.trackObject);
      return this.trackObject.attributes.artwork.url.replace(
        '{w}', '250'
      ).replace(
        '{h}', '250'
      );
    },
  },
  async mounted () {
    try {
      const resp = await this.$store.getters.fetch(
        `/v1/catalog/us/songs/${this.id}`
      );
      console.log(resp);
      this.trackObject = resp.data[0];
      this.loading = false;
    } catch (err) {
      this.loading = false;
      console.error(err);
    }
  },
  created () {
    console.log(this.trackObject);
  },
  methods: {
    pauseTrack: async function (event) {
      event.preventDefault();
      this.$store.dispatch("pause");
    },
    favoriteItem: async function (event) {
      await favoriteTrack(this.id);
    },
    playTrack: function (event) {
      event.preventDefault();
      console.log(this.id);
      this.$store.dispatch("setQueue", { "song": this.id } ).then( () => {
        this.$store.dispatch("play");
      });
    },
  },
};
</script>

<style scoped>
@media screen and (prefers-color-scheme: dark) {
  .songName {
    color: black;
  }
  .songName:hover, .songName:focus {
    color: black;
  }
  .artistName:hover, .artistName:focus {
    color: black;
  }
  .textContain {
    color: grey;
  }
  .posterInfo {
    color: black;
  }
  .posterName {
    color: black;
  }
  .posterHandle {
    color: black;
  }
  .postDate {
    color: black;
  }
  .postTime {
    color: black;
  }
  .audioAction {
    color: black;
  }
  .audioFavorite:hover, .audioFavorite:focus {
    color: grey;
  }
}
>>>.v-list-item {
  min-height: 2rem;
}
>>>.v-sheet {
  padding: 0;
}
.artistName {
  font-size: 0.8rem;
  margin-bottom: 0;
  padding-top: 5px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  opacity: 0.8;
}
.songName {
  color: white;
  font-size: 0.75rem;
  font-weight: 600;
  margin-bottom: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  opacity: 0.9;
}
.songName:hover, .songName:focus {
  cursor: pointer;
  color: white;
  opacity: 1;
}
.artistName:hover, .artistName:focus {
  cursor: pointer;
  color: white;
  opacity: 1;
}
.textContain {
  display: flex;
  bottom: 0;
  width: 100%;
  padding-top: 0.5rem;
  flex-direction: column;
}
</style>
