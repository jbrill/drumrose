import axios from 'axios';


/*
 * Fetches reviews
 * */
export const getTrackReviews = async bearerToken => {
  try {
    const response = await axios.get(
      `${process.env.baseUrl}/api/reviews/tracks/`,
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
export const getTrackReview = async bearerToken => {
  try {
    const response = await axios.get(
      `${process.env.baseUrl}/api/reviews/tracks/<track_id>/`,
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
      `${process.env.baseUrl}/api/followers/${userHandle}/`,
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
 * Add follower
 * */
export const addFollower = async (bearerToken, data) => {
  try {
    const response = await axios.post(
      `${process.env.baseUrl}/api/followers/`,
      data,
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
 * Patch user (i.e. add follower, change username)
 * */
export const patchUserDetail = async (bearerToken, userHandle, data) => {
  try {
    const response = await axios.patch(
      `${process.env.baseUrl}/api/users/${userHandle}/`,
      data,
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
      `${process.env.baseUrl}/api/users/${userHandle}/`,
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
      `${process.env.baseUrl}/api/users/`,
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
 * Post track review
 * */
export const reviewTrack = async (bearerToken, data) => {
  return await axios.post(
    `${process.env.baseUrl}/api/reviews/tracks/`,
    data,
    {
      headers: {
        Authorization: `${bearerToken}`,
      },
    }
  );
};

/* 
 * Update track review
 * */
export const updateTrackReview = async (bearerToken, data) => {
  return await axios.put(
    `${process.env.baseUrl}/api/reviews/tracks/`,
    data,
    {
      headers: {
        Authorization: `${bearerToken}`,
      },
    }
  );
};

/* 
 * Post album review
 * */
export const reviewAlbum = async (bearerToken, data) => {
  return await axios.post(
    `${process.env.baseUrl}/api/reviews/albums/`,
    data,
    {
      headers: {
        Authorization: `${bearerToken}`,
      },
    }
  );
};


/* 
 * Post album review
 * */
export const reviewPlaylist = async (bearerToken, data) => {
  return await axios.post(
    `${process.env.baseUrl}/api/reviews/playlists/`,
    data,
    {
      headers: {
        Authorization: `${bearerToken}`,
      },
    }
  );
};

/* 
 * Fetches a list of favorite tracks
 * */
export const getFavoritedTracks = async bearerToken => {
  try {
    const response = await axios.get(
      `${process.env.baseUrl}/api/favorites/tracks/`,
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
 * Fetches a list of reviews for specific track
 * */
export const getTrackDetailedReviews = async (bearerToken, trackId) => {
  try {
    const response = await axios.get(
      `${process.env.baseUrl}/api/reviews/tracks/${trackId}`,
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
      `${process.env.baseUrl}/api/playlists/`,
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
    `${process.env.baseUrl}/api/albums/`,
  );
};

/*
 * Fetches all tracks
 * */
export const getTracks = async bearerToken => {
  try {
    const response = await axios.get(
      `${process.env.baseUrl}/api/tracks/`,
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
    `${process.env.baseUrl}/api/favorites/tracks/`,
    trackData,
    {
      headers: {
        Authorization: `${bearerToken}`,
      },
    }
  );
};


/*
 * Deletes a favorited track
 * */
export const unFavoriteTrack = async (bearerToken, trackId) => {
  return await axios.delete(
    `${process.env.baseUrl}/api/favorites/tracks/${trackId}/`,
    {
      headers: {
        Authorization: `${bearerToken}`,
      },
    }
  );
};

/*
 * Deletes a favorited album
 * */
export const unFavoriteAlbum = async (bearerToken, albumId) => {
  return await axios.delete(
    `${process.env.baseUrl}/api/favorites/albums/${albumId}/`,
    {
      headers: {
        Authorization: `${bearerToken}`,
      },
    }
  );
};


/*
 * Deletes a favorited playlist
 * */
export const unFavoritePlaylist = async (bearerToken, playlistId) => {
  return await axios.delete(
    `${process.env.baseUrl}/api/favorites/playlists/${playlistId}/`,
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
    `${process.env.baseUrl}/api/favorites/albums/`,
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
    `${process.env.baseUrl}/api/favorites/playlists/`,
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
    `${process.env.baseUrl}/api/tracks/${appleMusicId}/`,
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
    `${process.env.baseUrl}/api/albums/${appleMusicId}/`,
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
    `${process.env.baseUrl}/api/playlists/${appleMusicId}/`,
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
    `${process.env.baseUrl}/api/playlists/`,
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
    `${process.env.baseUrl}/api/albums/`,
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
  return await axios.post(
    `${process.env.baseUrl}/api/tracks/`,
    trackData,
    {
      headers: {
        Authorization: `${bearerToken}`,
      },
    },
  );
};
