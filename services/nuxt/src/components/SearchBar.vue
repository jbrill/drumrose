<template>
  <div class="search-bar">
    <input
      onfocus="this.placeholder = ''"
      onblur="this.placeholder = 'Search for music...'"
      placeholder="Search for music..."
      class="search-bar__input"
    >
  </div>
</template>

<script>
export default {
  components: {},
};
</script>

<style scoped>
@media screen and (prefers-color-scheme: dark) {
  .search-bar__input {
    color: white;
    background-color: grey;
  }
}
.search-bar__input {
  width: 18rem;
  height: 2rem;
  background-image: url('~assets/search.png');
  background-repeat: no-repeat;
  background-position: left;
  background-position-x: 0.5rem;
  background-size: 1rem 1rem;
  border-radius: 0.2rem;
  border: 1px solid var(--primary-black--light);
  background-color: white;
  font-size: 0.8rem;
  color: black;
  padding-left: 2.5rem;
}

.search-bar__input:focus {
  outline: none !important;
  border: 1px solid var(--primary-purple);
  box-shadow: 0 0 10px #719ece;
  opacity: 1;
}

::placeholder {
  color: var(--primary-black--light);
  font-weight: 300;
  font-family: 'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif;
}
</style>
