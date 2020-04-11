<template>
  <div class="top--body">
    <menuOptions />
  </div>
</template>

<script>
import MenuOptions from '~/components/MenuOptions';

export default {
  components: {
    MenuOptions,
  },
};
</script>

<style scoped>
.top--body {
  height: 100%;
  display: inline-block;
  margin-top: 7rem;
}
</style>
