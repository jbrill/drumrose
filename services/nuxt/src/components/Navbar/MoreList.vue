<template>
  <div class="more--menu__contain">
    <div
      class="user-dropdown"
      ref="moreList"
      @click="showMoreMenu = !showMoreMenu"
    >
    <img class="user-avatar" src="https://upload.wikimedia.org/wikipedia/en/thumb/b/b2/PleasePleasePlease.jpg/220px-PleasePleasePlease.jpg" />
    <p class="user-handle">jbrilly</p>
    <i
      class="material-icons more--menu__contain__btn"
    >arrow_drop_down</i></div>
    <transition name="fade">
      <div v-if="showMoreMenu">
        <ul class="more--list__menu">
          <li>
            <nuxt-link to="/about">
              <button class="more-list__menu__btn">
                About Us
              </button>
            </nuxt-link>
          </li>
          <li>
            <nuxt-link to="/about">
              <button class="more-list__menu__btn">
                Legal
              </button>
            </nuxt-link>
          </li>
          <li>
            <nuxt-link to="/about">
              <button class="more-list__menu__btn">
                Copyright
              </button>
            </nuxt-link>
          </li>
          <li>
            <nuxt-link to="/about">
              <button class="more-list__menu__btn">
                Support
              </button>
            </nuxt-link>
          </li>
          <li>
            <nuxt-link to="/about">
              <button class="more-list__menu__btn">
                Keyboard Shortcuts
              </button>
            </nuxt-link>
          </li>
          <li>
            <nuxt-link to="/jbrlly">
              <button class="more-list__menu__btn">
                Profile
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
          <li>
            <nuxt-link to="/settings">
              <button class="more-list__menu__btn">
                Sign out
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
  height: 100%;
  display: flex;
  width: 100%;
  justify-content: flex-end;
  margin-right: 0.5rem;
  align-items: center;
}
.more--menu__contain__btn {
  font-size: 1.5rem;
  color: white;
  align-self: center;
}
@media screen and (prefers-color-scheme: dark) {
  .more--menu__contain__btn {
    color: white;
  }
  .more--menu__contain__btn:hover, .more--menu__contain__btn:focus {
    color: var(--primary-purple);
  }
  .more--list__menu {
    color: var(--primary-purple);
  }
  .more-list__menu__btn {
    color: var(--primary-purple);
  }
  .more-list__menu__btn:hover, .more-list__menu__btn:focus {
    color: var(--primary-red);
  }
}
.more--menu__contain__btn:hover, .more--menu__contain__btn:focus {
  color: var(--primary-purple);
}
@media screen and (prefers-reduced-motion: reduce) {
.fade-enter-active,
.fade-leave-active {
  transition: none;
}
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
  width: 8rem;
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
.more-list__menu__btn:hover, .more-list__menu__btn:focus {
  cursor: pointer;
  color: var(--primary-yellow);
  background-color: black;
}
.user-avatar {
  width: 2rem;
  height: auto;
  align-self: center;
  border-radius: 50%;
}
.user-dropdown {
  display: flex;
}
.user-dropdown:hover, .user-dropdown:focus {
  cursor: pointer;
}
</style>
