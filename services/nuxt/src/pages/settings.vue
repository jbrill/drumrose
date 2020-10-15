<template>
  <v-container flex class="settings-contain">
    <v-radio-group
      v-model.number="bitrate"
      type="number"
      label="Bitrate"
      :mandatory="true"
    >
      <v-radio label="Standard (64 kbps)" :value="64" />
      <v-radio label="High (256 kbps)" :value="256" />
    </v-radio-group>
    <v-divider />
    <span>Select your country</span>
    <v-select
      v-model="storefront"
      :items="countries"
      item-text="name"
      item-value="code"
      label="Select your country"
      index="code"
      outlined
      persistent-hint
      placeholder="Storefront"
      prepend-inner-icon="mdi-earth"
      solo
    />
    <v-divider v-if="auth.loggedIn" />
    <span v-if="auth.loggedIn">Account options</span>
    <v-btn
      v-if="auth.loggedIn"
      color="var(--primary-purple)"
      @click.stop="resetPasswordDialog = true"
    >
      Reset Password
    </v-btn>
    <v-dialog
      v-model="resetPasswordDialog"
      width="500"
    >
      <v-card >
        <v-card-title class="headline">
          Confirm your password reset
        </v-card-title>

        <v-card-text>
          To reset your password, we'll send a link to your email.
        </v-card-text>

        <v-card-actions>
          <v-spacer />

          <v-btn
            color="var(--primary-purple)"
            @click="resetPasswordDialog = false"
          >
            Reset
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-btn
      v-if="auth.loggedIn"
      color="var(--primary-red)"
      @click.stop="deleteAccountDialog = true"
    >
      Delete Account
    </v-btn>
    <v-dialog
      v-model="deleteAccountDialog"
      width="500"
    >
      <v-card>
        <v-card-title class="headline">
          Confirm account deletion
        </v-card-title>

        <v-card-text>
          To delete your account, please confirm by clicking the button below.
        </v-card-text>

        <v-card-actions>
          <v-spacer />

          <v-btn
            color="var(--primary-red)"
            @click="deleteAccountDialog = false"
          >
            Delete
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import { mapState } from 'vuex';

export default {
  async fetch () {
    this.loadingCountries = true;
    if (this.$store.isAuthorized) {
      const userStorefrontResp = await this.$store.getters.fetch(
        "/v1/me/storefront"
      );
      this.selectedCountry = userStorefrontResp.data[0].attributes.name;
    }

    const storefrontResp = await this.$store.getters.fetch(
      "/v1/storefronts"
    );
    storefrontResp.data.forEach( country => {  
      this.countries.push({
        'name': country.attributes.name,
        'code': country.id,
      });
    });
    this.loadingCountries = false;
  },
  data () {
    return {
      resetPasswordDialog: false,
      deleteAccountDialog: false,
      countries: [],
      selectedCountry: null,
      loadingCountries: false,
    };
  },
  computed: {
    ...mapState(['auth']),
    bitrate: {
			get () {
				return this.$store.state.bitrate;
			},
			set (value) {
				this.$store.dispatch('setBitrate', value);
			},
		},
    storefront: {
			get () {
				return this.$store.state.storefront;
			},
			set (value) {
        console.log(value);
				this.$store.dispatch('setStorefront', value);
			},
		},
  },
};
</script>

<style scoped>
>>>.v-label {
  margin: 0;
}
.settings-contain * {
  padding-top: 1rem;
}
</style>
