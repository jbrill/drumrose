<template>
  <div>
    <v-autocomplete
      v-model="selectedSearch"
      background-color="var(--primary-black-light)"
      :items="entries"
      :loading="isLoading"
      :search-input.sync="search"
      clearable
      hide-details
      hide-selected
      hide-no-data
      dense
      item-text="attributes.name"
      item-value="attributes.name"
      no-data-text="No data found"
      placeholder="Search Drumrose"
      prepend-inner-icon="mdi-database-search"
      outlined
      return-object
      width="100%"
    >
      <v-btn
        v-if="search"
        slot="prepend-item"
        width="100%"
        text
        nuxt
        :to="'/search/' + search"
        class="search-button"
        color="var(--primary-yellow)"
      >
        Search for '{{ search }}'
      </v-btn>	
      <template v-slot:no-data>
        <v-list-item>
          <v-list-item-title>
            Find <strong>music</strong> and <strong>users</strong>
          </v-list-item-title>
        </v-list-item>
      </template>
      <template v-slot:item="{ item }">
        <v-list-item-avatar v-if="item.type === 'songs'">
          <img
            :src="appleImage(item)"
            :alt="item.attributes.name"
          >
        </v-list-item-avatar>
        <v-list-item-avatar v-else-if="item.type === 'artists'">
          <v-icon>mdi-account</v-icon>
        </v-list-item-avatar>
        <v-list-item-avatar v-else-if="item.type === 'albums'">
          <img
            :src="appleImage(item)"
            :alt="item.attributes.name"
          >
        </v-list-item-avatar>
        <v-list-item-content v-if="item.type === 'songs'">
          <v-list-item-title v-text="item.attributes.name" />
          <v-list-item-subtitle v-text="item.attributes.artistName" />
        </v-list-item-content>
        <v-list-item-content v-else-if="item.type === 'artists'">
          <v-list-item-title v-text="item.attributes.name" />
        </v-list-item-content>
        <v-list-item-content v-else-if="item.type === 'albums'">
          <v-list-item-title v-text="item.attributes.name" />
          <v-list-item-subtitle v-text="item.attributes.artistName" />
        </v-list-item-content>
        <v-list-item-content v-else v-text="item" />
        <v-list-item-action v-if="item.type === 'songs'">
          <v-btn icon>
            <v-icon color="grey lighten-1">
              mdi-waveform
            </v-icon>
          </v-btn>
        </v-list-item-action>	
        <v-list-item-action v-if="item.type === 'artists'">
          <v-btn icon>
            <v-icon color="grey lighten-1">
              mdi-brain
            </v-icon>
          </v-btn>
        </v-list-item-action>	
        <v-list-item-action v-if="item.type === 'albums'">
          <v-btn icon>
            <v-icon color="grey lighten-1">
              mdi-record-circle
            </v-icon>
          </v-btn>
        </v-list-item-action>	
      </template>
    </v-autocomplete>
  </div>
</template>

<script>
export default {
  data: () => ({
    isLoading: false,
    search: null,
    selectedSearch: null,
    entries: [],
  }),
  watch: {
    search (val) {
      // Items have already been requested
      this.isLoading = false;
      if (!val) {
        this.entries = [];
        return;
      }
      // this.entries = [
      //   {
      //     header: 'Tracks',
      //   },
      //   {
      //     divider: true,
      //   },
      //   {
      //     header: 'Artists',
      //   },
      //   {
      //     divider: true,
      //   },
      //   {
      //     header: 'Albums',
      //   },
      // ];
      this.isLoading = true;
      this.$store.dispatch('getHints', val).then(res => {
        this.isLoading = false;
        this.entries = [
          {
            header: 'Tracks',
          },
        ].concat(
          res.results.songs.data
        ).concat([
          {
            divider: true,
          },
          {
            header: 'Artists',
          },
        ]).concat(
          res.results.artists.data
        ).concat([
          {
            divider: true,
          },
          {
            header: 'Albums',
          },
        ]).concat(
          res.results.albums.data
        );
      });
      this.isLoading = false;
    },
    selectedSearch (newVal, oldVal) {
      this.isLoading = false;
      if (!newVal) return;
      if (newVal.type === 'songs') {
				this.$router.push({
					path: `/tracks/${newVal.id}`,
				});
      } else if (newVal.type === 'artists') {
				this.$router.push({
					path: `/artists/${newVal.id}`,
				});
      } else if (newVal.type === 'albums') {
				this.$router.push({
					path: `/albums/${newVal.id}`,
				});
      }
    },
  },
  methods: {
    appleImage (image) {
      return image.attributes.artwork.url.replace(
        '{w}', '2500'
      ).replace(
        '{h}', '2500'
      );
    },
  },
};
</script>

<style scoped>
</style>
