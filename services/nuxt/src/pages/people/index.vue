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
                  class="font-weight-bold"
                  style="color: var(--primary-yellow)"
                >
                  {{ user.username }}
                </nuxt-link>
              </v-list-item-title>
              <v-list-item-subtitle class="text--secondary">
                {{ user.followers.length }} Followers
              </v-list-item-subtitle>
            </v-list-item-content>

            <v-list-item-action>
              <v-list-item-action-text>
                {{ user.id }}
                Member since {{ user.created_date.split('-')[0] }}
              </v-list-item-action-text>
              <v-icon
                v-if="!(following.includes(user.id))"
                color="grey lighten-1"
                small
                @click="followPerson(user.username)"
              >
                person_add_alt_1
              </v-icon>

              <v-icon
                v-else
                color="yellow lighten-3"
                small
                @click="followPerson(user.username)"
              >
                person_add_minus
              </v-icon>
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
      } catch (err) {
        console.error(err);
        this.$toast.show(`Log in to follow ${username}`);
      }
    },
  },
};
</script>

<style scoped></style>
