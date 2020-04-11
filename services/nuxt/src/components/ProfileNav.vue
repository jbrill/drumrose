<template>
  <nuxt-link class="profile--link" to="/profile">
    <div class="profile--link__contain">
      <img
        class="profile--link__contain__img"
        src="https://avatars1.githubusercontent.com/u/\
          1837026?s=400&u=95442a7c7332e8d25cd4eafeae3753ce593dc441&v=4"
      >
      <p>{{ loggedUser ? loggedUser.nickname : 'friend' }}</p>
    </div>
  </nuxt-link>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  computed: mapGetters(['isAuthenticated', 'loggedUser']),
};
</script>

<style scoped>
.profile--link__contain {
  /* text-align: center; */
  /* padding: 2px; */
  /* width: 110%; */
  /* height: 110%; */
  width: 1em;
  height: auto;
  float: left;
}
.profile--link__contain:hover {
  background-color: rgba(255, 255, 255, 0.3);
  box-shadow: 0rem 2rem 3rem -2rem rgba(0, 0, 0, 0.3);
  border: 1px solid grey;
  cursor: pointer;
  border-radius: 4px;
}
.profile--link__contain__img {
  border-radius: 50%;
  width: 3rem;
}
</style>
