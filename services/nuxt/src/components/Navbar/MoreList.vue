<template>
  <div class="more--menu__contain">
    <i
      ref="moreList"
      class="material-icons more--menu__contain__btn"
      @click="showMoreMenu = !showMoreMenu"
    >arrow_drop_down</i>
    <transition name="fade">
      <div v-if="showMoreMenu">
        <ul class="more--list__menu">
          <li>
            <nuxt-link to="/profile">
              <button class="more-list__menu__btn">
                Profile
              </button>
            </nuxt-link>
          </li>
          <li>
            <nuxt-link to="/about">
              <button class="more-list__menu__btn">
                About
              </button>
            </nuxt-link>
          </li>
          <li>
            <nuxt-link to="/settings">
              <button class="more-list__menu__btn">
                Settings
              </button>
            </nuxt-link>
          </li>
        </ul>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  components: {},
  data () {
    return {
      showMoreMenu: false,
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
      // if we click outside element, hide menu
      const el = this.$refs.moreList;
      const { target } = e;
      if (el !== target && !el.contains(target)) {
        if (this.showMoreMenu) {
          this.showMoreMenu = false;
        }
      }
    },
    signOff (e) {
      console.log('SIGNING OFF HERE');
      // redirect to home
    },
  },
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
  color: var(--primary-purple);
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
