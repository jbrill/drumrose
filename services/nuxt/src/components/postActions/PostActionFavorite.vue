<template>
  <div class="PostActionFavoriteContain">
    <i class="postActionFavorite material-icons">favorite_border</i>
  </div>
</template>

<script>
export default {
  name: 'PostActionFavorite',
};
</script>

<style scoped>
.postActionFavorite:hover {
  color: #be002e;
}
.PostActionFavoriteContain {
  float: right;
  color: white;
  padding-left: 1rem;
}
</style>
