<template>
  <div>
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
        :artwork-url="appleImage"
        :link="'/albums/' + id"
        type="album"
      />
    </v-badge>
    <MusicFooter
      :primary-name="attributes.name"
      :primary-link="'/albums/' + id"
      :secondary-name="attributes.artistName"
      :secondary-link="'/artists/' + artistId"
    />
  </div>
</template>

<script>
import { mapState } from 'vuex';
import Artwork from '~/components/MusicItem/Artwork';
import MusicFooter from '~/components/MusicItem/MusicFooter';
import { favoriteTrack } from '~/api/api';


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
    attributes: {
      type: Object,
      default: () => {},
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
    };
  },
  computed: {
    ...mapState(['nowPlayingItem', 'playbackState', 'queue']),
    appleImage () {
      return this.attributes.artwork.url.replace(
        '{w}', this.attributes.artwork.width
      ).replace(
        '{h}', this.attributes.artwork.height
      );
    },
  },
  async created () {
    try {
      const resp = await this.$store.getters.fetch(
        `/v1/catalog/us/albums/${this.id}`
      );
      console.log(resp);
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
