import axios from 'axios';

const getUserDetail = async function (bearerToken, userHandle) {
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

export default getUserDetail;
