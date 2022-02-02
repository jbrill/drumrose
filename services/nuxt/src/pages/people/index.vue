<template>
  <div class="profileContain">
    <p style="text-align: center">
      Artists, fans, lovers — find passionate music afficianados!
    </p>
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
          <v-list-item-subtitle class="text--primary">
            {{ user.followers.length }} Followers
          </v-list-item-subtitle>
        </v-list-item-content>

        <v-list-item-action>
          <v-list-item-action-text>
            Member since {{ user.created_date.split('-')[0] }}
          </v-list-item-action-text>
          <v-icon
            v-if="!active"
            color="grey lighten-1"
            @click="followPerson(user.username)"
          >
            person_add_alt_1
          </v-icon>

          <v-icon
            v-else
            color="yellow"
          >
            star
          </v-icon>
        </v-list-item-action>
      </v-list-item>

      <v-divider
        v-if="index + 1 < users.length"
        :key="index"
      />
    </v-list>
  </div>
</template>

<script>
import { getUserList, patchUserDetail } from '~/api/api';

export default {
  async asyncData ({ store, $auth }) {
    const usersResponse = await getUserList();
    console.log(usersResponse.data.users);
    return {
      "users": usersResponse.data.users,
    };
  },
  methods: {
    async followPerson (username) {
      try {
        patchUserDetail(
          this.$auth.getToken('auth0'),
          this.$auth.user['https://django-server:8000/handle'],
          {
            "user_handle": username,
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
