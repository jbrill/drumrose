<template>
  <div>
    <button class="showModal" @click="showModal = true">
      <i class="material-icons">album</i>
    </button>
    <!-- use the modal component, pass in the prop -->
    <AddPostModal v-if="showModal" @close="showModal = false" />
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import AddPostModal from "~/components/AddPostModal.vue";

export default {
  data: function() {
    return {
      showModal: false
    };
  },
  components: {
    AddPostModal
  }
};
</script>

<style scoped>
.showModal {
  background-color: black;
  color: white;
  height: 2.5rem;
  width: 6rem;
  position: absolute;
  right: 3rem;
  font-size: 1.5rem;
  text-align: center;
}
.showModal i {
  box-shadow: 0px 13px 21px -10px rgba(0, 0, 0, 0.3);
}
.showModal:hover {
  cursor: pointer;
}
</style>
