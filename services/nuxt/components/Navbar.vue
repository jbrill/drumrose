<template>
  <div class="header">
    <nuxt-link class="title__middle" to="/" exact>DRUMROSE</nuxt-link>
    <div class="search-bar__contain"><search-bar /></div>
    <signIn v-if="!isAuthenticated" />
    <AddPostButton v-else />
    <div class="stateLinks">
      <div class="nav-bar__right--actions"><moreList /></div>
    </div>
  </div>
</template>

<script>
import { store } from "~/plugins/localStorage";
import MoreList from "~/components/Navbar/MoreList";
import SearchBar from "~/components/SearchBar";
import NeptuneLogo from "~/assets/svg/logo.svg";
import SignIn from "~/components/partials/sign-in";
import AddPostButton from "~/components/AddPostButton";

export default {
  components: {
    MoreList,
    SearchBar,
    NeptuneLogo,
    SignIn,
    AddPostButton
  },
  computed: {
    isAuthenticated: function() {
      return store.getters.isAuthenticated;
    }
  }
};
</script>

<style>
.header {
  position: fixed;
  z-index: 10000;
  background-color: var(--primary-black-light);
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
.title__middle:hover {
  color: var(--primary-purple);
}
.title__middle {
  letter-spacing: 2px;
  font-size: 2em;
  color: var(--primary-red);
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
  opacity: 0.9;
  margin-right: 1rem;
}
.search-bar__contain:hover {
  color: black;
  opacity: 1;
  transition: opacity 0.2s ease-out;
  -moz-transition: opacity 0.2s ease-out;
  -webkit-transition: opacity 0.2s ease-out;
  -o-transition: opacity 0.2s ease-out;
}
</style>
