<template>
  <div class="header">
    <nuxt-link to="/" color="var(--primary-yellow)" class="title-button">
      DRUMROSE
    </nuxt-link>
    <v-btn @click="login" v-if="!auth.loggedIn">Log In</v-btn>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  computed: {
    ...mapState(['auth']),
  },
  methods: {
    login () {
      this.$auth.loginWith('auth0')
    },
    async signOut () {
      await this.$auth.logout();
      if (process.client) {
        const AUTH0_DOMAIN = 'drumrose.auth0.com';
        const AUTH0_CLIENT_ID = 'nA1RUMeTG88LVxGeEJc9Xu4PhWPHQRTg';
        console.log(AUTH0_DOMAIN)
        window.location.href = `https://${AUTH0_DOMAIN}/v2/logout?returnTo=https%3A%2F%2Fteton.drumrose.io&client_id=${AUTH0_CLIENT_ID}`
      }
    },
  },
};
</script>

<style>
.header {
  padding-top: 4rem;
  padding-left: 2rem;
  min-height: 3rem;
  display: flex;
	align-items: center;
	font-size: 3rem;
	z-index: 10;
	height: 2rem;
  font-family: 'Helvetica', sans-serif;
  font-weight: bolder;
}
.audio-contain {
  display: flex;
  justify-content: center;
  margin: 0 auto;
  width: 100%;
}
.title-button {
  font-size: 1.5rem;
  letter-spacing: 0.5rem;
}
.profile-menu-icon {
  height: 100%;
}
@media screen and (prefers-color-scheme: dark) {
  .header {
    background-color: transparent;
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
