<template>
  <v-menu
    z-index="100"
    allow-overflow
    absolute
    transition="scale-transition"
  >
    <template v-slot:activator="{ on }">
      <v-btn
        icon
        dark
        v-on="on"
        @click="menu = true"
      >
        <v-icon small color="white" class="album-overlay-more">
          mdi-dots-horizontal
        </v-icon>
      </v-btn>
    </template>
    <v-list>
      <v-list-item>test</v-list-item>
    </v-list>
  </v-menu>
</template>

<script>
export default {
  props: {
    id: {
      type: String,
      default: '',
    },
  },
  data () {
    return {
      playlistDialog: false,
      menu: false,
    };
  },
  watch: {
    isClicked: function () {
      if(this.menu){
        document.documentElement.style.overflow = 'hidden';
        return;
      }

      document.documentElement.style.overflow = 'auto';
    }, 
  },
  methods: {
    addToQueue: function () {
      this.$store.dispatch("setQueue", { "playlist": this.id });
    },
    addToLibrary: function () {
      this.$store.dispatch("addToLibrary", { 'playlist': this.id });
    },
  },
};
</script>

<style scoped>
</style>
