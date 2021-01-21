<template>
  <div class="profileContain">
    <p style="text-align: center">
      Find friends passionate about music
    </p>
    <v-list two-line>
      <v-list-item-group
        multiple
      >
        <v-list-item
          v-for="(item) in users"
          :key="item.username"
        >
          <v-list-item-content>
            <v-list-item-title
              nuxt
              :to="'/people/' + item.username"
              v-text="item.username"
            />
            <v-list-item-subtitle
              class="text--primary"
              v-text="item.username"
            />
            <v-list-item-subtitle 
              v-text="item.username"
            />
          </v-list-item-content>

          <v-list-item-action>
            <v-list-item-action-text
              v-text="item.username"
            />
            <v-icon
              v-if="!active"
              color="grey lighten-1"
            >
              star_border
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
      </v-list-item-group>
    </v-list>
  </div>
</template>

<script>
import { getUserList } from '~/api/api';

export default {
  async asyncData ({ store, $auth }) {
    const usersResponse = await getUserList();
    return {
      "users": usersResponse.data.users,
    };
  },
};
</script>

<style scoped></style>
