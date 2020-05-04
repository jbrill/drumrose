<template>
  <div>
    <b-btn v-b-modal.addPostModal class="add-post-button">
      New Tune
    </b-btn>
    <b-modal id="addPostModal" title="Add a post" hide-footer>
      <form method="POST" @submit="onSubmitForm">
        <div class="form-group">
          <label for="tune"> Tune </label>
          <input
            type="text"
            name="tune"
            class="form-control"
            @input="onTuneChange"
          >
          <ul id="autocomplete-results" class="autocomplete-results">
            <li
              v-for="(hint, i) in track_query_hints"
              :key="i"
              class="autocomplete-result"
              @click="togglePick(hint)"
            >
              {{ hint.attributes.name }} <br>
              {{ hint.attributes.artistName }}
            </li>
          </ul>
        </div>
        <div class="form-group">
          <label for="caption"> Caption </label>
          <input
            type="text"
            name="caption"
            class="form-control"
            @input="onCaptionChange"
          >
        </div>

        <div v-if="!submitted" class="form-group">
          <b-button
            type="submit"
            class="btn btn-default"
            :disabled="errors"
            variant="primary"
            @click="show = false"
          >
            Add Post
          </b-button>
        </div>
        <div v-if="submitted" class="alert alert-success">
          Thanks!
        </div>
      </form>
    </b-modal>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import {
  getTrackIDFromQuery,
  getTrackHintsFromQuery,
  createPost,
} from '~/utils/post_util';

export default {
  components: {},
  props: {
    items: {
      type: Array,
      required: false,
      default: () => [],
    },
  },
  data: function () {
    return {
      addPostModal: false,
      submitted: false,
      track_query_hints: [],
      errors: false,
      track_id_choice: null,
      caption: null,
    };
  },
  methods: {
    onSubmitForm: async function (e) {
      if (!process.client) {
        return;
      }
      await createPost(
        window.localStorage.api_token,
        this.track_id_choice,
        this.caption,
        this.$store.state.user_handle
      );
      this.submitted = true;
    },
    onTuneChange: async function (e) {
      const searchQuery = e.target.value;
      const resp = await getTrackHintsFromQuery(
        searchQuery,
        this.$store.state.appleMusicToken
      );
      console.log(resp);
      this.track_query_hints = resp;
    },
    onCaptionChange: function (e) {
      const caption = e.target.value;
      this.caption = caption;
    },
    togglePick: function (appleTrackResult) {
      this.track_id_choice = appleTrackResult.id;
    },
  },
};
</script>

<style scoped>
.add-post-button {
  margin-right: 2rem;
  border: none;
  border-radius: 5px;
  background-color: black; 
  box-shadow: var(--shadow-heavy);  
  top: 5rem;
  width: 7rem;
  line-height: 1.5rem;
  color: white;
}

.add-post-button:hover, .add-post-button:focus {
  opacity: 0.9 !important;
}

.autocomplete-results {
  color: grey;
  list-style-type: none;
  padding-left: 1rem;
  margin-top: 1em;
}
@media screen and (prefers-color-scheme: dark) {
  .autocomplete-results {
    color: white;
  }
}

.autocomplete-result {
  height: 100%;
}

.autocomplete-result:hover, .autocomplete-result:focus {
  background-color: #f2f2f2;
  cursor: pointer;
}
</style>
