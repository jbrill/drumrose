import axios from 'axios';

export const getUserDetail = async (bearerToken, userHandle) => {
  try {
    const response = await axios.get(
      `https://teton.drumrose.io/api/users/${userHandle}`,
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

export const getFavoritedTracks = async bearerToken => {
  try {
    const response = await axios.get('https://teton.drumrose.io/api/favorites/tracks/', {
      headers: {
        Authorization: `Bearer ${bearerToken}`,
      },
    });
    return response;
  } catch (err) {
    console.error(err);
    return {
      data: [],
    };
  }
};

export const getFavoritedAlbums = async bearerToken => {
  try {
    const response = await axios.get('https://teton.drumrose.io/api/favorites/albums/', {
      headers: {
        Authorization: `Bearer ${bearerToken}`,
      },
    });
    return response;
  } catch (err) {
    console.error(err);
    return {
      data: [],
    };
  }
};

export const getFavoritedPlaylists = async bearerToken => {
  try {
    const response = await axios.get('https://teton.drumrose.io/api/favorites/playlists/', {
      headers: {
        Authorization: `Bearer ${bearerToken}`,
      },
    });
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
    console.log(response.data)
    return response;
  } catch (err) {
    console.error(err);
    return {
      data: [],
    };
  }
};
