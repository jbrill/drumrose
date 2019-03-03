<template>
  <div>
    <b-btn class="neptune-button__strong" v-b-modal.addPostModal
      >New Tune</b-btn
    >
    <b-modal id="addPostModal" title="Add a post" hide-footer>
      <form method="POST" @submit="onSubmitForm">
        <div class="form-group">
          <label for="song"> Song </label>
          <input type="text" name="song" class="form-control" />
        </div>
        <div class="form-group">
          <label for="artist"> Artist </label>
          <input type="text" name="artist" class="form-control" />
        </div>
        <div class="form-group">
          <label for="caption"> Caption </label>
          <input type="text" name="caption" class="form-control" />
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
import { getTrackIDFromQuery } from "~/utils/post_util";

export default {
  components: {},
  methods: {
    onSubmitForm: function(e) {
      event.preventDefault();
      console.log("SUBMITTING FORM");
      getTrackIDFromQuery("testquery", this.$store.state.music_token);
      this.submitted = true;
    }
  },
  data: function() {
    return {
      addPostModal: false,
      submitted: false,
      errors: false
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
</style>
