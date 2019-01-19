<template>
  <div>
    <div class="profileContain">
      <h1>Jason Brill</h1>
      <img class="userAvatar" />
      <div class="userPosts">USER POSTS</div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import TopBody from "~/components/TopBody";

export default {
  name: "user-profile",
  components: {
    TopBody
  },
  computed: mapGetters(["isAuthenticated", "loggedUser"]),
  async asyncData({ app }) {
    const user = await app.$axios.$get(`http://localhost:8000/users/`);
    console.log(user);
    return { user };
  }
};
</script>

<style scoped>
.profileContain {
  width: 80%;
  margin: 0 auto;
}
</style>
