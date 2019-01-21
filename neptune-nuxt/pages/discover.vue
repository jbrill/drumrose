<template>
  <div>
    <div v-if="isAuthenticated" class="loggedInContent"><post-feed /></div>
    <div v-else><div class="topExtension">LISTEN TO MUSIC</div></div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import ProfileNav from "~/components/ProfileNav";
import MenuOptions from "~/components/MenuOptions";
import PostFeed from "~/components/PostFeed";
import AddPostButton from "~/components/AddPostButton";
import TopBody from "~/components/TopBody";

export default {
  computed: mapGetters(["isAuthenticated", "loggedUser"]),
  components: {
    ProfileNav,
    MenuOptions,
    PostFeed,
    AddPostButton,
    TopBody
  },
  methods: {}
};
</script>

<style scoped>
.content {
  max-width: 90%;
  margin: 0 auto;
  margin-top: 8rem;
  text-align: center;
}
.topBodyContain {
  width: 100%;
  height: 40px;
}
.menuContain {
  width: 80%;
  float: left;
}
.profileContain {
  margin-top: -2rem;
  margin-right: 5%;
  float: right;
}
.feedContain {
  margin-bottom: 10%;
  margin-top: 5%;
}
.topExtension {
  position: absolute;
  width: 100%;
  height: 90%;
  top: 0;
  background-color: #b7205a;
}
.search-box {
  flex: 1;

  padding: 0;
  border: 0;
  border-bottom: 1px solid rgba(#000, 0.3);
  transition: border 0.2s ease;

  &:focus {
    outline: none;
    border-bottom-color: rgba(#000, 1);
  }
}

.searchContain {
}
</style>
