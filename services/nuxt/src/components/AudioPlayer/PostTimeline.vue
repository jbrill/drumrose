<template>
  <div class="timeline-wrap">
    <v-slider
      v-if="playbackTime"
      v-model="playbackTime.currentPlaybackTime"
      color="var(--primary-yellow)"
      track-color="#ccc"
      :max="playbackTime.currentPlaybackDuration"
      @change="changePosition"
    >
      <template v-slot:prepend color="var(--primary-yellow)">
        {{ currentPlaybackTime }}
      </template>
      <template v-slot:append>
        {{ currentPlaybackDuration }}
      </template>
    </v-slider>
  </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex';

export default {
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
  methods: {
    changePosition (e) {
      console.log(e);
			this.$store.dispatch("seek", e);
    },
  }, 
};
</script>

<style scoped>
>>>.v-messages {
  display: none;
}
>>>.v-input__prepend-outer {
  font-size: 0.7rem;
  color: var(--primary-yellow);
}
>>>.v-input__append-outer {
  font-size: 0.7rem;
}
.timeline-wrap {
	text-align: center;
	width: 40%;
	display: flex;
  justify-content: center;
  align-items: center; 
}
>>>.v-slider__thumb {
	height: 8px;
	width: 8px;
  cursor: grabbing;
}

>>>.v-slider--horizontal .v-slider__track-container {
	height: 2px;
}
>>>.v-input {
  align-items: center !important;
  height: 100%;
}
>>>.v-input__slot {
  margin-bottom: 0;
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
  color: var(--primary-yellow);
}
.timeline-time-end {
  color: white;
}
.timeline-before-wheel {
	position: absolute;
	height: 100%;
	background-color: var(--primary-yellow);
  z-index: 100;
}
.timeline-mouse-hover {
	position: absolute;
	height: 4px;
	background-color: var(--primary-purple);
}
</style>
