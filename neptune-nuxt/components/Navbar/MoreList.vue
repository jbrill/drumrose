<template>
  <div ref="more--list" class="more--menu__contain">
    <i @click="showMoreMenu = !showMoreMenu" class="material-icons"
      >arrow_drop_down</i
    >
    <transition name="fade">
      <div v-if="showMoreMenu" class="more--menu__contain">
        <ul class="more--list__menu">
          <li>
            <nuxt-link to="/profile"
              ><button class="more-list__menu__btn">Profile</button></nuxt-link
            >
          </li>
          <li>
            <nuxt-link to="/about"
              ><button class="more-list__menu__btn">About</button></nuxt-link
            >
          </li>
          <li>
            <nuxt-link to="/settings"
              ><button class="more-list__menu__btn">Settings</button></nuxt-link
            >
          </li>
          <li>
            <nuxt-link to="/auth/sign-off"
              ><button class="more-list__menu__btn">Sign Off</button></nuxt-link
            >
          </li>
        </ul>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  methods: {
    documentClick(e) {
      // if we click outside element, hide menu
      let el = this.$refs.moreList;
      let target = e.target;
      if (el !== target && !el.contains(target)) {
        this.showMoreMenu = this.showMoreMenu ? false : true;
      }
    }
  },
  created() {
    if (!process.server) {
      document.addEventListener("click", this.documentClick);
    }
  },
  destroyed() {
    // important to clean up!!
    if (!process.server) {
      document.removeEventListener("click", this.documentClick);
    }
  },
  data() {
    return {
      showMoreMenu: false
    };
  }
};
</script>

<style scoped>
.more--menu__contain {
  margin-right: 3rem;
}
.more--menu__contain i {
  font-size: 2rem;
  color: white;
  margin-top: 0.5rem;
}
.more--menu__contain i:hover {
  color: #f4f4f4;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
.more--list__menu {
  position: absolute;
  top: 4rem;
  background-color: black;
  z-index: 10;
  right: 0;
  padding: 0;
}
.more--list__menu {
  width: 8rem;
  padding: 0;
}
.more--list__menu li {
  width: 100%;
  list-style: none;
}
.more--list__menu li * {
  width: 100%;
}
.more-list__menu__btn {
  background-color: black;
  color: white;
  border: none;
  height: 3rem;
}
.more-list__menu__btn:hover {
  cursor: pointer;
  color: #f5f5f5;
  background-color: #030114;
}
</style>
