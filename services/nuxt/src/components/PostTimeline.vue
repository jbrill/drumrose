<template>
  <div class="timeline-wrap">
    <span
      class="timeline-time timeline-time-begin"
    >
      {{ currentPlaybackTime }}
    </span>
      <v-progress-linear
        v-model="currentPlaybackTime"
        :buffer-value="bufferedProgress || 100"
        color="var(--primary-red)"
      ></v-progress-linear>
      <span class="timeline-time timeline-time-end">
        {{ currentPlaybackDuration }}
      </span>
  </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex';

export default {
  data () {
    return {
      wheelPosition: "0%",
			mousePosition: "0%",
      dragging: false,
      startedPlaying: false,
    };
  },
  computed: {
    ...mapGetters({
      currentPlaybackDuration: 'getCurrentPlaybackDuration',
      currentPlaybackTime: 'getCurrentPlaybackTime',
    }),
    ...mapState([
      'bufferedProgress',
      'playbackTime',
    ]),
  },
	mounted () {
    window.addEventListener('mouseup', this.stopDrag);
	},
  methods: {
    startDrag () {
      this.dragging = true;
			this.startedPlaying = true;
    },
    stopDrag () {
      this.dragging = false;
    },
    doDrag (event) {
      if (this.dragging) {
        const wheelOffset = 100 * (
          event.clientX / this.$refs.timeline.clientWidth
        );
				if (wheelOffset === 0) console.log(event);
				if (wheelOffset === 0) return;
        this.wheelPosition = wheelOffset + "%";
      }
    },
    moveWheel (event) {
			const wheelOffset = 100 * (
        event.offsetX / this.$refs.timeline.clientWidth
      );
			this.wheelPosition = wheelOffset + "%";
      const currPos = (
        event.offsetX / this.$refs.timeline.clientWidth
      ) * this.$store.state.playbackTime.currentPlaybackDuration;
      this.$store.dispatch("seek", currPos); 
    },
		hoverTimeline (event) {
			if (!this.dragging) {
				const wheelOffset = 100 * (
          event.offsetX / this.$refs.timeline.clientWidth
        );
				this.mousePosition = wheelOffset + "%";
			}
		},
  }, 
};
</script>

<style>
.timeline-wrap {
	text-align: center;
	width: 100%;
	height: 100%;
	display: flex;
  justify-content: center;
  align-items: center; 
}
.post-timeline {
  width: 90%;
  height: 60%;
  margin: 0 auto;
  background-color: #ccc;
	position: relative;
}
.post-timeline-buffer {
  height: 100%;
  margin: 0 auto;
  background-color: #F5F5F5;
	position: absolute;
}
.post-timeline:hover, .post-timeline:focus {
	opacity: 1;
  cursor: pointer;
}
.timeline-time {
  font-size: 0.7rem;
  padding: 10px;
}
.timeline-time-begin {
  color: var(--primary-red);
}
.timeline-time-end {
  color: white;
}
.timeline-before-wheel {
	position: absolute;
	height: 100%;
	background-color: var(--primary-red);
  z-index: 100;
}
.timeline-mouse-hover {
	position: absolute;
	height: 4px;
	background-color: var(--primary-purple);
}
</style>
