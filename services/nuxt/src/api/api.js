import axios from 'axios';

export const getUserDetail = async function (bearerToken, userHandle) {
  const userInfo = await axios.get(
    `https://teton.drumrose.io/api/users/${userHandle}`,
    {
      headers: {
        Authorization: `Bearer ${bearerToken}`,
      },
    }
  );
  return userInfo;
};

export const getPlaylists = async function() {
  const response = await axios.get(
    `https://teton.drumrose.io/api/playlists/`,
  );
  console.log("RESPONSE")
  console.log(response.data)
  return response;
}
