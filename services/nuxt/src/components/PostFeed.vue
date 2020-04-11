<template>
  <div class="post--feed">
    <post v-for="post in posts" :key="post.id" :post="post" />
  </div>
</template>

<script>
import Post from '~/components/Post.vue';

export default {
  components: {
    Post,
  },
  props: ['posts'],
  created () {},
};
</script>
<style scoped>
.post--feed {
  display: grid;
  grid-template-columns: 50% 50%;
  row-gap: 4rem;
}
</style>
