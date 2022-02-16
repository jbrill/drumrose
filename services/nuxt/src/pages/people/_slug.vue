<template>
  <v-container class="profileContain" style="width:100%">
    <v-responsive style="display: flex; justify-content: space-between">
      <v-skeleton-loader
        v-if="!profile"
        class="mx-auto"
        type="card"
      />
      <v-card
        v-else
        style="padding: 2rem;"
      >
        <v-row flex class="content-contain" style="margin: 0; width:100%">
          <v-col>
            <v-layout>
              <v-flex justify-space-between>
                <v-container flex style="display: flex; justify-content: space-between">
                  <v-col cols="12" sm="3">
                    <v-img
                      elevation="12"
                      src="https://picsum.photos/id/11/500/300"
                      lazy-src="https://picsum.photos/id/11/10/6"
                      aspect-ratio="1"
                      width="100%"
                      height="auto"
                      style="margin: 0 auto; border-radius: 50%" 
                      class="fill-height grey lighten-2"
                      gradient="
                        to top right, rgba(100,115,201,.0), rgba(25,32,72,.34)
                      "
                    >
                      <template v-slot:placeholder>
                        <v-row
                          class="fill-height ma-0"
                          align="center"
                          justify="center"
                        >
                          <v-progress-circular
                            indeterminate
                            color="grey lighten-5"
                          />
                        </v-row>
                      </template>
                    </v-img>
                    <p class="title profileName" style="padding-top: 2rem; text-align: center">
                      {{ profile.username }}
                    </p>
                    <!-- add if username is logged in -->
                    <v-btn to="/settings">
                      Edit Profile
                    </v-btn>
                  </v-col>
                  <v-container style="height: 20%">
                    <v-row style="justify-content: space-evenly">
                      <nuxt-link :to="'/' + profile.username + '/' + 'followers'">
                        <div>
                          <p class="overline number-descriptor" style="font-size: 2rem !important; text-align: center">{{ profile.followers.length }}</p>
                          <span class="overline descriptor" style="text-align: center">followers</span>
                        </div>
                      </nuxt-link>
                      <v-divider vertical />
                      <nuxt-link :to="'/' + profile.username + '/' + 'following'">
                        <p class="overline number-descriptor" style="text-align: center">{{ profile.following.length }}</p>
                        <p class="overline descriptor" style="text-align: center">following</p>
                      </nuxt-link>
                      <v-divider vertical />
                      <nuxt-link :to="'/' + profile.username + '/' + 'reviews'">
                        <p class="overline number-descriptor" style="text-align: center">{{ profile.track_reviews.length + profile.album_reviews.length + profile.playlist_reviews.length }}</p>
                        <p class="overline descriptor" style="text-align: center">reviews</p>
                      </nuxt-link>
                      <v-divider vertical />
                      <nuxt-link :to="'/' + profile.username + '/' + 'ratings'">
                        <p class="overline number-descriptor" style="text-align: center">{{ profile.followers.length }}</p>
                        <p class="overline descriptor" style="text-align: center">ratings</p>
                      </nuxt-link>
                    </v-row>
                  </v-container>
                </v-container>
              </v-flex>
            </v-layout>
          </v-col>
        </v-row>
      </v-card>
      <v-card>
        <CarouselSection
          v-if="profile"
          title="Favorites"
          :carousel-items="favoritedTracks"
        />
      </v-card>
      <v-card>
        <v-card-title>Favorited Albums</v-card-title>
      </v-card>
      <v-card>
        <v-card-title>Favorited Playlists</v-card-title>
      </v-card>
    </v-responsive>
  </v-container>
</template>

<script>
import {
  getUserDetail, getFavoritedTracks, addFollower,
} from '~/api/api';

export default {
  async asyncData ({ store, route, $auth }) {
    let userResponse;

    if ($auth.loggedIn) {
      userResponse = await getUserDetail(
        $auth.getToken('auth0'),
        route.params.slug,
      );
    } else {
      userResponse = await getUserDetail(
        $auth.getToken('auth0'),
        route.params.slug,
      );
    }
    let favoritesResponse = await getFavoritedTracks(
      $auth.getToken('auth0'),
      route.params.slug,
    );
    console.log(userResponse.data)
    if (!userResponse || userResponse.status != 200) {
      console.error(userResponse.data);
      return { "profile": null };
    }
    console.log(favoritesResponse);
    return {
      "profile": userResponse.data,
      "favoritedTracks": favoritesResponse.data.favorited_tracks,
    };
  },
};
</script>

<style scoped>
.descriptor {
  color: grey;
}
.descriptor:hover, .descriptor:focus{
  color: var(--primary-yellow) !important;
}
.number-descriptor {
  font-size: 2rem !important;
}
.v-application p {
  margin: 0 !important;
}
</style>
