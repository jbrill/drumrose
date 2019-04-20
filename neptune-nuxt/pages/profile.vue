<template>
  <div class="profile__contain">
    <h1>Jason Brill</h1>
    <img class="userAvatar" />
    <div class="userPosts">USER POSTS</div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import { getPosts } from "~/utils/post_util";

export default {
  name: "user-profile",
  components: {},
  computed: mapGetters(["isAuthenticated", "loggedUser"]),
  async created() {
    // Server cannot update localstorage
    if (process.server) return;
    const postResponse = await getPosts(window.localStorage.api_token);
  }
};
</script>

<style scoped></style>
