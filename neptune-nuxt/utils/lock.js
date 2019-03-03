import { setSecret } from "./auth";

import uuid from "uuid";
import config from "~/config.json";
import auth0 from "auth0-js";

export const getBaseUrl = () =>
  `${window.location.protocol}//${window.location.host}`;
