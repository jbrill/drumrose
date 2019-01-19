<template>
  <div class="header">
    <nuxt-link class="title" to="/" exact>
      <img src="~/assets/logo.png" />
    </nuxt-link>
    <nuxt-link class="title_middle" to="/" exact>NEPTUNE</nuxt-link>
    <div class="stateLinks">
      <div class="nav-bar__right--actions"><moreList /></div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import MoreList from "~/components/Navbar/MoreList";

export default {
  components: {
    MoreList
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
  z-index: 100;
  background-color: #9c0235;
  top: 0;
  left: 0;
  display: flex;
  align-items: center;
  width: 100%;
  min-height: 4rem;
}
.header img {
  height: 3rem;
}
.title {
  margin-left: 2em;
  font-size: 1.4em;
}
.title:hover {
}
.title_middle {
  letter-spacing: 2px;
  font-size: 2.3em;
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
</style>
