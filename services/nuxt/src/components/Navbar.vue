<template>
  <div class="header">
    <v-btn to="/" primary text nuxt color="var(--primary-yellow)" ripple x-large class="title-button">
      DRUMROSE
    </v-btn>
    <div class="navigation-contain">
      <v-btn color="#ccc" text nuxt to="/">FEED</v-btn>
      <v-btn color="#ccc" text nuxt to="/playlists">PLAYLISTS</v-btn>
      <v-btn color="#ccc" text nuxt to="/library">LIBRARY</v-btn>
    </div>
    <div class="search-bar__contain">
      <SearchBar />
    </div>
    <!---<AddPostButton />-->
    <MoreList />
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
  z-index: 1000;
  background-color: var(--primary-black-light);
  left: 0;
  display: flex;
  align-items: center;
  width: 100%;
  min-height: 4rem;
  box-shadow: var(--shadow-heavy);
}
.navigation-contain {
  display: flex;
  justify-content: flex-end;
  margin: 0 auto;
  width: 100%;
  padding-right: 1rem;
}
.title-button span {
  font-weight: bolder;
  font-size: larger;
}
@media screen and (prefers-color-scheme: dark) {
  .header {
    background-color: black;
  }
  .title__middle {
    color: var(--primary-red);
  }
  .title__middle:hover, .title__middle:focus {
    color: white;
  }
  .search-bar__contain:hover, .search-bar__contain:focus {
    color: ghostwhite;
  }
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
.title__middle {
  letter-spacing: 2px;
  font-size: 1.5rem;
  color: ghostwhite;
  font-weight: bolder;
  margin: 0 auto;
  margin-left: 3rem;
}
.title__middle:hover, .title__middle:focus {
  color: var(--primary-red);
}
a {
  text-decoration: none;
}
.registerLink {
  padding-right: 2%;
}

.nav-bar__right--actions .moreListContain {
  float: right;
}
.search-bar__contain {
  margin: 0 auto;
  opacity: 0.9;
  margin-right: 1.2rem;
}
@media screen and (prefers-reduced-motion: reduce) {
  .search-bar__contain:hover, .search-bar__contain:focus {
    color: black;
    opacity: 1;
    transition: none;
  }
}
.search-bar__contain:hover, .search-bar__contain:focus {
  color: black;
  opacity: 1;
  transition: opacity 0.2s ease-out;
}
</style>
