import axios from 'axios';


/*
 * Fetches reviews
 * */
export const getTrackReviews = async bearerToken => {
  try {
    const response = await axios.get(
      `https://teton.drumrose.io/api/reviews/tracks/`,
      {
        headers: {
          Authorization: `${bearerToken}`,
        },
      }
    );
    return response;
  } catch(err) {
    throw new Error(err);
  }
};

/*
 * Fetches reviews
 * */
export const getReviews = async bearerToken => {
  try {
    const response = await axios.get(
      `https://teton.drumrose.io/api/reviews/`,
      {
        headers: {
          Authorization: `${bearerToken}`,
        },
      }
    );
    return response;
  } catch(err) {
    console.error(err);
    return {
      data: [],
    };
  }
};


/*
 * Fetches followers
 * */
export const getFollowers = async (bearerToken, userHandle) => {
  try {
    const response = await axios.get(
      `https://teton.drumrose.io/api/followers/${userHandle}/`,
      {
        headers: {
          Authorization: `${bearerToken}`,
        },
      }
    );
    return response;
  } catch(err) {
    console.error(err);
    return {
      data: [],
    };
  }
};


/*
 * Fetches user detail
 * */
export const getUserDetail = async (bearerToken, userHandle) => {
  try {
    const response = await axios.get(
      `https://teton.drumrose.io/api/users/${userHandle}/`,
      {
        headers: {
          Authorization: `${bearerToken}`,
        },
      }
    );
    return response;
  } catch(err) {
    console.error(err);
    return {
      data: [],
    };
  }
};


/*
 * Fetches user list
 * */
export const getUserList = async bearerToken => {
  try {
    const response = await axios.get(
      `https://teton.drumrose.io/api/users/`,
      {
        headers: {
          Authorization: `${bearerToken}`,
        },
      }
    );
    return response;
  } catch(err) {
    console.error(err);
    return {
      data: [],
    };
  }
};

/* 
 * Fetches a list of favorites. Can consist of albums, tracks, or playlists
 * */
export const getFavorites = async bearerToken => {
  try {
    const response = await axios.get(
      'https://teton.drumrose.io/api/favorites/',
      {
        headers: {
          Authorization: `${bearerToken}`,
        },
      }
    );
    return response;
  } catch (err) {
    console.error(err);
    return {
      data: [],
    };
  }
};

/* 
 * Fetches a list of favorites. Can consist of albums, tracks, or playlists
 * */
export const postFavorite = async (bearerToken, data) => {
  try {
    const response = await axios.post(
      'https://teton.drumrose.io/api/favorites/',
      data,
      {
        headers: {
          Authorization: `${bearerToken}`,
        },
      }
    );
    return response;
  } catch (err) {
    console.error(err);
    return {
      data: [],
    };
  }
};

/* 
 * Fetches a list of favorites. Can consist of albums, tracks, or playlists
 * */
export const postReview = async (bearerToken, data) => {
  try {
    const response = await axios.post(
      'https://teton.drumrose.io/api/reviews/',
      data,
      {
        headers: {
          Authorization: `${bearerToken}`,
        },
      }
    );
    return response;
  } catch (err) {
    console.error(err);
    return {
      data: [],
    };
  }
};

/* 
 * Fetches a list of favorite tracks
 * */
export const getFavoritedTracks = async bearerToken => {
  try {
    const response = await axios.get(
      'https://teton.drumrose.io/api/favorites/tracks/',
      {
        headers: {
          Authorization: `Bearer ${bearerToken}`,
        },
      }
    );
    return response;
  } catch (err) {
    console.error(err);
    return {
      data: [],
    };
  }
};

export const getPlaylists = async bearerToken => {
  try {
    const response = await axios.get(
      `https://teton.drumrose.io/api/playlists/`,
    );
    console.log(response.data);
    return response;
  } catch (err) {
    console.error(err);
    return {
      data: [],
    };
  }
};

/*
 * Posts a favorited track
 * */
export const favoriteTrack = async (bearerToken, appleMusicId) => {
  try {
    const response = await axios.post(
      `https://teton.drumrose.io/api/tracks/${appleMusicId}/`,
      {
        headers: {
          Authorization: `Bearer ${bearerToken}`,
        },
      }
    );
    return response;
  } catch(err) {
    console.error(err);
    return {
      data: [],
    };
  }
};


/*
 * Fetches detail route for a track
 * */
export const getTrackDetail = async (bearerToken, appleMusicId) => {
  return await axios.get(
    `https://teton.drumrose.io/api/tracks/${appleMusicId}/`,
    {
      headers: {
        Authorization: `Bearer ${bearerToken}`,
      },
    }
  );
};


/*
 * Fetches detail route for an album
 * */
export const getAlbumDetail = async (bearerToken, appleMusicId) => {
  try {
    const response = await axios.get(
      `https://teton.drumrose.io/api/albums/${appleMusicId}/`,
      {
        headers: {
          Authorization: `Bearer ${bearerToken}`,
        },
      }
    );
    return response;
  } catch(err) {
    throw new Error(err);
  }
};


/*
 * Fetches detail route for a playlist
 * */
export const getPlaylistDetail = async (bearerToken, appleMusicId) => {
  return await axios.get(
    `https://teton.drumrose.io/api/playlists/${appleMusicId}/`,
    {
      headers: {
        Authorization: `Bearer ${bearerToken}`,
      },
    }
  );
};


/*
 * Creates a playlist
 * */
export const createPlaylist = async (bearerToken, playlistData) => {
  return await axios.get(
    `https://teton.drumrose.io/api/playlists/${appleMusicId}/`,
    playlistData,
    {
      headers: {
        Authorization: `Bearer ${bearerToken}`,
      },
    },
  );
};

