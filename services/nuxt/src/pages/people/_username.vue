<template>
  <div class="profileContain">
    <v-img />
    <p class="profileName">
      {{ profile.username }}
    </p>
    <div class="postsContain">
      POSTS GO HERE...
    </div>
    <v-btn flat depressed elevation="2">{{profile.followers.length}} followers</v-btn>
    <v-divider vertical style="{color: white}"></v-divider>
    <v-btn>{{profile.following.length}} following</v-btn>
    <v-btn>{{profile.following.length}} playlists</v-btn>
    <v-btn>{{profile.following.length}} reviews</v-btn>
    <v-btn>{{profile.following.length}} ratings</v-btn>
  </div>
</template>

<script>
import {
  getUserDetail, getUserList, addFollower,
} from '~/api/api';

export default {
  async asyncData ({ store, route, $auth }) {
    let userResponse;

    if ($auth.loggedIn) {
      userResponse = await getUserDetail(
        $auth.getToken('auth0'),
        route.params.username,
      );
    }
    if (!userResponse ) {
      return { "profile": null };
    }
    return {
      "profile": userResponse.data,
    };
  },
};
</script>

<style scoped></style>
