export const getUserDetail = async (bearerToken, userHandle) => {
  const userInfo = await axios.get(
    `http://django-server:8000/users/${userHandle}`,
    {
      headers: {
        Authorization: "Bearer " + bearerToken
      }
    }
  );
  return userInfo;
};
