import axios from "axios";

const APPLE_API_URL = "https://api.music.apple.com/v1/catalog/us/";

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

async function getTrackInfoResponseFromAppleID(appleID, config) {
  const getTrackInfo_URL = APPLE_API_URL + "songs/" + appleID;
  const trackInfoResponse = await axios.get(getTrackInfo_URL, config);
  return trackInfoResponse;
}

async function getTrackIDResponseFromQuery(query, config) {
  const getTrackID_URL =
    APPLE_API_URL + "search?term=james+brown&limit=2&types=songs";
  const trackIDResponse = await axios.get(getTrackID_URL, config);
  console.log(trackIDResponse);
  return trackIDResponse;
}

export const getTrackIDFromQuery = async (query, bearerToken) => {
  const trackIDResponse = await getTrackIDResponseFromQuery(
    query,
    getConfig(bearerToken)
  );
  return trackIDResponse.data.results.songs.data[0];
};

export const getPosts = async bearerToken => {
  try {
    const posts = await axios.get("http://localhost:8000/posts/", {
      headers: {
        Authorization: "Bearer " + bearerToken
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
  const apple_api_url = APPLE_API_URL + "songs/" + trackId;
  const resp = await axios.get(apple_api_url, getConfig(bearerToken));
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
