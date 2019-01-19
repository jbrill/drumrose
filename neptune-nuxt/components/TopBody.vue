<template>
  <div class="top--body"><menuOptions /> <searchBar /></div>
</template>

<script>
import MenuOptions from "~/components/MenuOptions";
import SearchBar from "~/components/SearchBar";

export default {
  components: {
    MenuOptions,
    SearchBar
  }
};
</script>

<style scoped>
.top--body {
  height: 100%;
  display: inline-block;
  margin-top: 6rem;
}

.search-bar {
  position: absolute;
  right: 4rem;
  top: 6rem;
}
</style>
