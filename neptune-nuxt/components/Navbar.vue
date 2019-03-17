<template>
  <div class="header">
    <nuxt-link class="title" to="/" exact>
      <NeptuneLogo class="title__img" />
    </nuxt-link>
    <nuxt-link class="title_middle" to="/" exact>NEPTUNE</nuxt-link>
    <div class="search-bar__contain"><search-bar /></div>
    <signIn v-if="!isAuthenticated" />
    <div class="stateLinks">
      <div class="nav-bar__right--actions"><moreList /></div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import MoreList from "~/components/Navbar/MoreList";
import SearchBar from "~/components/SearchBar";
import NeptuneLogo from "~/assets/svg/logo.svg";
import SignIn from "~/components/partials/sign-in";
import SignOut from "~/components/partials/sign-out";

export default {
  components: {
    MoreList,
    SearchBar,
    NeptuneLogo,
    SignIn,
    SignOut
  },
  computed: mapGetters(["isAuthenticated"]),
  methods: {
    logout: function(event) {
      // `this` inside methods points to the Vue instance
      alert("Hello " + this.name + "!");
      // `event` is the native DOM event
      if (event) {
        alert(event.target.tagName);
      }
    }
  }
};
</script>

<style scoped>
.header {
  position: fixed;
  z-index: 1000;
  background-color: #9c0235;
  left: 0;
  display: flex;
  align-items: center;
  width: 100%;
  min-height: 4rem;
  box-shadow: var(--shadow-heavy);
}
.header img {
  height: 3rem;
}
.title {
  margin-left: 2em;
  font-size: 1.4em;
}
.title__img {
  width: 3rem;
  height: auto;
  vertical-align: middle;
}
.title_middle {
  letter-spacing: 2px;
  font-size: 2em;
  color: white;
  font-weight: lighter;
  margin: 0 auto;
  margin-left: 3rem;
}
a {
  text-decoration: none;
}
.registerLink {
  padding-right: 2%;
}
.stateLinks {
  display: inline;
}
.nav-bar__right--actions {
  display: inline-block;
}
.nav-bar__right--actions .search-bar {
  float: left;
  margin-right: 6rem;
  margin-top: 0.3rem;
}

.nav-bar__right--actions .moreListContain {
  float: right;
}
.search-bar__contain {
  margin: 0 auto;
}
.sign--in__contain {
  margin-right: 1rem;
}
</style>
