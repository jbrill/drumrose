<template>
  <div class="header">
    <nuxt-link to="/" color="var(--primary-red)" class="title-button">
      DRUMROSE
    </nuxt-link>
    <div class="navigation-contain">
      <v-btn color="#ccc" text nuxt to="/">SOCIAL</v-btn>
      <v-btn color="#ccc" text nuxt to="/discover">DISCOVER</v-btn>
      <v-btn color="#ccc" text nuxt to="/playlists">PLAYLISTS</v-btn>
      <v-btn color="#ccc" text nuxt to="/library">LIBRARY</v-btn>
    </div>
    <div style="text-align: center">
			<v-menu dark open-on-hover offset-y>
        <template v-slot:activator="{ on }">
          <v-btn
            tile
            dark
            class="profile-menu-button-contain"
            v-on="on"
          >
            jbrilly
						<v-icon
              style="height: 100%"
              right dark
							v-on="on"
						>
						 mdi-chevron-down
						</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item
            v-for="(item, index) in profileOptions"
            :key="index"
            @click=""
            :to="item.link"
          >
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </div>
    <div class="application-preferences">
      <v-menu dark offset-y>
        <template v-slot:activator="{ on }">
          <v-icon
            dark center
            v-on="on"
          >
           mdi-dots-horizontal 
          </v-icon>
        </template>
        <v-list>
          <v-list-item
            v-for="(item, index) in applicationOptions"
            :key="index"
            :to="item.link"
            @click=""
          >
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </div>
  </div>
</template>

<script>
export default {
  components: {
  },
  data: () => ({
    profileOptions: [
      { title: 'Profile', link: "/profile" },
      { title: 'Likes', link: "/likes" },
      { title: 'Playlists', link: "/playlists" },
      { title: 'Following', link: "/following" },
		],
    applicationOptions: [
      { title: 'About Us', links: "about" },
      { title: 'Terms', link: "terms" },
      { title: 'Contact', link: "/contact" },
      { title: 'Settings', link: "/settings" },
      { title: 'Sign Out' },
		],
	})
};
</script>

<style>
.header {
  position: fixed;
  z-index: 1000;
  background-color: var(--primary-black-light);
  left: 0;
  display: grid;
  grid-template-columns: 25% 50% 20% 5%;
  grid-template-rows: 100%;
  align-items: center;
  width: 100%;
  min-height: 4rem;
  box-shadow: var(--shadow-heavy);
}
.navigation-contain {
  display: flex;
  justify-content: center;
  margin: 0 auto;
  width: 100%;
}
.title-button {
  font-weight: bolder;
  color: var(--primary-red) !important;
  font-size: 1.5rem;
  padding-left: 1rem;
}
.profile-menu-icon {
  height: 100%;
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
