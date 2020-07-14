<template>
  <div class="settings-contain">
    <span>Bitrate</span>
    <v-radio-group v-model="radios" :mandatory="false">
			<v-radio label="Standard (64 kbps)" value="radio-1"></v-radio>
			<v-radio label="High (256 kbps)" value="radio-2"></v-radio>
		</v-radio-group>
    <v-divider></v-divider>
    <v-btn color="var(--primary-purple)">Reset Password</v-btn>
    <v-btn color="var(--primary-red)">Delete Account</v-btn>
  </div>
</template>

<script>
export default {
  data () {
    return {
      radios: 'radio-1',
    }
  },
}
</script>

<style scoped>
>>>.v-label {
  margin: 0;
}
</style>
