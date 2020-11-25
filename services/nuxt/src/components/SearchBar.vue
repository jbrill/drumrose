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
      color="var(--primary-yellow)"
      item-text="attributes.name"
      item-value="attributes.name"
      no-data-text="No data found"
      placeholder="Search music"
      prepend-inner-icon="mdi-magnify"
      outlined
      width="15rem"
      return-object
      @keydown.enter="searchVal"
    >
      <template v-slot:no-data>
        <v-list-item>
          <v-list-item-title>
            Search for your favorite
            <strong>music</strong>
          </v-list-item-title>
        </v-list-item>
      </template>
      <v-btn
        v-if="search"
        slot="prepend-item"
        text
        nuxt
        width="100%"
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
      console.log(val);

      this.isLoading = true;
      this.$store.dispatch('getHints', val).then(res => {
        this.isLoading = false;
        console.log(res.results);
        this.entries = [];
        if ('songs' in res.results && 'data' in res.results.songs) {
          this.entries.push({
            header: 'Tracks',
          });
          res.results.songs.data.forEach( song => {
            this.entries.push(song);
          });
            
          this.entries.push({
              divider: true,
          });
        }
        if ('artists' in res.results && 'data' in res.results.artists) {
          this.entries.push({
            header: 'Artists',
          });
          res.results.artists.data.forEach( artist => {
            this.entries.push(artist);
          });
            
          this.entries.push({
              divider: true,
          });
        }
        if ('albums' in res.results && 'data' in res.results.albums) {
          this.entries.push({
            header: 'Albums',
          });
          res.results.albums.data.forEach( album => {
            this.entries.push(album);
          });
            
          this.entries.push({
              divider: true,
          });
        }
        console.log(this.entries);
      }).catch(err => {
        console.log(err);
      })
      .finally(() => (this.isLoading = false));
      
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
    searchVal (ev) {
      if (ev.keyCode === 13) {
        let newVal = ev.target.value;
        this.isLoading = false;
        if (!newVal) return;
        this.$router.push({
          path: `/search/${newVal}`,
        });
      }
    },
  },
};
</script>

<style scoped>
>>>.v-list-item {
  max-width: 20rem !important;
}
</style>
