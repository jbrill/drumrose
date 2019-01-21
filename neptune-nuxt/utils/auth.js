import jwtDecode from "jwt-decode";
import Cookie from "js-cookie";
import jwt from "jsonwebtoken";
import config from "~/config.json";
import fs from "fs";

const getQueryParams = () => {
  const params = {};
  window.location.href.replace(
    /([^(?|#)=&]+)(=([^&]*))?/g,
    ($0, $1, $2, $3) => {
      params[$1] = $3;
    }
  );
  return params;
};

export const extractInfoFromHash = () => {
  if (process.server) return;
  const { id_token, state } = getQueryParams();
  return {
    token: id_token,
    secret: state
  };
};

export const getDecodedJWT = jwt => {
  return JSON.stringify(jwtDecode(jwt));
};

export const setStorage = (token, identifier) => {
  if (process.client) {
    window.localStorage.setItem(identifier, token);
  } else {
    Cookie.set(identifier, token);
  }
};

export const getFromCookie = identifier => {
  if (process.client) return;
  return Cookie.get(identifier);
};

export const getFromLocalStorage = identifier => {
  if (process.server) return;
  return window.localStorage.identifier;
};

export const unsetAll = () => {
  if (process.server) {
    Object.keys(Cookies.get()).forEach(function(cookieName) {
      var neededAttributes = {
        // Here you pass the same attributes that were used when the cookie was created
        // and are required when removing the cookie
      };
      Cookies.remove(cookieName, neededAttributes);
    });
  } else {
    window.localStorage.removeItem("token");
    window.localStorage.removeItem("user");
    window.localStorage.removeItem("secret");
    window.localStorage.setItem("logout", Date.now());
  }
};

export const getUserFromCookie = req => {
  if (!req.headers.cookie) return;
  const jwtCookie = req.headers.cookie
    .split(";")
    .find(c => c.trim().startsWith("jwt="));
  if (!jwtCookie) return;
  const jwt = jwtCookie.split("=")[1];
  console.log(jwtDecode(jwt));
  return jwtDecode(jwt);
};

export const getUserFromLocalStorage = () => {
  const json = window.localStorage.user;
  return json ? JSON.parse(json) : undefined;
};

export const setSecret = secret =>
  window.localStorage.setItem("secret", secret);

export const checkSecret = secret => window.localStorage.secret === secret;

export const getAppleMusicToken = () => {
  if (process.client) return;
  var privateKey = fs.readFileSync("./utils/AuthKey_T3K3M873XH.p8").toString();
  const teamId = config.APPLE_MUSIC_TEAM_ID;
  const keyId = config.APPLE_MUSIC_KEY_ID;
  return jwt.sign({}, privateKey, {
    algorithm: "ES256",
    expiresIn: "180d",
    issuer: teamId,
    header: {
      alg: "ES256",
      kid: keyId
    }
  });
};
