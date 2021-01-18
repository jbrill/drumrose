<template>
  <div>
    <v-skeleton-loader
      v-if="loading || !attributes"
      class="mx-auto"
      type="image"
    />
    <v-container v-else>
      <v-badge
        avatar
        bordered
        overlap
        icon="mdi-record-circle-outline"
        style="width: 100%; border-radius: 5px"
        class="grey lighten-1"
        color="var(--primary-purple)"
      >
        <Artwork
          :id="id"
          :is-playable="isPlayable"
          :is-actionable="isActionable"
          :artwork-url="appleImage()"
          :tracks="tracks"
          :link="'/albums/' + id"
          type="album"
          :name="attributes.name"
        />
      </v-badge>
      <MusicFooter
        :primary-name="attributes.name"
        :primary-link="'/albums/' + id"
        :secondary-name="attributes.artistName"
        :secondary-link="'/artists/' + artistId"
      />
    </v-container>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import Artwork from '~/components/MusicItem/Artwork';
import MusicFooter from '~/components/MusicItem/MusicFooter';
import {
  favoriteTrack,
  getAlbumDetail,
  createAlbum,
} from '~/api/api';


export default {
  components: {
    Artwork,
    MusicFooter,
  },
  props: {
    id: {
      type: String,
      default: '',
    },
    tracks: {
      type: Array,
      default: () => [],
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
  data () {
    return {
      loading: true,
      playlistDialog: false,
      artistName: '',
      artworkUrl: '',
      name: '',
      artistId: '',
      attributes: false,
    };
  },
  computed: {
    ...mapState(['nowPlayingItem', 'playbackState', 'queue']),
  },
  async created () {
    if (this.$auth.loggedIn) {
      try {
        await getAlbumDetail(
          this.$auth.getToken('auth0'),
          this.id
        );
      } catch (err) {
        if (err.response.status === 409) {
          try {
            await createAlbum(
              this.$auth.getToken('auth0'),
              {
                'id': this.id,
                'name': this.name,
              }
            );
          } catch (err) {
            console.error(err);
          }
        }
      }
    }
  },
  async mounted () {
    this.loading = true;
    try {
      const resp = await this.$store.getters.fetch(
        `/v1/catalog/us/albums/${this.id}`
      );
      this.attributes = resp.data[0].attributes;
      this.artistId = resp.data[0].relationships.artists.data[0].id;
      this.loading = false;
    } catch (err) {
      this.loading = false;
      console.error(err);
    }
  },
  methods: {
    addToQueue: function () {
      this.$store.dispatch("setQueue", { "album": this.id });
    },
    pauseTrack: async function (event) {
      event.preventDefault();
      this.$store.dispatch("pause");
    },
    favoriteItem: async function (event) {
      await favoriteTrack(this.appleMusicId);
    },
    playTrack: function (event) {
      event.preventDefault();
      this.$store.dispatch("setQueue", { "album": this.id } ).then( () => {
        this.$store.dispatch("play");
      });
    },
    appleImage () {
      console.log(this.attributes)
      return this.attributes.artwork.url.replace(
        '{w}', this.attributes.artwork.width
      ).replace(
        '{h}', this.attributes.artwork.height
      );
    },
  },
};
</script>

<style scoped>
@media screen and (prefers-color-scheme: dark) {
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
</style>
