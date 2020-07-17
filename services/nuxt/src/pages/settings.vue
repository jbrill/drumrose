<template>
  <div class="settings-contain">
    <v-radio-group type="number" v-model.number="bitrate" label="Bitrate" :mandatory="true">
			<v-radio label="Standard (64 kbps)" :value="64"></v-radio>
			<v-radio label="High (256 kbps)" :value="256"></v-radio>
		</v-radio-group>
    <v-divider></v-divider>
    <v-btn @click.stop="resetPasswordDialog = true" color="var(--primary-purple)">Reset Password</v-btn>
    <v-dialog
			v-model="resetPasswordDialog"
			width="500"
		>
			<v-card>
				<v-card-title class="headline">Confirm your password reset</v-card-title>

				<v-card-text>
				  To reset your password, we'll send a link to your email.
        </v-card-text>

				<v-card-actions>
					<v-spacer></v-spacer>

					<v-btn
						color="var(--primary-purple)"
						@click="resetPasswordDialog = false"
					>
						Reset
					</v-btn>
				</v-card-actions>
			</v-card>
		</v-dialog>
    <v-btn @click.stop="deleteAccountDialog = true" color="var(--primary-red)">Delete Account</v-btn>
    <v-dialog
			v-model="deleteAccountDialog"
      width="500"
		>
			<v-card>
				<v-card-title class="headline">Confirm account deletion</v-card-title>

				<v-card-text>
				  To delete your account, please confirm by clicking the button below.
        </v-card-text>

				<v-card-actions>
					<v-spacer></v-spacer>

					<v-btn
						color="var(--primary-red)"
						@click="deleteAccountDialog = false"
					>
						Reset
					</v-btn>
				</v-card-actions>
			</v-card>
		</v-dialog>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  data () {
    return {
      resetPasswordDialog: false,
      deleteAccountDialog: false,
    }
  },
  computed: {
    bitrate: {
			get () {
				return this.$store.state.bitrate
			},
			set (value) {
        console.log(value)
				this.$store.dispatch('setBitrate', value)
			}
		}
  },
}
</script>

<style scoped>
>>>.v-label {
  margin: 0;
}
</style>
