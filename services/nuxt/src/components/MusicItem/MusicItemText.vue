<template>
<div class="textContain">
	<v-tooltip bottom>
		<template v-slot:activator="{ on }">
			<nuxt-link
				class="songName"
				:to="'/tracks/' + appleMusicId"
			>
				<span
					ref="songName"
					class="songName"
					v-on="on"
				>{{ name }}</span>
			</nuxt-link>
		</template>
		<div>track name</div>
	</v-tooltip>
	<v-tooltip v-if="type === 'playlist'" bottom>
		<template v-slot:activator="{ on }">
			<nuxt-link :to="'/people/' + curatorName" class="artistName">
				<span
					ref="curatorName"
					class="curatorName"
					v-on="on"
				>{{ curatorName }}</span>
			</nuxt-link>
		</template>
		<div>track name</div>
	</v-tooltip>
	<v-tooltip v-else bottom>
		<template v-slot:activator="{ on }">
			<nuxt-link :to="'/artists/' + artistName" class="artistName">
				<span
					ref="curatorName"
					class="artistName"
					v-on="on"
				>{{ artistName }}</span>
			</nuxt-link>
		</template>
		<div>artist name</div>
	</v-tooltip>
</div>
</template>

<script>
export default {
  props: {
    artistName: {

    },
    name: {
      
    },
  },
}
</script>

<style scoped>
.textContain {
  display: flex;
  bottom: 0;
  width: 100%;
  padding-top: 0.5rem;
  flex-direction: column;
  color: var(--primary-black-light);
}
</style>
