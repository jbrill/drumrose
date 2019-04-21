import config from "~/config.json";
import auth0 from "auth0-js";

let instance = null;

class WebAuthSingleton {
  constructor(redirectURL) {
    if (!instance) {
      instance = this;
    }

    this._type = "WebAuthSingleton";
    this.webAuth = new auth0.WebAuth({
      domain: config.AUTH0_CLIENT_DOMAIN,
      audience: config.API_AUDIENCE,
      clientID: config.AUTH0_CLIENT_ID,
      responseType: "token id_token",
      redirectUri: redirectURL,
      scope: "openid profile"
    });

    return instance;
  }

  authorize() {
    return this.webAuth.authorize();
  }

  static staticMethod() {
    return "staticMethod";
  }

  get type() {
    return this._type;
  }

  set type(value) {
    this._type = value;
  }
}

export const webAuth = new WebAuthSingleton();
// ...

// // index.js
// import SingletonModuleScopedInstance from "./SingletonModuleScopedInstance";
//
// // Instantiate
// const instance2 = new SingletonModuleScopedInstance();
// console.log(instance2.type, instance2.singletonMethod());
//
// // Time test
// console.log(instance2.time);
//
// // Getter/Setter
// instance2.type = "type updated";
// console.log(instance2.type);
//
// setTimeout(() => {
//   const instance2ReinstanciateAttempt = new SingletonModuleScopedInstance();
//   console.log(instance2ReinstanciateAttempt.time); // Return the same time
// }, 1000);
//
// // Static method
// console.log(SingletonModuleScopedInstance.staticMethod());
