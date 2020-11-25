<template>
  <v-menu
    close-on-content-click
    origin="bottom right"
    z-index="10000"
    attach
    top
    left
    dark
    two-line
    max-width="25rem"
    transition="scale-transition"
  >
    <template v-slot:activator="{ on }">
      <v-btn
        icon
        dark
        :class="{ 'show-btns': hover }"
        @click.native.stop.prevent
        v-on="on"
      >
        <v-icon
          small
          color="transparent"
          :class="{ 'show-btns': hover }"
          class="album-overlay-more"
        >
          mdi-dots-horizontal
        </v-icon>
      </v-btn>
    </template>
    <v-list dense>
      <v-list-item 
        :style="{
          'justify-content':'center'
        }"
      >
        <v-rating
          background-color="white"
          color="var(--primary-purple)"
          dense
          half-increments
          hover
          size="18"
          @input="changeRating"
          @click.native.stop.prevent
        />
      </v-list-item>
      <v-dialog v-model="dialog" scrollable max-width="300px">
        <template v-slot:activator="{ on, attrs }">
          <v-list-item
            v-bind="attrs"
            v-on="on"
            @click.native.stop.prevent
          >
            <v-list-item-icon>
              <v-icon small>
                mdi-playlist-music
              </v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>
                Add to playlist
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
        <v-card>
          <v-tabs>
            <v-tab>Add to playlist</v-tab>
            <v-tab>Create a playlist</v-tab>
          </v-tabs>
        </v-card>
      </v-dialog>
      <v-divider />
      <v-list-item @click.native.stop.prevent @click="addToQueue">
        <v-list-item-icon>
          <v-icon small>
            mdi-thumb-up
          </v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>More like this</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-divider />
      <v-list-item @click.native.stop.prevent @click="addToQueue">
        <v-list-item-icon>
          <v-icon small>
            mdi-thumb-down
          </v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Less like this</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-divider />
      <v-list-item @click.native.stop.prevent @click="addToQueue">
        <v-list-item-icon>
          <v-icon small>
            mdi-playlist-star
          </v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Add to queue</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-divider />
      <v-list-item
        @click.native.stop.prevent
        @click="
          addToLibrary()
        "
      >
        <v-list-item-icon>
          <v-icon small>
            mdi-library
          </v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Add to library</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-menu>
</template>

<script>
export default {
  
};
</script>

<style scoped>
</style>