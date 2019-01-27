<template>
  <div class="menu-options">
    <ul>
      <li><nuxt-link to="/" class="menubtn">Feed</nuxt-link></li>
      <li><nuxt-link to="/discover" class="menubtn">Discover</nuxt-link></li>
      <li><nuxt-link to="/lists" class="menubtn">Lists</nuxt-link></li>
    </ul>
  </div>
</template>

<script>
export default {
  components: {},
  name: "menuoptions"
};
</script>

<style scoped>
.menu-options {
  display: inline-block;
}
ul {
  margin-left: 0;
  float: left;
  width: 40%;
  padding-bottom: 10px;
  min-width: 500px;
  border-bottom: 0.5px solid var(--red-accent);
}
ul li {
  display: inline;
  font-size: 1.5rem;
  margin-left: 1em;
}
.menubtn {
  color: white;
}
.menubtn:hover {
  cursor: pointer;
  color: var(--primary-yellow);
  border-bottom: 2px solid var(--primary-yellow);
}
</style>
