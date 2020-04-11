<template>
  <div class="top--body"><menuOptions /></div>
</template>

<script>
import MenuOptions from '~/components/MenuOptions';
import AddPostButton from '~/components/AddPostButton';

export default {
  components: {
    MenuOptions,
    AddPostButton
  }
}
</script>

<style scoped>
.top--body {
  height: 100%;
  display: inline-block;
  margin-top: 7rem;
}
</style>
