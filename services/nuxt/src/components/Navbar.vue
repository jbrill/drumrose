<template>
  <div class="header">
    <nuxt-link class="title__middle" to="/" exact>
      DRUMROSE
    </nuxt-link>
    <div class="search-bar__contain">
      <SearchBar />
    </div>
    <AddPostButton />
    <div class="stateLinks">
      <div class="nav-bar__right--actions">
        <MoreList />
      </div>
    </div>
  </div>
</template>

<script>
import MoreList from '~/components/Navbar/MoreList';
import SearchBar from '~/components/SearchBar';
import AddPostButton from '~/components/AddPostButton';

export default {
  components: {
    MoreList,
    SearchBar,
    AddPostButton,
  },
};
</script>

<style>
.header {
  position: fixed;
  z-index: 0;
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
  color: var(--primary-red);
}
.title__middle {
  letter-spacing: 2px;
  font-size: 1.7rem;
  color: ghostwhite;
  font-weight: bolder;
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
