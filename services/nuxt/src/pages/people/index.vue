<template>
  <div class="profileContain">
    <p>
      Find more music lovers here.
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
