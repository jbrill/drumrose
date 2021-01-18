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
 * Fetches all playlists
 * */
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
 * Fetches all albums
 * */
export const getAlbums = async () => {
  return await axios.get(
    `https://teton.drumrose.io/api/albums/`,
  );
};

/*
 * Fetches all tracks
 * */
export const getTracks = async bearerToken => {
  try {
    const response = await axios.get(
      `https://teton.drumrose.io/api/tracks/`,
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
 * Posts a favorited track
 * */
export const favoriteTrack = async (bearerToken, trackData) => {
  return await axios.post(
    `https://teton.drumrose.io/api/favorites/tracks/`,
    trackData,
    {
      headers: {
        Authorization: `${bearerToken}`,
      },
    }
  );
};


/*
 * Posts a favorited track
 * */
export const favoriteAlbum = async (bearerToken, albumData) => {
  return await axios.post(
    `https://teton.drumrose.io/api/favorites/albums/`,
    albumData,
    {
      headers: {
        Authorization: `${bearerToken}`,
      },
    }
  );
};


/*
 * Posts a favorited track
 * */
export const favoritePlaylist = async (bearerToken, playlistData) => {
  return await axios.post(
    `https://teton.drumrose.io/api/favorites/playlists/`,
    playlistData,
    {
      headers: {
        Authorization: `${bearerToken}`,
      },
    }
  );
};


/*
 * Fetches detail route for a track
 * */
export const getTrackDetail = async (bearerToken, appleMusicId) => {
  return await axios.get(
    `https://teton.drumrose.io/api/tracks/${appleMusicId}/`,
    {
      headers: {
        Authorization: `${bearerToken}`,
      },
    }
  );
};


/*
 * Fetches detail route for an album
 * */
export const getAlbumDetail = async (bearerToken, appleMusicId) => {
  return await axios.get(
    `https://teton.drumrose.io/api/albums/${appleMusicId}/`,
    {
      headers: {
        Authorization: `${bearerToken}`,
      },
    }
  );
};


/*
 * Fetches detail route for a playlist
 * */
export const getPlaylistDetail = async (bearerToken, appleMusicId) => {
  return await axios.get(
    `https://teton.drumrose.io/api/playlists/${appleMusicId}/`,
    {
      headers: {
        Authorization: `${bearerToken}`,
      },
    }
  );
};


/*
 * Creates a playlist
 * */
export const createPlaylist = async (bearerToken, playlistData) => {
  return await axios.post(
    `https://teton.drumrose.io/api/playlists/`,
    playlistData,
    {
      headers: {
        Authorization: `${bearerToken}`,
      },
    },
  );
};


/*
 * Creates an album
 * */
export const createAlbum = async (bearerToken, albumData) => {
  return await axios.post(
    `https://teton.drumrose.io/api/albums/`,
    albumData,
    {
      headers: {
        Authorization: `${bearerToken}`,
      },
    },
  );
};

/*
 * Creates a track
 * */
export const createTrack = async (bearerToken, trackData) => {
  console.log(bearerToken)
  return await axios.post(
    `https://teton.drumrose.io/api/tracks/`,
    trackData,
    {
      headers: {
        Authorization: `${bearerToken}`,
      },
    },
  );
};
