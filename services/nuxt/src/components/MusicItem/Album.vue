<template>
  <div>
    <v-badge
      avatar
      bordered
      overlap
      icon="mdi-record-circle-outline"
      style="width: 100%"
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
    <div class="textContain">
      <nuxt-link
        class="songName"
        :to="'/albums/' + id"
      >
        <span
          ref="songName"
          class="songName"
        >{{ attributes.name }}</span>
      </nuxt-link>
      <nuxt-link :to="'/artists/' + attributes.curatorName" class="artistName">
        <span
          ref="curatorName"
          class="artistName"
        >{{ attributes.artistName }}</span>
      </nuxt-link>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import Artwork from '~/components/MusicItem/Artwork';

import { getAlbumDetail, favoriteTrack } from '~/api/api';


export default {
  components: {
    Artwork,
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
      isLoading: true,
      playlistDialog: false,
      artistName: '',
      artworkUrl: '',
      name: '',
    };
  },
  mounted () {
    console.log(this.attributes)
  },
  computed: {
    ...mapState(['nowPlayingItem', 'playbackState', 'queue']),
    appleImage () {
      console.log("this.attributes")
      console.log(this.attributes)
      return this.attributes.artwork.url.replace(
        '{w}', '2500'
      ).replace(
        '{h}', '2500'
      );
    },
  },
  methods: {
    addToQueue: function () {
      this.$store.dispatch("setQueue", { "playlist": this.id });
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
      this.$store.dispatch("setQueue", { "playlist": this.id } ).then( () => {
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
.artistName {
  font-size: 0.8rem;
  margin-bottom: 0;
  font-weight: 600;
  padding-top: 5px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  opacity: 0.8;
}
.songName {
  font-size: 0.75rem;
  margin-bottom: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  opacity: 0.8;
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
  color: var(--primary-black-light);
}
</style>
