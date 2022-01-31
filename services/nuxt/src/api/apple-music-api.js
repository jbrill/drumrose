import axios from 'axios';

/*
 * Fetches user detail
 * */
export const getUserDetail = async (bearerToken, userHandle) => {
  try {
    const response = await axios.get(
      `${process.env.baseUrl}/api/users/${userHandle}/`,
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
      `${process.env.baseUrl}/api/favorites/`,
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
