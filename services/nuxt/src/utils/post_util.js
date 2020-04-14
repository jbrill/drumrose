import axios from 'axios';

const appleApiUrl = 'https://api.music.apple.com/v1/catalog/us/';

function getConfig (bearerToken) {
  const bearer = {
    Authorization: `Bearer ${bearerToken}`,
  };
  const config = {
    headers: bearer,
    params: {},
  };
  return config;
}

async function getTrackHintResponseFromQuery (query, config) {
  const getTrackHintUrl = `${appleApiUrl}search/\
    hints?term=${query}&limit=10&types=songs`;
  const trackHintResponse = await axios.get(getTrackHintUrl, config);
  return trackHintResponse;
}

async function getTrackInfoResponseFromAppleID (appleID, config) {
  const getTrackInfoUrl = `${appleApiUrl}songs/${appleID}`;
  const trackInfoResponse = await axios.get(getTrackInfoUrl, config);
  return trackInfoResponse;
}

async function getTrackIDResponseFromQuery (query, config) {
  const getTrackIdUrl = `${appleApiUrl}search?term=\
    ${query}&limit=2&types=songs`;
  const trackIDResponse = await axios.get(getTrackIdUrl, config);
  return trackIDResponse;
}

export const getTrackHintsFromQuery = async (query, bearerToken) => {
  const trackIDResponse = await getTrackIDResponseFromQuery(
    query.replace(' ', '+'),
    getConfig(bearerToken)
  );
  return trackIDResponse.data.results.songs.data;
};

export const getTrackIDFromQuery = async (query, bearerToken) => {
  const trackIDResponse = await getTrackIDResponseFromQuery(
    query.replace(' ', '+'),
    getConfig(bearerToken)
  );
  return trackIDResponse.data.results.songs.data[0];
};

export const getPosts = async bearerToken => {
  try {
    const posts = await axios.get('https://teton.drumrose.io/api/posts/', {
      headers: {
        Authorization: `Bearer ${bearerToken}`,
      },
    });
    return posts;
  } catch (err) {
    console.error(err);
    return {
      data: [],
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
      'https://teton.drumrose.io/api/posts/',
      {
        apple_music_id: appleSongID,
        handle: userHandle,
        caption: caption,
      },
      {
        headers: {
          Authorization: `Bearer ${bearerToken}`,
        },
      }
    );
    return posts;
  } catch (err) {
    console.error(err);
    return {
      data: [],
    };
  }
};

async function getTrackInfo (trackId, bearerToken) {
  const appleApiTrackUrl = `${appleApiUrl}/songs/${trackId}`;
  const resp = await axios.get(appleApiTrackUrl, getConfig(bearerToken));
  const trackData = resp.data.data[0].attributes;
  return {
    track_playback: trackData,
    track_name: trackData.name,
    track_artist: trackData.artistName,
    track_cover_url: trackData.artwork.url
      .replace('{w}', '250')
      .replace('{h}', '250'),
  };
}

export const parsePosts = (posts, musicToken) => {
  const parsedPosts = [];
  posts.forEach(post => {
    const trackInfo = getTrackInfo(post.song.apple_music_id, musicToken);
    console.log(trackInfo);
    const postStructure = {
      track: trackInfo,
      user: post.user,
      caption: post.caption,
    };
    if (trackInfo) {
      parsedPosts.push(postStructure);
    }
  });
  return parsedPosts;
};
