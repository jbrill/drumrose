<template>
  <div class="profileContain">
    <p class="profileName">
      Jason Brill
    </p>
    <div class="postsContain">
      POSTS GO HERE...
      {{ followers }}
    </div>
  </div>
</template>

<script>
import { getFollowers } from '~/api/api'

export default {
  async asyncData({ store, $auth }) {
    if (store.auth && store.auth.loggedIn) {
      const followersResponse = await getFollowers(
        $auth.getToken('auth0')
      );
      return {
        "followers": followersResponse.data,
      };
    }
  }
}
</script>

<style scoped></style>
