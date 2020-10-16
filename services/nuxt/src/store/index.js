/* global MusicKit */

import axios from 'axios';
import clonedeep from 'lodash.clonedeep';
import { errorMessage } from '~/utils/MusicKit';


export const state = () => ({
	// State information
  isInitialized: false,
  supportsEME: false,
  storefront: '',

  // Authorization information
  isAuthorized: false,

  // Now playing information
  bitrate: 0,
  playbackState: 0,
  bufferedProgress: 0,
  shuffleMode: 0,
  repeatMode: 0,
  nowPlayingItem: null,
  playbackTime: null,
  volume: null,

	// Queue
  queue: [],
  queuePosition: -1,
  history: [],

  // Library
  activeCollection: null,

  // Posts
  favoritedPosts: [],
  activePost: null,

  // Server side
  appleMusicToken: null,
});


/**
 * Return the appropriate API object.
 */
let getApi = library => {
  if (process.server) return;
  return library ? 
    MusicKit.getInstance().api.library : MusicKit.getInstance().api;
};


/**
 * Returns headers for a fetch request to the Apple Music API.
 */
export function apiHeaders (state) {
  if (process.client) {
		return {
			Authorization: 'Bearer ' + MusicKit.getInstance().developerToken,
			Accept: 'application/json', 'Content-Type': 'application/json',
			'Music-User-Token': '' + MusicKit.getInstance().musicUserToken,
		};
  } else {
		return {
			Authorization: 'Bearer ' + state.appleMusicToken,
			Accept: 'application/json', 'Content-Type': 'application/json',
		};
  }
}


export const getters = {
  storefront (state) {
    return state.storefront;
  },

	getCurrentPlaybackDuration (state) {
		if (state.playbackTime && state.playbackTime.currentPlaybackDuration) {
      const minutes = Math.floor(
        state.playbackTime.currentPlaybackDuration / 60
      );
      const seconds = state.playbackTime.currentPlaybackDuration - minutes * 60;
      const parsedMinutes = minutes;
      const parsedSeconds = seconds < 10 ? `0${seconds}` : `${seconds}`;
      return `${parsedMinutes}:${parsedSeconds}`;
    }
    return "0:00";
	},
	
	getCurrentPlaybackTime (state) {
		if (state.playbackTime && state.playbackTime.currentPlaybackTime) {
      const minutes = Math.floor(state.playbackTime.currentPlaybackTime / 60);
      const seconds = state.playbackTime.currentPlaybackTime - minutes * 60;
      const parsedMinutes = minutes;
      const parsedSeconds = seconds < 10 ? `0${seconds}` : `${seconds}`;
      return `${parsedMinutes}:${parsedSeconds}`;
    }
    return "0:00";
	},

  async recommendations (state) {
    return await MusicKit.getInstance().api.recommendations();
  },
  async recentlyAdded (state) {
    return await MusicKit.getInstance().api.library.collection(
      'recently-added', null, {}
    );
  },
  async recentlyPlayed (state) {
    return await getApi(false).recentPlayed();
  },
  async heavyRotation (state) {
    return await getApi(false).historyHeavyRotation();
  },
  getQueue (state) {
   return state.queue;
  },
  // Data fetching
  get (state) {
    try {
      async (library, type, id, options) => {
        await getApi(library)[type](id, options);
      };
    } catch (err) {
      if (err == MusicKit.MKError.ACCESS_DENIED) {
        console.log("AY");
      }
    }
  },
  collection (state) {
    return (library, type, id, options) => {
      return getApi(library).api.collection(type, id, options);
    };
  },
  headers ( state ) {
		if (process.client) {
			return new Headers({
				Authorization: 'Bearer ' +
          MusicKit.getInstance().developerToken,
				Accept: 'application/json', 'Content-Type': 'application/json',
				'Music-User-Token': '' + MusicKit.getInstance().musicUserToken,
			});
		} else {
			return {
				Authorization: 'Bearer ' + state.appleMusicToken,
				Accept: 'application/json', 'Content-Type': 'application/json',
			};
		}
  },
  fetch (state, { $sentry }) {
    return path => {
      return fetch(
        `https://api.music.apple.com${path}`,
        {
          headers: getters.headers( state ),
        }
      ).then( r => {
        return r.json();
      }).catch( err => {
        console.error(err);
        $sentry.captureException(err);
      });
    };
  },
  search (state) {
    return (library, query, options) => {
      return getApi(library).search(query, options);
    };
  },
};

export const mutations = {
  favoritedPosts (state, posts) {
    state.favoritedPosts = posts;
  },
	init (state) {
    if (state.isInitialized) {
      console.warn('Already initialized; aborting');
      return;
    }

    state.isInitialized = true;
  },
	setAppleMusicToken (state, apple_music_token) {
		state.appleMusicToken = apple_music_token;
	},
	activeCollection (state, activeCollection) {
		state.activeCollection = activeCollection;
	},
  isAuthorized (state, isAuthorized) {
    state.isAuthorized = isAuthorized;
  },
  supportsEME (state, supportsEME) {
    state.supportsEME = supportsEME;
  },
  storefront (state, storefront) {
    state.storefront = storefront;
  },

  // Now playing
  bitrate (state, bitrate) {
    state.bitrate = bitrate;
  },
  playbackState (state, playbackState) {
    state.playbackState = playbackState;
  },
  bufferedProgress (state, bufferedProgress) {
    state.bufferedProgress = bufferedProgress;
  },
  shuffleMode (state, shuffleMode) {
    state.shuffleMode = shuffleMode;
  },
  repeatMode (state, repeatMode) {
    state.repeatMode = repeatMode;
  },
  nowPlayingItem (state, nowPlayingItem) {
    state.nowPlayingItem = nowPlayingItem;
  },
  playbackTime (state, playbackTime) {
    state.playbackTime = playbackTime;
  },
  volume (state, volume) {
    state.volume = volume;
  },

  // Queue
  queue (state, queue) {
    state.queue = queue;
  },
  queuePosition (state, position) {
    state.queuePosition = position;
  },
  addHistoryItem (state, item) {
    // Only keep 100 items in the history.
    state.history.splice(0, 0, clonedeep(item));
    state.history = state.history.slice(0, Math.min(state.history.length, 100));
  },

  // Posts
  nowPlayingPost (state, nowPlayingPost) {
    state.nowPlayingPost = nowPlayingPost;
  },
  posts (state, posts) {
    state.posts = posts;
  },

  // Event listeners
  addEventListener (state, listener) {
    MusicKit.getInstance().addEventListener(listener.event, listener.func);
  },
  removeEventListener (state, listener) {
    MusicKit.getInstance().removeEventListener(listener.event, listener.func);
  },
};

export const actions = {
  async nuxtServerInit ({ commit }, { $sentry }) {
    try {
      const tokenResponse = await axios.post(
        'https://teton.drumrose.io/api/apple_music_token/'
      );
      await commit('setAppleMusicToken', tokenResponse.data.token);
    } catch(err) {
      console.error(err);
      $sentry.captureException(err);
    }
  },
	async nuxtClientInit (
    { commit, state, dispatch }, { $sentry, req }, )
  {
    try {
      const tokenResponse = await axios.post(
        'https://teton.drumrose.io/api/apple_music_token/'
      );
      console.log(tokenResponse);
      commit('setAppleMusicToken', tokenResponse.data.token);

      MusicKit.configure({
        developerToken: tokenResponse.data.token,
        app: {
          name: 'DRUMROSE',
          build: '2.0.0',
          icon: "ICON",
        },
      });
    } catch(err) {
      console.error(err);
      $sentry.captureException(err);
    }

    let localStorage = window.localStorage;

    // Check for EME
    commit('supportsEME', MusicKit.getInstance().player.canSupportDRM);

    // storefront
    commit('storefront', MusicKit.getInstance().storefrontId);

    // Update authorization status
    commit('isAuthorized', MusicKit.getInstance().isAuthorized);

    // Update volume status
    commit('volume', MusicKit.getInstance().player.volume);

    if (localStorage && localStorage.getItem('volume')) {
      try {
        dispatch(
          'setVolume', JSON.parse(localStorage.getItem('volume') || '1')
        );
      } catch (err) {
        console.error(err);
        $sentry.captureException(err);
      }
    }

    // Update bitrate
    commit('bitrate', MusicKit.getInstance().bitrate);

    if (localStorage && localStorage.getItem('bitrate')) {
      try {
        dispatch(
          'setBitrate', MusicKit.PlaybackBitrate[
            localStorage.getItem('bitrate') || 'HIGH'
          ]
        );
      } catch (err) {
        console.error(err);
        $sentry.captureException(err);
      }
    }

    // Update shuffle mode
    commit('shuffleMode', MusicKit.getInstance().player.shuffleMode);

    if (localStorage && localStorage.getItem('shuffle')) {
      try {
        dispatch(
          'shuffle', JSON.parse(localStorage.getItem('shuffle') || 'false')
        );
      } catch (err) {
        console.error(err);
        $sentry.captureException(err);
      }
    }

    // Update shuffle mode
    commit('repeatMode', MusicKit.getInstance().player.repeatMode);

    if (localStorage && localStorage.getItem('repeat')) {
      try {
        dispatch('repeat', JSON.parse(localStorage.getItem('repeat') || '0'));
      } catch (err) {
        console.error(err);
        $sentry.captureException(err);
      }
    }

    // Update playback state
    commit('playbackState', MusicKit.getInstance().playbackState);

    // Update bufferred status
    commit(
      'bufferedProgress',
      MusicKit.getInstance().player.currentBufferedProgress
    );

    // Update queue information
    commit('queue', clonedeep(MusicKit.getInstance().player.queue.items));
    commit('queuePosition', MusicKit.getInstance().player.queue.position);
    
    // Update library information
    commit('activeCollection', 'artists');

    // Register event handlers
    commit('addEventListener', {
      event: MusicKit.Events.storefrontIdentifierDidChange,
      func: evt => {
        commit('storefront', MusicKit.getInstance().storefrontId);
      },
    });

    commit('addEventListener', {
      event: MusicKit.Events.storefrontCountryCodeDidChange,
      func: evt => {
        commit('storefront', MusicKit.getInstance().storefrontId);
      },
    });

    commit('addEventListener', {
      event: MusicKit.Events.authorizationStatusDidChange,
      func: evt => {
        if (MusicKit.getInstance().isAuthorized) {
          setTimeout(() => {
            MusicKit.getInstance().me().then(me => {
              commit('storefront', me.storefront);
            });
          }, 1000);
        }

        commit('isAuthorized', MusicKit.getInstance().isAuthorized);
      },
    });

    commit('addEventListener', {
      event: MusicKit.Events.playbackStateDidChange,
      func: evt => {
        commit('playbackState', evt.state);
      },
    });

    commit('addEventListener', {
      event: MusicKit.Events.bufferedProgressDidChange,
      func: evt => {
        commit('bufferedProgress', evt.progress);
      },
    });

    commit('addEventListener', {
      event: MusicKit.Events.mediaItemDidChange,
      func: evt => {
        // Add the current item (if any) to the history.
        if (state.nowPlayingItem) {
          commit('addHistoryItem', state.nowPlayingItem);
        }

        commit('nowPlayingItem', clonedeep(evt.item));
      },
    });

    commit('addEventListener', {
      event: MusicKit.Events.playbackTimeDidChange,
      func: evt => {
        commit('playbackTime', clonedeep(evt));
      },
    });

    commit('addEventListener', {
      event: MusicKit.Events.playbackVolumeDidChange,
      func: evt => {
        commit('volume', MusicKit.getInstance().player.volume);
      },
    });

    commit('addEventListener', {
      event: MusicKit.Events.primaryPlayerDidChange,
      func: evt => {
        commit('supportsEME', MusicKit.getInstance().player.canSupportDRM);
      },
    });

    commit('addEventListener', {
      event: MusicKit.Events.playbackBitrateDidChange,
      func: evt => {
        commit('bitrate', MusicKit.getInstance().bitrate);
      },
    });

    commit('addEventListener', {
      event: MusicKit.Events.queueItemsDidChange,
      func: items => commit('queue', clonedeep(items)),
    });

    commit('addEventListener', {
      event: MusicKit.Events.queuePositionDidChange,
      func: evt => commit('queuePosition', evt.position),
    });

    commit('addEventListener', {
      event: MusicKit.Events.mediaPlaybackError,
      func: evt => {
        console.error('PLAYBACK_ERROR', evt);
        $sentry.captureException(evt);

        // Notify the user of the error.
        dispatch(
          'alerts/add', errorMessage({
            name: MusicKit.MKError.MEDIA_PLAYBACK,
          }), { 
            root: true,
          }
        );
      },
    });

    // Initialize the instance
    commit('init');
  },
  setStorefront ({ commit }, storefront) {
    MusicKit.getInstance().storefrontId = storefront;
    MusicKit.getInstance().api.userStorefrontId = storefront;
    MusicKit.getInstance().storekit.storefrontCountryCode = storefront;
    commit('storefront', storefront);
  },
  async resetStorefront ({ dispatch }) {
    let me = await MusicKit.getIntance.me();

    if (me.storefront) {
      dispatch('setStorefront', me.storefront);
    } else {
      dispatch('setStorefront', 'us');
    }
  },
  setNowPlayingPost ({ commit }, post) {
    commit('nowPlayingPost', post);
  },
  setFavoritedPosts ({ commit }, posts) {
    commit('favoritedPosts', posts);
  },
  setActiveCollection ({ commit }, activeCollection) {
    commit('activeCollection', activeCollection);
  },
  toggleShuffleMode ({ commit, state }) {
    MusicKit.getInstance().player.shuffle = state.shuffleMode === 0 ? 1 : 0;
    commit('shuffleMode', MusicKit.getInstance().player.shuffleMode);

    if (window.localStorage) {
      window.localStorage.setItem(
        'shuffle', JSON.stringify(state.shuffleMode === 1)
      );
    }
  },
  shuffle ({ commit }, shuffle = true) {
    MusicKit.getInstance().player.shuffle = shuffle;
    if (window.localStorage) {
      window.localStorage.setItem('shuffle', JSON.stringify(shuffle));
    }
    commit('shuffleMode', MusicKit.getInstance().player.shuffleMode);
  },
  toggleRepeatMode ({ commit }) {
    // Repeat modes: 0 - off, 1 - one, 2 - all
    MusicKit.getInstance().player.repeatMode = 
      MusicKit.getInstance().player.repeatMode === 0 ? 
      2 : MusicKit.getInstance().player.repeatMode - 1;
    commit('repeatMode', MusicKit.getInstance().player.repeatMode);
    if (window.localStorage) {
      window.localStorage.setItem(
        'repeat', JSON.stringify(MusicKit.getInstance().player.repeatMode)
      );
    }
  },
  repeat ({ commit }, mode = 2) {
    MusicKit.getInstance().player.repeatMode = mode;
    commit('repeatMode', MusicKit.getInstance().player.repeatMode);
    if (window.localStorage) {
      window.localStorage.setItem('repeat', JSON.stringify(mode));
    }
  },
  setBitrate ({ commit }, bitrate) {
    MusicKit.getInstance().bitrate = bitrate;
    commit('bitrate', MusicKit.getInstance().bitrate);
    if (window.localStorage) {
      window.localStorage.setItem('bitrate', MusicKit.PlaybackBitrate[bitrate]);
    }
  },

  async play (_) {
    await MusicKit.getInstance().player.play();
  },
  async pause (_) {
    await MusicKit.getInstance().player.pause();
  },
  async previous (_) {
    await MusicKit.getInstance().player.skipToPreviousItem();
  },
  async next (_) {
    await MusicKit.getInstance().player.skipToNextItem();
  },
  async seek (_, time) {
    await MusicKit.getInstance().player.seekToTime(time);
  },
  async playNext (_, queue) {
    await MusicKit.getInstance().player.queue.prepend(queue);
  },
  async playLater (_, queue) {
    await MusicKit.getInstance().player.queue.append(queue);
  },
  changeTo (_, position) {
    return MusicKit.getInstance().changeToMediaAtIndex(position);
  },
  setQueue (_, queue) {
    return MusicKit.getInstance().setQueue(queue);
  },
  authorize (_) {
    return MusicKit.getInstance().authorize();
  },
  setVolume (_, volume) {
    const newVolume = parseFloat(volume);

    MusicKit.getInstance().player.volume = newVolume;

    if (window.localStorage) {
      window.localStorage.setItem('volume', JSON.stringify(newVolume));
    }
  },

  // Ratings
  rate (_, { item, rating }) {
    let types = {
      song: 'songs',
      playlist: 'playlists',
      album: 'albums',
      station: 'stations',
      'library-songs': 'library-songs',
      'library-playlists': 'library-playlists',
      'library-albums': 'library-albums',
      'library-stations': 'library-stations',
    };

    if (!(item.type in types)) {
      return;
    }

    return new Promise(async (resolve, reject) => {
      try {
        let res = await fetch(
          `https://api.music.apple.com/v1/me/ratings/
          ${types[item.type]}/${item.id}`,
          {
            method: 'PUT',
            headers: apiHeaders(),
            body: JSON.stringify({
              type: 'rating',
              attributes: {
                value: rating,
              },
            }),
          }
        );

        if (res.status === 200) {
          resolve(true);
        } else {
          reject(MusicKit.MKError(MusicKit.MKError.SERVER_ERROR));
        }
      } catch (err) {
        reject(err);
      }
    });
  },
  love ({ dispatch }, item) {
    return dispatch('rate', {
      item: item,
      rating: 1,
    });
  },
  dislike ({ dispatch }, item) {
    return dispatch('rate', {
      item: item,
      rating: -1,
    });
  },

  // Library
  addToLibrary (_, { type, id }) {
    return new Promise(async (resolve, reject) => {
      try {
        await fetch(
          `https://api.music.apple.com/v1/me/library/?ids[${type}s]=${id}`,
          {
            method: 'POST',
            headers: apiHeaders(),
            body: {},
          }
        );

        resolve(true);
      } catch (err) {
        reject(err);
      }
    });
  },

  addToPlaylist (_, { playlistId, items }, { sentry }) {
    return new Promise(async (resolve, reject) => {
      try {
        let res = await fetch(
          `https://api.music.apple.com/v1/me/library/playlists/
          ${playlistId}/tracks`,
          {
            method: 'POST',
            headers: apiHeaders(),
            body: JSON.stringify({
              data: items,
            }),
          }
        );

        if (res.status === 204) {
          // Invalid local cache
          let api = getApi(true);
          api.clearCacheItems();

          // Return successful
          resolve(true);
        } else {
          reject(MusicKit.MKError(MusicKit.MKError.SERVER_ERROR));
        }
      } catch (err) {
        reject(err);
      }
    });
  },

  newPlaylist (_, { name, items = [] }, { $sentry }) {
    return new Promise(async (resolve, reject) => {
      try {
        let res = await fetch(
          `https://api.music.apple.com/v1/me/library/playlists`,
          {
            method: 'POST',
            headers: apiHeaders(),
            body: JSON.stringify({
              attributes: {
                name: name,
              },
              relationships: {
                tracks: {
                  data: items,
                },
              },
            }),
          }
        );

        if (res.status === 201) {
          // Invalid local cache
          let api = getApi(true);
          api.clearCacheItems();

          // Return successful
          resolve(true);
        } else {
          reject(MusicKit.MKError(MusicKit.MKError.SERVER_ERROR));
        }
      } catch (err) {
        reject(err);
      }
    });
	},
  
  async getHints (_, searchInput) {
     const getHints = {
       method: "GET",
       url: `https://api.music.apple.com/v1/catalog/us/search?term=` + 
            `${searchInput}&limit=5&types=` +
            `songs,artists,albums,playlists,`,
       headers: apiHeaders(),
     };
     const { data } = await axios(getHints);
     return data;
  },
};

export const strict = false;
