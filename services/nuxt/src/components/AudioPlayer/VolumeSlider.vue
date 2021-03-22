<template>
  <div class="volumeSlider">
    <v-menu
      :close-on-content-click="false"
      top
      :offset-y="true"
      dark
      transition="slide-y-transition"
      open-on-hover
      elevation="10"
    >
      <template v-slot:activator="{ on }">
        <v-btn
          icon
          v-on="on"
        >
          <v-icon class="album-overlay-more">
            mdi-volume-vibrate
          </v-icon>
        </v-btn>
      </template>
      <v-slider
        v-model="mappedVolume"
        dark
        class="volume-slider"
        vertical
        min="0"
        max="1"
        step="0.01"
        color="var(--primary-yellow)"
        background-color="#272727"
      />
    </v-menu>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  props: {
    id: {
      type: String,
      default: '',
    },
  },
  data () {
    return {
      playlistDialog: false,
    };
  },
  computed: {
    ...mapState(['volume']),
    mappedVolume: {
      get () {
        return this.volume;
      },
      set (val) {
        this.$store.dispatch('setVolume', `${val}`);
      },
    },
  },
  methods: {
    addToQueue: function () {
      this.$store.dispatch("setQueue", { "playlist": this.id });
    },
    addToLibrary: function () {
      this.$store.dispatch("addToLibrary", { 'playlist': this.id });
    },
  },
};
</script>

<style scoped>
.volumeSlider {
  display:flex;
  align-items: center;
  padding: 5px;
}
.v-menu__content {
  overflow-y: hidden !important;
}
</style>
