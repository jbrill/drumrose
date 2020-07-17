import axios from 'axios';


/*
 * Fetches user detail
 * */
export const getUserDetail = async (bearerToken, userHandle) => {
  try {
    const response = await axios.get(
      `https://teton.drumrose.io/api/users/${userHandle}/`,
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
      { headers: {
          Authorization: `${bearerToken}`,
      }}
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
