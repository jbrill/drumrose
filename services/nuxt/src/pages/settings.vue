<template>
  <v-container flex class="settings-contain">
    <v-radio-group type="number" v-model.number="bitrate" label="Bitrate" :mandatory="true">
			<v-radio label="Standard (64 kbps)" :value="64"></v-radio>
			<v-radio label="High (256 kbps)" :value="256"></v-radio>
		</v-radio-group>
    <v-divider></v-divider>
    <span>Select your country</span>
    <v-select
      v-model="storefront"
			:items="countries"
			label="Select your country"
      outlined
      persistent-hint
      placeholder="Apple Music Storefront"
      prepend-inner-icon="mdi-earth"
			solo
		></v-select>
		</v-row>
    <v-divider v-if="auth.loggedIn"></v-divider>
    <span v-if="auth.loggedIn">Account options</span>
    <v-btn v-if="auth.loggedIn" @click.stop="resetPasswordDialog = true" color="var(--primary-purple)">Reset Password</v-btn>
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
    <v-btn v-if="auth.loggedIn" @click.stop="deleteAccountDialog = true" color="var(--primary-red)">Delete Account</v-btn>
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
  </v-container>
</template>

<script>
import { mapState } from 'vuex';

export default {
  data () {
    return {
      resetPasswordDialog: false,
      deleteAccountDialog: false,
      countries: [],
      selectedCountry: null,
      loadingCountries: false,
    }
  },
  computed: {
    ...mapState(['auth']),
    bitrate: {
			get () {
				return this.$store.state.bitrate
			},
			set (value) {
				this.$store.dispatch('setbitrate', value);
			}
		},
    storefront: {
			get () {
				return this.$store.state.storefront
			},
			set (value) {
				this.$store.dispatch('setStorefront', value);
			}
		}
  },
  async fetch () {
    this.loadingCountries = true;
    const storefrontResp = await this.$store.getters.fetch(
      "/v1/storefronts"
    )
    const userStorefrontResp = await this.$store.getters.fetch(
      "/v1/me/storefront"
    )
    this.countries = storefrontResp.data.map(country => country.attributes.name)
    this.selectedCountry = userStorefrontResp.data[0].attributes.name;
    this.loadingCountries = false;
  },
}
</script>

<style scoped>
>>>.v-label {
  margin: 0;
}
</style>
