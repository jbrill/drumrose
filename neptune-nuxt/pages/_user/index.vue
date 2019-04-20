<template>
  <div class="profileContain">
    <img
      class="profileAvatar"
      src="https://avatars1.githubusercontent.com/u/1837026?s=400&u=95442a7c7332e8d25cd4eafeae3753ce593dc441&v=4"
    />
    <p class="profileName">Jason Brill</p>
    <div class="postsContain">POSTS GO HERE...</div>
  </div>
</template>

<script>
import { getUserDetail } from "~/api/neptune_api";

export default {
  async created() {
    console.log(params.user);
    const user = await getUserDetail(
      window.localStorage.api_token,
      params.user
    );
    console.log(user);
    return { user };
  }
};
</script>

<style scoped></style>
