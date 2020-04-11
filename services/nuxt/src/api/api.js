export const getUserDetail = async (bearerToken, userHandle) => {
  const userInfo = await axios.get(`https://teton.drumrose.io/api/users/${userHandle}`, {
    headers: {
      Authorization: 'Bearer ' + bearerToken,
    },
  });
  return userInfo;
};
