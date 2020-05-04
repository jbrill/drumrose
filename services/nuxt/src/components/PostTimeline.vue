<template>
  <div
		class="timeline-wrap"
		@click="moveWheel"
		@mouseleave="stopDrag"
		@mousedown="startDrag"
		@mousemove="doDrag"
	>
		<div 
			ref="timeline"
			class="post-timeline"
		>
			<div v-if="startedPlaying" :style="{ width: wheelPosition }" class="timeline-before-wheel"></div>
			<!---<div v-if="startedPlaying" :style="{ width: mousePosition }" class="timeline-mouse-hover"></div>-->
			<!---<div v-if="startedPlaying" :style="{ left: wheelPosition }" ref="wheel" class="post-timeline-wheel"></div>-->
		</div>
	</div>
</template>

<script>
export default {
  data() {
    return {
      wheelPosition: "0%",
			mousePosition: "0%",
      dragging: false,
      startedPlaying: false,
    }
  },
	mounted () {
    window.addEventListener('mouseup', this.stopDrag);
	},
  methods: {
    startDrag() {
      this.dragging = true;
			this.startedPlaying = true;
    },
    stopDrag() {
      this.dragging = false;
    },
    doDrag(event) {
      if (this.dragging) {
				console.log("DRAGGING");
				
        const wheelOffset = 100 * (event.clientX / this.$refs.timeline.clientWidth);
				if (wheelOffset === 0) console.log(event);
				if (wheelOffset === 0) return;
        this.wheelPosition = wheelOffset + "%";
				console.log(this.wheelPosition);
      }
    },
    moveWheel (event) {
			const wheelOffset = 100 * (event.offsetX / this.$refs.timeline.clientWidth);
			this.wheelPosition = wheelOffset + "%";
    },
		hoverTimeline(event) {
			console.log(event);
			if (!this.dragging) {
				const wheelOffset = 100 * (event.offsetX / this.$refs.timeline.clientWidth);
				this.mousePosition = wheelOffset + "%";
			}
		}
  }, 
}
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
  background-color: #F2F2F2;
	position: relative;
}
.post-timeline:hover, .post-timeline:focus {
	opacity: 1;
}
.timeline-before-wheel {
	position: absolute;
	height: 100%;
	background-color: var(--primary-red);
}
.timeline-mouse-hover {
	position: absolute;
	height: 4px;
	background-color: var(--primary-purple);
}
</style>
