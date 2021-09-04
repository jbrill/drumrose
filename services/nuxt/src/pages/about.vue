<template>
  <v-layout>
    <v-navigation-drawer>
      <v-card>
        <v-list elevation="12" color="transparent" class="grow">
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
        <h2
          class="font-weight-bold header-1"
          :style="{'color': 'var(--primary-yellow)'}"
        >
          About
        </h2>
        <v-divider />
        <v-spacer />
        <p class="header-2 font-weight-bold white--text">
          What is Drumrose?
        </p>
        <p>
          {{ drumroseDescription }}
        </p>
        <p class="header-2 font-weight-bold white--text">
          Why do we exist?
        </p>
        <p>
          {{ drumrosePurpose }}
        </p>
      </v-container>
      <v-container>
        <h2
          class="font-weight-bold header-1"
          :style="{'color': 'var(--primary-yellow)'}"
        >
          Data
        </h2>
        <v-divider />
        <v-spacer />
        <p class="header-2 font-weight-bold white--text">
          Where do you get your data?
        </p>
        <p>
          bleh
        </p>
        <p class="header-2 font-weight-bold white--text">
          What do you do with my data?
        </p>
        <p>
          bleh
        </p>
      </v-container>
      <v-container>
        <h2
          class="font-weight-bold header-1"
          :style="{'color': 'var(--primary-yellow)'}"
        >
          Contact
        </h2>
        <v-divider />
        <v-spacer />
        <p class="header-2 font-weight-bold white--text">
          What is Drumrose?
        </p>
        <p>
          {{ drumroseDescription }}
        </p>
      </v-container>
      <v-container>
        <p class="header-2 font-weight-bold white--text">
          Why do we exist?
        </p>
        <p>
          {{ drumrosePurpose }}
        </p>
      </v-container>
      <v-container>
        <h2
          class="
            font-weight-bold header-1
          "
          :style="{'color': 'var(--primary-yellow)'}"
        >
          Legal
        </h2>
        <v-divider />
        <v-spacer />
        <p class="header-2 font-weight-bold white--text">
          What is Drumrose?
        </p>
        <p>
          {{ drumroseDescription }}
        </p>
      </v-container>
      <v-container>
        <p class="header-2 font-weight-bold white--text">
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
        'Data',
        'Contact',
        'Legal',
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
