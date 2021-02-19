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
            <a
              :href="'/people/' + user.username"
              style="color: var(--primary-yellow)"
            >
              {{ user.username }}
            </a>
          </v-list-item-title>
          <v-list-item-subtitle class="text--primary">
            {{ user.followers.length }} Followers
          </v-list-item-subtitle>
        </v-list-item-content>

        <v-list-item-action>
          <v-list-item-action-text>
            Member since 2009
          </v-list-item-action-text>
          <v-icon
            v-if="!active"
            color="grey lighten-1"
            @click="followPerson"
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
import { getUserList } from '~/api/api';

export default {
  async asyncData ({ store, $auth }) {
    const usersResponse = await getUserList();
    console.log(usersResponse)
    return {
      "users": usersResponse.data.users,
    };
  },
  methods: {
    followPerson () {
      console.log("SHOULD FOLLOW");
    },
  }
};
</script>

<style scoped></style>
