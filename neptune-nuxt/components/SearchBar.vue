<template>
  <div class="search-bar">
    <input placeholder="Search for music" class="search-bar__input" />
  </div>
</template>

<script>
export default {
  components: {}
};
</script>

<style scoped>
.search-bar__input {
  width: 20rem;
  height: 2rem;
  background-image: url("~assets/search.png");
  background-repeat: no-repeat;
  background-position: left;
  background-position-x: 0.5rem;
  background-size: 1rem 1rem;
  padding-left: 2rem;
}

.search-bar__input:focus {
  outline: none !important;
  border: 1px solid #c0102c;
  box-shadow: 0 0 10px #719ece;
}
</style>
