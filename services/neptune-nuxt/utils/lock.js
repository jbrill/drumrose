import { setSecret } from "./auth";

import uuid from "uuid";

export const getBaseUrl = () =>
  `${window.location.protocol}//${window.location.host}`;
