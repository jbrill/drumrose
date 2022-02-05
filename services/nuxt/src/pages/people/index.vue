<template>
  <div class="profileContain">
    <p style="text-align: center">
      Artists, fans, lovers — find passionate music afficianados!
    </p>
    <v-responsive
      class="overflow-y-auto"
    >
      <v-lazy
        v-for="
          rowIdx in users.length
        "
        :key="rowIdx"
        :options="{
          threshold: .5
        }"
        min-height="400"
        transition="fade-transition"
      >
        <v-list two-line>
          <v-list-item
            v-for="(user) in users"
            :key="user.username"
          >
            <v-list-item-content>
              <v-list-item-title>
                <nuxt-link
                  :to="'/people/' + user.username"
                  class="font-weight-bold text--primary username"
                >
                  {{ user.username }}
                </nuxt-link>
              </v-list-item-title>
              <v-list-item-subtitle class="text--secondary overline">
                {{ user.track_reviews.length + user.playlist_reviews.length + user.album_reviews.length }} {{ "Reviews".toLowerCase() }} | {{ user.track_reviews.length + user.playlist_reviews.length + user.album_reviews.length }} {{ "Ratings".toLowerCase() }} | {{ user.track_reviews.length + user.playlist_reviews.length + user.album_reviews.length }} {{ "Reviews".toLowerCase() }} | {{ user.followers.length }} {{ "Followers".toLowerCase() }}
              </v-list-item-subtitle>
            </v-list-item-content>

            <v-list-item-action>
              <v-list-item-action-text>
                Member since {{ user.created_date.split('-')[0] }}
              </v-list-item-action-text>
              <v-btn
                v-if="!(following.includes(user.id))"
                small
                @click="followPerson(user.username)"
              >
                follow
              </v-btn>

              <v-btn
                v-else
                small
                @click="unFollowPerson(user.username)"
              >
                unfollow
              </v-btn>
            </v-list-item-action>
          </v-list-item>

          <v-divider
            v-if="index + 1 < users.length"
            :key="index"
          />
        </v-list>
      </v-lazy>
    </v-responsive>
  </div>
</template>

<script>
import {
  getUserDetail, getUserList, addFollower,
} from '~/api/api';

export default {
  async asyncData ({ store, $auth, $toast }) {
    let userResponse;
    let usersResponse;
    usersResponse = await getUserList();
    
    if ($auth.loggedIn) {
      userResponse = await getUserDetail(
        $auth.getToken('auth0'),
        $auth.user['https://django-server:8000/handle'],
      );
    }
    console.log(userResponse);
    if (!userResponse ) {
      return {
        "following": [],
        "users": usersResponse.data.users,
      };
    }
    console.log(userResponse.data.following)
    return {
      "following": userResponse.data.following,
      "users": usersResponse.data.users,
    };
  },
  methods: {
    async followPerson (username) {
      try {
        addFollower(
          this.$auth.getToken('auth0'),
          {
            "following_user": username,
          }
        );
        this.$toast.show(`Successfully followed ${username}`);
      } catch (err) {
        console.error(err);
        this.$toast.show(`Log in to follow ${username}`);
      }
    },
  },
};
</script>

<style scoped>
.username:hover, .username:focus {
  color: var(--primary-yellow) !important;
  font-weight: black;
}
</style>
