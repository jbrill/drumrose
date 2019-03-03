<template>
  <div class="sign--in__contain">
    <b-btn @click="onSubmitForm" class="neptune-button__strong">Sign Out</b-btn>
  </div>
</template>

<script>
import { getBaseUrl } from "~/utils/lock";
import auth0 from "auth0-js";
import config from "~/config.json";

export default {
  middleware: "anonymous",
  methods: {
    onSubmitForm: function(e) {
      console.log("SHOULD SIGN OFF HERE...");
    }
  },
  data() {
    return {
      modalShow: false
    };
  }
};
</script>
<style scoped>
.neptune-button__strong {
  font-size: 0.8rem;
}
</style>
