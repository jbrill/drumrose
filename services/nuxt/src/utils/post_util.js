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

async function getTrackHintResponseFromQuery(query, config) {
  const getTrackHint_URL =
    APPLE_API_URL + "search/hints?term=" + query + "&limit=10&types=songs";
  const trackHintResponse = await axios.get(getTrackHint_URL, config);
  return trackHintResponse;
}

async function getTrackInfoResponseFromAppleID(appleID, config) {
  const getTrackInfo_URL = APPLE_API_URL + "songs/" + appleID;
  const trackInfoResponse = await axios.get(getTrackInfo_URL, config);
  return trackInfoResponse;
}

async function getTrackIDResponseFromQuery(query, config) {
  const getTrackID_URL =
    APPLE_API_URL + "search?term=" + query + "&limit=2&types=songs";
  const trackIDResponse = await axios.get(getTrackID_URL, config);
  return trackIDResponse;
}

export const getTrackHintsFromQuery = async (query, bearerToken) => {
  const trackIDResponse = await getTrackIDResponseFromQuery(
    query.replace(" ", "+"),
    getConfig(bearerToken)
  );
  return trackIDResponse.data.results.songs.data;
};

export const getTrackIDFromQuery = async (query, bearerToken) => {
  const trackIDResponse = await getTrackIDResponseFromQuery(
    query.replace(" ", "+"),
    getConfig(bearerToken)
  );
  return trackIDResponse.data.results.songs.data[0];
};

export const getPosts = async bearerToken => {
  try {
    const posts = await axios.get("https://teton.drumrose.io/api/posts/", {
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

export const createPost = async (
  bearerToken,
  appleSongID,
  caption,
  userHandle
) => {
  try {
    const posts = await axios.post(
      "https://teton.drumrose.io/api/posts/",
      {
        apple_music_id: appleSongID,
        handle: userHandle,
        caption: caption
      },
      {
        headers: {
          Authorization: "Bearer " + bearerToken
        }
      }
    );
    return posts;
  } catch (err) {
    console.error(err);
    return {
      data: []
    };
  }
};

async function getTrackInfo(trackId, bearerToken) {
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
}

export const parsePosts = async (posts, musicToken) => {
  let parsedPosts = [];
  for (let post of posts) {
    const track_info = await getTrackInfo(post.song.apple_music_id, musicToken);
    console.log(track_info);
    const postStructure = {
      track: track_info,
      user: post.user,
      caption: post.caption
    };
    if (track_info) parsedPosts.push(postStructure);
  }
  return parsedPosts;
};
