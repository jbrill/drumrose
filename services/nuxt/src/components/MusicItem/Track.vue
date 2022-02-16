<template>
  <div>
    <v-skeleton-loader
      v-if="loading || !trackObject || !('attributes' in trackObject)"
      class="mx-auto"
      type="image"
      style="height: 100%"
    />
    <v-container
      v-else
      class="post-container"
    >
      <v-badge
        avatar
        bordered
        overlap
        style="width: 100%; border-radius: 5px"
        class="grey lighten-1"
        icon="mdi-waveform"
        color="var(--primary-purple)"
      >
        <Artwork
          :id="trackObject.id"
          :is-playable="isPlayable"
          :is-actionable="isActionable"
          :artwork-url="appleImage()"
          :link="type === 'review' ? `people/${user}/reviews/tracks/${trackObject.id}` : `/tracks/${trackObject.id}`"
          type="song"
          :name="attributes.name"
          :artist-name="attributes.artistName"
          :favorited="isFavorited"
          :review="trackReview"
          :rating="trackRating"
        />
      </v-badge>
      <MusicFooter
        v-if="isActionable"
        :primary-name="attributes.name"
        :primary-link="'/tracks/' + trackObject.id"
        :secondary-name="attributes.artistName"
        :secondary-link="
          '/artists/' + artistId
        "
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
  getTrackDetail,
  createTrack,
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
    type: {
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
    user: {
      type: String,
      default: 'false',
    },
  },
  data () {
    return {
      loading: true,
      playlistDialog: false,
      artistName: '',
      artistId: '',
      artworkUrl: '',
      name: '',
      trackObject: {},
      attributes: {},
      isFavorited: false,
      trackReview: null,
      trackRating: null,
    };
  },
  computed: {
    ...mapState(['nowPlayingItem', 'playbackState', 'queue', 'auth']),
  },
  async created () {
    if (this.$auth.loggedIn) {
      try {
        const trackResponse = await getTrackDetail(
          this.$auth.getToken('auth0'),
          this.id
        );
        console.log(trackResponse);
        this.isFavorited = trackResponse.data.track.favorited;
        this.trackReview = trackResponse.data.track.review;
        this.trackRating = trackResponse.data.track.rating;
      } catch (err) {
        if (err.response.status === 409) {
          try {
            await createTrack(
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
        `/v1/catalog/us/songs/${this.id}`
      );
      this.attributes = resp.data[0].attributes;
      this.trackObject = resp.data[0];
      this.loading = false;
      console.log(resp.data)
      if (resp.data[0].relationships.artists.length > 0) {
        this.artistId = resp.data[0].relationships.artists.data[0].id;
      } else {
        this.artistId = resp.data[0].relationships.artists.data[0].id;
      }
    } catch (err) {
      this.loading = false;
      console.error(err);
    }
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
    appleImage () {
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
.container {
  padding: 0 !important;
}
.textContain {
  display: flex;
  bottom: 0;
  width: 100%;
  padding-top: 0.5rem;
  flex-direction: column;
}
</style>
