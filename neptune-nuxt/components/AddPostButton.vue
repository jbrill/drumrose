<template>
  <div>
    <b-btn class="neptune-button__strong" v-b-modal.addPostModal
      >New Tune</b-btn
    >
    <!-- <i class="material-icons">album</i> -->
    <!-- use the modal component, pass in the prop -->
    <!-- <AddPostModal v-on:closed="showModal = false" v-if="showModal" /> -->
    <b-modal id="addPostModal" title="Add a post" hide-footer>
      <form method="POST" @submit="onSubmitForm">
        <div class="form-group">
          <label for="tune"> Tune </label>
          <input type="text" name="tune" class="form-control" />
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
import AddPostModal from "~/components/AddPostModal.vue";

export default {
  components: {
    AddPostModal
  },
  methods: {
    onSubmitForm: function(e) {
      event.preventDefault();
      console.log(e);
    }
  },
  data: function() {
    return {
      // showModal: false
      addPostModal: false
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
