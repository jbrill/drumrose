<template>
  <div class="profileContain">
    <p style="text-align: center">
      Find friends passionate about music
    </p>
    <div class="peopleContain">
      {{ users }}
    </div>
  </div>
</template>

<script>
import { getUserList } from '~/api/api';

export default {
  async asyncData ({ store, $auth }) {
    const usersResponse = await getUserList();
    return {
      "users": usersResponse.data,
    };
  },
};
</script>

<style scoped></style>
