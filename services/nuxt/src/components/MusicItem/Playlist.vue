<template>
  <div>
    <v-skeleton-loader
      v-if="loading || !attributes"
      class="mx-auto"
      type="image"
      style="height: 100%"
    />
    <v-badge
      v-else
      avatar
      bordered
      overlap
      icon="mdi-playlist-music"
      style="width: 100%; border-radius: 5px"
      class="grey lighten-1"
      color="var(--primary-purple)"
    >
      <Artwork
        :id="id"
        :is-playable="isPlayable"
        :is-actionable="isActionable"
        :artwork-url="appleImage()"
        :link="'/playlists/' + id"
        :tracks="tracks"
        type="playlist"
        :name="attributes.name"
        :artist-name="attributes.curatorName"
        :favorited="isFavorited"
      />
    </v-badge>
    <MusicFooter
      :primary-name="attributes.name"
      :primary-link="'/playlists/' + id"
      :secondary-name="attributes.curatorName"
      :secondary-link="'/people/' + attributes.curatorName"
    />
  </div>
</template>

<script>
import { mapState } from 'vuex';
import Artwork from '~/components/MusicItem/Artwork';
import MusicFooter from '~/components/MusicItem/MusicFooter';

import {
  favoriteTrack, getPlaylistDetail, createPlaylist,
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
      attributes: false,
      name: '',
      tracks: [],
      isFavorited: false,
    };
  },
  computed: {
    ...mapState(['auth', 'nowPlayingItem', 'playbackState', 'queue']),
  },
  async created () {
    if (this.$auth.loggedIn) {
      try {
        const playlistResponse = await getPlaylistDetail(
          this.$auth.getToken('auth0'),
          this.id
        );
        this.isFavorited = playlistResponse.data.playlist.favorited;
      } catch (err) {
        if (err.response.status === 409) {
          try {
            await createPlaylist(
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
    try {
      const resp = await this.$store.getters.fetch(
        `/v1/catalog/us/playlists/${this.id}`
      );
      this.attributes = resp.data[0].attributes;
      this.tracks = resp.data[0].relationships.tracks.data;
      this.loading = false;
    } catch (err) {
      console.error(err);
      this.loading = false;
    }
  },
  methods: {
    addToQueue: function () {
      this.$store.dispatch(
        "setQueue", {
          "playlist": this.id,
        }
      );
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
    appleImage () {
      console.log(this.attributes);
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
  color: white;
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
