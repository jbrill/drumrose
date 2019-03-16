<template>
  <div>
    <b-btn class="neptune-button__strong" v-b-modal.addPostModal
      >New Tune</b-btn
    >
    <b-modal id="addPostModal" title="Add a post" hide-footer>
      <form method="POST" @submit="onSubmitForm">
        <div class="form-group">
          <label for="tune"> Tune </label>
          <input
            type="text"
            name="tune"
            @input="onTuneChange"
            class="form-control"
          />
          <ul id="autocomplete-results" class="autocomplete-results">
            <li
              v-for="(hint, i) in track_query_hints"
              :key="i"
              @click="togglePick(hint)"
              class="autocomplete-result"
            >
              {{ hint.attributes.name }} - {{ hint.attributes.artistName }}
            </li>
          </ul>
        </div>
        <div class="form-group">
          <label for="caption"> Caption </label>
          <input
            type="text"
            name="caption"
            @input="onCaptionChange"
            class="form-control"
          />
        </div>

        <div class="form-group" v-if="!submitted">
          <b-button
            @click="show = false"
            type="submit"
            class="btn btn-default"
            v-bind:disabled="errors"
            variant="primary"
          >
            Add Post
          </b-button>
        </div>
        <div class="alert alert-success" v-if="submitted">Thanks!</div>
      </form>
    </b-modal>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import {
  getTrackIDFromQuery,
  getTrackHintsFromQuery,
  createPost
} from "~/utils/post_util";

export default {
  components: {},
  methods: {
    onSubmitForm: async function(e) {
      event.preventDefault();
      console.log("SUBMITTING FORM");
      await createPost(
        this.$store.state.api_token,
        this.track_id_choice,
        this.caption,
        this.$store.state.user_handle
      );
      this.submitted = true;
    },
    onTuneChange: async function(e) {
      const search_query = e.target.value;
      const resp = await getTrackHintsFromQuery(
        search_query,
        this.$store.state.music_token
      );
      console.log(resp);
      this.track_query_hints = resp;
    },
    onCaptionChange: async function(e) {
      const caption = e.target.value;
      this.caption = caption;
    },
    togglePick: function(apple_track_result) {
      this.track_id_choice = apple_track_result.id;
    }
  },
  props: {
    items: {
      type: Array,
      required: false,
      default: () => []
    }
  },
  data: function() {
    return {
      addPostModal: false,
      submitted: false,
      track_query_hints: [],
      errors: false,
      track_id_choice: null,
      caption: null
    };
  }
};
</script>

<style scoped>
.neptune-button__strong {
  position: absolute;
  right: 15%;
  top: 7rem;
  width: 7rem;
  line-height: 2rem;
}

.autocomplete-results {
  color: grey;
  list-style-type: none;
  padding-left: 1rem;
  margin-top: 1em;
}

.autocomplete-result {
  height: 2rem;
}

.autocomplete-result:hover {
  background-color: #f2f2f2;
  cursor: pointer;
}
</style>
