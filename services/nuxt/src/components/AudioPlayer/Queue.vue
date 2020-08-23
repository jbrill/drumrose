<template>
<div class="queueContain">
  <QueueItem
    :trackObject="nowPlayingItem"
    :nowPlaying="true"
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
				@click="showQueue"
				class="queueButton"
				v-on="on"
				v-bind="attrs"
			>
				<v-icon>queue_music</v-icon>
			</v-btn>
    </template>
    <v-list>
      <v-subheader>Up Next - {{ queue.length }} Tracks</v-subheader>
      <v-list-item v-for="track in queue">
        <QueueItem :trackObject="track" />
      </v-list-item>
    </v-list>
  </v-menu>
</div>
</template>

<script>
import QueueItem from '~/components/AudioPlayer/QueueItem';
import { mapState } from 'vuex';


export default {
  data: () => ({
    items: [
      { title: 'Click Me' },
      { title: 'Click Me' },
      { title: 'Click Me' },
      { title: 'Click Me 2' },
    ],
  }),
  components: {
    QueueItem,
  },
  computed: {
    ...mapState(['nowPlayingItem', 'queue'])
  },
  methods: {
    showQueue () {
      console.log("queueueue");
    },
  },
  created() {
    console.log(this.nowPlayingItem)
  },
}

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
