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
            <v-list-item-title
              class="overline font-weight-bold"
              v-text="link"
            />
          </v-list-item>
        </v-list>
      </v-card>
    </v-navigation-drawer>
    <v-flex>
      <v-container>
        <h2 class="font-weight-bold header-1">
          About
        </h2>
        <v-divider />
        <v-spacer />
        <p class="header-2 font-weight-bold yellow--text">
          What is Drumrose?
        </p>
        <p>
          {{ drumroseDescription }}
        </p>
      </v-container>
      <v-container>
        <p class="header-2 font-weight-bold yellow--text">
          Why do we exist?
        </p>
        <p>
          {{ drumrosePurpose }}
        </p>
      </v-container>
    </v-flex>
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
      drumroseDescription: "Drumrose is an open, contextual catalog " +
        "set to advance the discussion and discourse of the musicverse.",
      drumrosePurpose: "We believe current models of music facilitation " +
        "are too centralized.",
    };
  },
};
</script>

<style scoped>
</style>
