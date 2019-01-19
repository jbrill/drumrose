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

export const setToken = token => {
  if (process.server) return;
  window.localStorage.setItem("token", token);
  console.log("TOKEN...");
  console.log(token);
  window.localStorage.setItem("user", JSON.stringify(jwtDecode(token)));
  Cookie.set("jwt", token);
};

export const unsetToken = () => {
  if (process.server) return;
  window.localStorage.removeItem("token");
  window.localStorage.removeItem("user");
  window.localStorage.removeItem("secret");
  Cookie.remove("jwt");
  window.localStorage.setItem("logout", Date.now());
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
  if (!process.server) return;
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
