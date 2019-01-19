<template>
  <div class="menu-options">
    <ul>
      <li><nuxt-link to="/" class="menubtn">Feed</nuxt-link></li>
      <li><nuxt-link to="/discover" class="menubtn">Discover</nuxt-link></li>
      <li><nuxt-link to="/jbrlly" class="menubtn">Profile</nuxt-link></li>
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
  border-bottom: 0.5px solid rgba(0, 0, 0, 0.4);
}
ul li {
  display: inline;
  font-size: 2rem;
  margin-left: 1em;
}
.menubtn {
  color: black;
}
.menubtn:hover {
  cursor: pointer;
  color: #c0102c;
  border-bottom: 2px solid #c0102c;
}
</style>
