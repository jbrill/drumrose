<template>
  <v-speed-dial
    v-model="fab"
    :top="top"
    :bottom="bottom"
    :right="right"
    :left="left"
    :direction="direction"
    :open-on-hover="hover"
    :transition="transition"
    fixed
    dark
    elevation="50"
    style="z-index: 100"
  >
    <template v-slot:activator>
      <v-badge
        fixed
        left
        top
        avatar
        bordered
        elevation="100"
        overlap
        :disabled="queue.length === 0"
        :content="queue.length > 0 ? queue.length : '0'"
        color="var(--primary-black-light)"
      >
        <v-btn
          v-model="fab"
          color="var(--primary-purple)"
          dark
          :disabled="queue.length === 0"
          fab
        >
          <v-icon v-if="fab">
            mdi-close
          </v-icon>
          <v-icon v-else>
            mdi-playlist-music
          </v-icon>
        </v-btn>
      </v-badge>
    </template>
    <v-list
      v-if="queue.length > 0"
      :close-on-content-click="false"
      offset-y
      max-height="60vh"
      nudge-top="-5vh"
      width="35vw"
      two-line
      elevation="20"
      class="queueMenu"
      style="
        margin-right: 35vw; z-index: 50;
      "
    >
      <v-layout flex justify-space-between align-items-center>
        <v-subheader v-if="queue.length > 0">
          Up Next - {{ queue.length }} Tracks
        </v-subheader>
        <v-subheader v-else>
          Up Next - {{ queue.length }} Track
        </v-subheader>
        <v-layout
          flex
          style="align-items: center; justify-content: flex-end;"
        >
          <v-btn
            small
            color="var(--primary-red)"
            @click="clearQueue"
          >
            Clear
          </v-btn>
          <v-btn elevation="2" icon>
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-layout>
      </v-layout>
      <v-list-item-group
        v-model="selected"
      >
        <template v-for="(track, index) in queue">
          <v-hover
            :key="`track-${index}`"
          >
            <v-list-item>
              <QueueItem :track-object="track" />
            </v-list-item>
          </v-hover>
        </template>
      </v-list-item-group>
    </v-list>
    <v-list
      v-else
      :close-on-content-click="false"
      offset-y
      max-height="10vh"
      nudge-top="-5vh"
      width="35vw"
      two-line
      class="queueMenu"
      style="
        margin-right: 35vw; z-index: 50;
      ">
      <v-subheader>Up Next - {{ queue.length }} Tracks</v-subheader>
      <v-list-item>Add a track to the queue</v-list-item>
    </v-list>
  </v-speed-dial>
</template>

<script>
import { mapState } from 'vuex';
import QueueItem from '~/components/AudioPlayer/QueueItem';


export default {
  components: {
    QueueItem,
  },
  data: () => ({
    direction: 'top',
    fab: false,
    fling: false,
    hover: false,
    tabs: null,
    top: false,
    right: true,
    bottom: true,
    left: false,
    transition: 'slide-y-reverse-transition',
    selected: null,
  }),
  computed: {
    ...mapState(['nowPlayingItem', 'queue']),
    activeFab () {
      switch (this.tabs) {
        case 'one': return { class: 'purple', icon: 'account_circle' }
        case 'two': return { class: 'red', icon: 'edit' }
        case 'three': return { class: 'green', icon: 'keyboard_arrow_up' }
        default: return {}
      }
    },
  },
  watch: {
    selected: function (idx) {
      this.selectTrack(idx);
    },
    top (val) {
      this.bottom = !val;
    },
    right (val) {
      this.left = !val;
    },
    bottom (val) {
      this.top = !val;
    },
    left (val) {
      this.right = !val;
    },
  },
  methods: {
    async selectTrack (trackIdx) {
      try {
          await this.$store.dispatch("setQueue", {
            'song': this.queue[trackIdx].id,
          });
          this.$store.dispatch("play");
        } catch (err) {
          console.error(err);
        }
    },
    async clearQueue () {
      try {
        await this.$store.dispatch("setQueue", {});
      } catch (err) {
        console.error(err);
      }
    },
  },
};

</script>

<style>
.queueMenu {
  overflow-y: scroll;
  height: 50vh;
  overflow: auto;
}
span.v-badge__badge {
  display: flex !important;
  align-items: center !important;
  justify-content: center;
  font-family: Arial, Helvetica, sans-serif !important;
}
</style>
