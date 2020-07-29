<template>
	<v-snackbar
		v-model="show"
		bottom
		right
    elevation="20"
    style="z-index: 2"
		:timeout="timeout"
	>
		{{ message }}
		<template v-slot:action="{ attrs }">
			<v-btn
				dark
				text
				v-bind="attrs"
				@click="show = false"
			>
				Close
			</v-btn>
		</template>
	</v-snackbar>
</template>

<script>
export default {
  data () {
    return {
      show: false,
      message: '',
      timeout: 6000,
      success: false,
    }
  },
  created: function () {
    this.$store.watch(state => state.snackbar.snack, () => {
      const msg = this.$store.state.snackbar.snack
      if (msg !== '') {
        this.show = true
        this.message = this.$store.state.snackbar.snack
        this.$store.commit('snackbar/setSnack', '')
      }
    })
  }
}
</script>

<style scoped>
</style scoped>
