<template>
  <v-layout>
    <v-navigation-drawer>
      <v-card>
        <v-list shaped elevation="12" color="transparent" class="grow">
          <v-list-item
            v-for="link in links"
            :key="link"
            link
          >
            <v-list-item-title class="overline font-weight-bold" v-text="link" />
          </v-list-item>
        </v-list>
      </v-card>
    </v-navigation-drawer>
    <v-container>
      <h2 class="font-weight-bold header-1">
        About
      </h2>
      <v-divider />
      <p class="overline font-weight-bold yellow--text">
        What is Drumrose?
      </p>
      <p>
        Drumrose is an open, contextual catalog set to increase the discussion and discourse of the musicverse.
      </p>
    </v-container>
  </v-layout>
</template>

<script>
export default {
  data () {
    return {
      links: [
        'About',
        'Legal',
        'Data',
      ],
    }
  }
};
</script>

<style scoped>
</style>
