<template>
  <v-expansion-panels>
    <v-expansion-panel>
      <v-expansion-panel-header>
        <v-row no-gutters>
          <v-col cols="8">
            Your Review
          </v-col>
          <v-col
            style="padding-top: 1rem;"
            cols="8"
            class="text--secondary"
          >
            <v-fade-transition leave-absolute>
              <v-rating
                v-model="rating"
                background-color="white"
                color="var(--primary-purple)"
                dense
                half-increments
                hover
                size="16"
                @click.native.stop.prevent
              />
            </v-fade-transition>
          </v-col>
        </v-row>
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        <v-textarea
          v-model="textValue"
          counter
          label="Add Review"
          :rules="rules"
          auto-grow
          outlined
          filled
          rows="2"
          row-height="20"
        />
        <v-btn
          :disabled="!auth.loggedIn || (rating === 0 && textValue.length === 0)"
          color="var(--primary-purple)"
          @click="submitReview"
        >
          Add Review
        </v-btn>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>
import { mapState } from 'vuex';
import { postReview } from '~/api/api';

export default {
  data: () => ({
    rating: 0,
    rules: [v => v.length <= 255 || 'Max 255 characters'],
    textValue: '',
  }),
  computed: {
    ...mapState(['auth', 'isAuthorized']),
  },
  methods: {
    async submitReview () {
      console.log(this.$auth.getToken('auth0'))
      await postReview(
        this.$auth.getToken('auth0'),
        { 'type': 'album', 'review': 'test', 'rating': 0.0 }
      );
    },
  },
};
</script>

<style scoped>
</style>