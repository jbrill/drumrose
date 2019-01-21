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
  border-radius: 0.5rem;
  background-color: #1e1b1a;
  font-size: 0.8rem;
  color: white;
  border: none;
  padding-left: 2rem;
}

.search-bar__input:focus {
  /* outline: none !important; */
  /* border: 1px solid var(--primary-purple); */
  box-shadow: 0 0 10px #719ece;
}

::placeholder {
  color: var(--primary-red);
  /* font-weight: lighter; */
  font-family: "Proxima Nova", "Helvetica Neue", Helvetica, Arial, sans-serif;
}
</style>
