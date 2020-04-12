<template>
  <div ref="dropdownMenu" class="postActionMoreContain">
    <i class="audioMore material-icons" @click="showDropdown = !showDropdown">
      more_horiz
    </i>
    <transition name="slide-y">
      <div v-if="showDropdown" class="postActionListContain">
        <ul class="postActionList">
          <li>Tune</li>
          <li>Share</li>
          <li>Report</li>
        </ul>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  data () {
    return {
      showDropdown: false,
    };
  },
  beforeMount () {
    document.addEventListener('click', this.documentClick);
  },
  beforeDestroy () {
    document.removeEventListener('click', this.documentClick);
  },
  methods: {
    documentClick (e) {
      const el = this.$refs.dropdownMenu;
      const { target } = e;
      if (el !== target && !el.contains(target)) {
        if (this.showDropdown === true) {
          this.showDropdown = false;
        }
      }
    },
  },
};
</script>

<style scoped>
.audioMore {
  color: white;
  margin-left: 1rem;
  margin-top: 0.5rem;
  font-size: 2rem;
  position: absolute;
  right: 1rem;
  top: 0;
}
.audioMore:hover, .audioMore:focus {
  color: #772ce6;
}
.postActionList {
  background-color: white;
  border: 1px solid black;
  padding: 0;
  width: 100%;
}
.postActionList:hover, .postActionList:focus {
  cursor: pointer;
}
.postActionListContain {
  right: 2rem;
  margin-top: -4em;
  position: absolute;
}
.postActionList li {
  list-style: none;
  padding: 1rem;
  text-align: left;
  margin-left: 0;
  font-size: 0.7rem;
}
.postActionList li:hover, .postActionList li:focus {
  background-color: #f5f5f5;
  color: #772ce6;
}
</style>
