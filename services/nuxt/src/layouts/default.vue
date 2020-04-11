<template>
  <div class="app">
    <navbar /> <nuxt />
  </div>
</template>

<script>
import Navbar from '~/components/Navbar';

export default {
  components: {
    Navbar,
  },
};
</script>

<style>
.app {
  font-family: Menlo, Monaco, 'Droid Sans Mono', Consolas, 'Lucida Console',
    'Courier New', monospace;
  margin: 0 auto;
  background-color: #f6f6f6;
}
</style>
