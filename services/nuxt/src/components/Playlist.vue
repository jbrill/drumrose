<template>
  <div class="playlist-contain">
    <div class="playlist-title-artwork-contain">
      <div class="artwork-contain" />
      <nuxt-link to="/playlists/test/">
        <h2 class="playlist-title">
          {{ playlist.title }}
        </h2>
      </nuxt-link>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'Playlist',
  props: {
    'playlist': {
      type: Object,
      default: () => {},
    },
  },
  computed: mapState(['nowPlayingItem', 'nowPlayingPost', 'playbackState']),
  methods: {
  },
  async created () {
    try {
      const resp = await getPlaylistDetail(
        this.$auth.getToken('auth0'),
        this.id
      )
      console.log(resp)
      this.pageId = resp.data.playlist.page_id
    } catch (err) {
      console.error(err.response)
      if (err.response == 409) {
        console.log("409!")
      }
      console.error(err)
    }
  },
};
</script>

<style scoped>
.playlist-title-artwork-contain {
  display: inline;
  text-align: left;
}
.playlist-track-artwork-contain {
  position: relative;
  height: 5rem;
}
.playlist-track-artwork-contain li {
  list-style: none;
  position: absolute;
  height: 100%;
}
.playlist-artwork {
  height: 100%;
  width: auto;
  border-radius: 5px;
}
.playlist-title {
  font-size: 1rem;
  color: #ccc;
  font-weight: bolder;
}
</style>
