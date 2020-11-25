<template>
  <div class="textContain lighten">
    <nuxt-link
      class="songName"
      :to="primaryLink"
    >
      <span
        ref="songName"
        class="subtitle-1"
      >{{ primaryName }}</span>
    </nuxt-link>
    <nuxt-link
      :to="secondaryLink"
      class="artistName"
    >
      <span
        ref="curatorName"
        class="overline"
      >{{ secondaryName }}</span>
    </nuxt-link>
  </div>
</template>

<script>
export default {
  props: {
    primaryName: {
      type: String,
      default: '',
    },
    primaryLink: {
      type: String,
      default: '',
    },
    secondaryName: {
      type: String,
      default: '',
    },
    secondaryLink: {
      type: String,
      default: '',
    },
  },
};
</script>

<style scoped>
@media screen and (prefers-color-scheme: dark) {
  .songName:hover, .songName:focus {
    color: black;
  }
  .artistName:hover, .artistName:focus {
    color: black;
  }
  .textContain {
    color: grey;
  }
  .posterInfo {
    color: black;
  }
  .posterName {
    color: black;
  }
  .posterHandle {
    color: black;
  }
  .postDate {
    color: black;
  }
  .postTime {
    color: black;
  }
  .audioAction {
    color: black;
  }
  .audioFavorite:hover, .audioFavorite:focus {
    color: grey;
  }
}
>>>.v-list-item {
  min-height: 2rem;
}
>>>.v-sheet {
  padding: 0;
}
.artistName {
  font-size: 0.8rem;
  margin-bottom: 0;
  font-weight: 600;
  padding-top: 5px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  color: #f2f2f2;
}
.artistName:hover, .artistName:focus {
  color: white;
}
.songName {
  font-size: 0.75rem;
  margin-bottom: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  opacity: 1;
  color: #ccc;
}
.songName:hover, .songName:focus {
  color: white;
}
.textContain {
  display: flex;
  bottom: 0;
  width: 100%;
  padding-top: 0.5rem;
  flex-direction: column;
  color: var(--primary-black-light);
}
</style>
