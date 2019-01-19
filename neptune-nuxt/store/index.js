export const state = () => {
  return {
    music_token: null,
    user: null,
    track_queue: null
  };
};

export const mutations = {
  SET_USER(state, user) {
    state.user = user || null;
  },
  SET_MUSIC_TOKEN(state, music_token) {
    state.music_token = music_token || null;
  },
  SET_PLAYING(state, track_info) {
    state.track_queue = track_info || null;
  }
};

export const getters = {
  isAuthenticated(state) {
    return !!state.user;
  },
  isMusicAuthenticated(state) {
    return !!state.music_token;
  },
  loggedUser(state) {
    return state.user;
  },
  musicToken(state) {
    return state.music_token;
  },
  trackQueue(state) {
    return state.track_queue;
  }
};
