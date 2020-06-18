<template>


</template>

<script>
export default {
  mounted() {
    if (this.$route.hash) {
      console.log("ROUTE HASH...")
      console.log(this.$route.hash)
      this.$auth.setToken(
        'auth0',
        `Bearer ${this.$route.hash.split('=')[1].split('&')[0]}`
      )
    }
    // fetch user information from token
    console.log(this.$auth.getToken('auth0'))
    console.log(this.$route.path)
    // schedule a redirect depending on authentication results
  }
}
</script>

<style>

</style>
