import axios from "axios";

function getConfig(bearerToken) {
  const bearer = {
    Authorization: `Bearer ${bearerToken}`
  };
  const config = {
    headers: bearer,
    params: {}
  };
  return config;
}

async function getPlayback(musicId, config) {
  const apple_api_url =
    "https://api.music.apple.com/v1/catalog/us/songs/" + musicId;
  const apple_resp = await axios.get(apple_api_url, config);
  console.log("here...");
  return apple_resp;
}

export const getPosts = async bearerToken => {
  try {
    console.log(bearerToken);
    const posts = await axios.get("http://localhost:8000/posts/", {
      headers: {
        Authorization: "Bearer " + bearerToken //the token is a variable which holds the token
      }
    });
    return posts;
  } catch (err) {
    console.error(err);
    return {
      data: []
    };
  }
};

export const getTrackInfo = async (trackId, bearerToken) => {
  const config = getConfig(bearerToken);
  const apple_api_url = `https://api.music.apple.com/v1/catalog/us/songs/${trackId}`;
  const resp = await axios.get(apple_api_url, config);
  const track_data = resp.data.data[0].attributes;
  return {
    track_playback: track_data,
    track_name: track_data.name,
    track_artist: track_data.artistName,
    track_cover_url: track_data.artwork.url
      .replace("{w}", "250")
      .replace("{h}", "250")
  };
};
