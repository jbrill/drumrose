import { setSecret } from "./auth";

import uuid from "uuid";

const getLock = options => {
  const config = require("~/config.json");
  const Auth0Lock = require("auth0-lock").default;
  return new Auth0Lock(
    config.AUTH0_CLIENT_ID,
    config.AUTH0_CLIENT_DOMAIN,
    options
  );
};

const getBaseUrl = () => `${window.location.protocol}//${window.location.host}`;

const getOptions = container => {
  const secret = uuid.v4();
  setSecret(secret);
  return {
    closable: true,
    auth: {
      responseType: "token id_token",
      redirectUrl: `${getBaseUrl()}/auth/signed-in`,
      params: {
        scope: "openid profile email",
        state: secret
      }
    },
    theme: {
      primaryColor: "#772CE6"
    },
    languageDictionary: {
      emailInputPlaceholder: "something@youremail.com",
      title: "Neptune"
    },
    allowedConnections: ["Username-Password-Authentication"]
  };
};

export const showLogin = container => getLock(getOptions(container)).show();
export const logout = () => getLock().logout({ returnTo: getBaseUrl() });
