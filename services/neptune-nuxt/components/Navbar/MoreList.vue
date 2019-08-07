<template>
  <div class="more--menu__contain">
    <!-- <profileNav /> -->
    <i
      ref="moreList"
      @click="showMoreMenu = !showMoreMenu"
      class="material-icons more--menu__contain__btn"
      >arrow_drop_down</i
    >
    <transition name="fade">
      <div v-if="showMoreMenu">
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
            <button
              @click="signOff"
              v-if="isAuthenticated"
              class="more-list__menu__btn"
            >
              Sign Off
            </button>
          </li>
        </ul>
      </div>
    </transition>
  </div>
</template>

<script>
import profileNav from "~/components/ProfileNav";
import { store } from "~/plugins/localStorage";

export default {
  components: {
    profileNav
  },
  computed: {
    isAuthenticated: function() {
      return store.getters.isAuthenticated;
    }
  },
  methods: {
    documentClick(e) {
      // if we click outside element, hide menu
      let el = this.$refs.moreList;
      let target = e.target;
      if (el !== target && !el.contains(target)) {
        if (this.showMoreMenu) {
          this.showMoreMenu = false;
        }
      }
    },
    signOff(e) {
      console.log("SIGNING OFF HERE");
      store.commit("set_api_token", null);
      store.commit("set_secret", null);
      // redirect to home
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
  z-index: -10;
}
.more--menu__contain__btn {
  font-size: 1.5rem;
  color: white;
  margin-top: 0.5rem;
}
.more--menu__contain__btn:hover {
  /* color: var(--primary-purple); */
  color: black;
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
  background-color: var(--primary-black-light);
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
  font-size: 0.8rem;
}
.more--list__menu li * {
  width: 100%;
}
.more-list__menu__btn {
  background-color: #1e1b1a;
  color: white;
  border: none;
  height: 3rem;
}
.more-list__menu__btn:hover {
  cursor: pointer;
  color: var(--primary-yellow);
  background-color: black;
}
</style>
