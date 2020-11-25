<template>
  <div class="queueContain">
    <QueueItem
      :track-object="nowPlayingItem"
      :now-playing="true"
    />
    <v-menu
      left
      top
      dark
      :close-on-content-click="false"
      offset-y
      max-height="50vh"
      width="45vw"
      nudge-top="25vh"
      class="queueMenu"
      transition="slide-y-reverse-transition"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          icon
          x-small
          class="queueButton"
          v-bind="attrs"
          v-on="on"
        >
          <v-icon>queue_music</v-icon>
        </v-btn>
      </template>
      <v-list two-line>
        <v-subheader>Up Next - {{ queue.length }} Tracks</v-subheader>
        <v-list-item-group
          v-model="selected"
          multiple
          active-class="pink--text"
        >
          <template v-for="(track, index) in queue">
            <v-list-item :key="'track' + index">
              <QueueItem :track-object="track" />
            </v-list-item>
          </template>
        </v-list-item-group>
      </v-list>
    </v-menu>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import QueueItem from '~/components/AudioPlayer/QueueItem';


export default {
  components: {
    QueueItem,
  },
  data: () => ({
    selected: null,
  }),
  computed: {
    ...mapState(['nowPlayingItem', 'queue']),
  },
  created () {
    console.log(this.nowPlayingItem);
  },
  methods: {
  },
};

</script>

<style scoped>
.queueContain {
  display: flex;
}
.queueButton {
  margin-left: 5px;
  align-self: center;
  opacity: 0.8;
}
.queueButton:hover, .queueButton:focus {
  opacity: 1
}
.queueMenu {
  overflow-y: scroll;
  height: 50vh;
}
</style>
