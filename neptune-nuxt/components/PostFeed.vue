<template>
  <div class="post--feed">
    <post v-for="post in posts" v-bind:key="post.id" v-bind:post="post" />
  </div>
</template>

<script>
import Post from "~/components/Post.vue";

export default {
  components: {
    Post
  },
  props: ["posts"],
  created() {
    console.log("POST FEED COMPONENT CREATED");
  }
};
</script>
<style scoped>
.post--feed {
  margin-top: 5rem;
  display: grid;
  grid-template-columns: 50% 50%;
  row-gap: 4rem;
}
</style>
