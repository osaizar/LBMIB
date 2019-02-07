import { BASE_URL, GET_USER, LOGIN_USER, LOGOUT_USER} from './Types';

export function getUser(token) {
  return function (dispatch) {
    fetch(BASE_URL+"/ajax/get_curr_user", {
      method: 'GET',
      headers : {
        'token' : token
      }
    })
      .then(response => // Try to parse the response
        response.json().then(json => ({
          status: response.status,
          json
        })
      ))
      .then(
        ({status, json}) => {
          if (status != 200){ // status is not good
            const user = {"token" : "", "username" : ""};
            localStorage.setItem("token", undefined);
            dispatch({ //TODO: create errors
              type : GET_USER,
              payload : user
            });
          }else{
            const user = {"token" : json.token, "username" : json.username};
            localStorage.setItem("token", json.token);
            dispatch({
              type : GET_USER,
              payload : user
            });
          }
        },
        err => { // TODO: create errors
          console.log("Fatal Error "+JSON.stringify(err));
        }
      );
  }
}

export function loginUser(postData) {
  return function (dispatch) {
    // Send login details, get token
    fetch(BASE_URL+"/ajax/login", {
      method: 'POST',
      headers : {
        'content-type' : 'application/json'
      },
      body : JSON.stringify(postData)
    })
      .then(response => // Try to parse the response
        response.json().then(json => ({
          status: response.status,
          json
        })
      ))
      .then(
        ({status, json}) => {
          if (status != 200){ // status is not good
            dispatch({ //TODO: create errors
              type : LOGIN_USER,
              payload : ""
            });
          }else{
            const user = {"token" : json.token, "username" : ""};
            localStorage.setItem("token", json.token)
            dispatch({
              type : LOGIN_USER,
              payload : user
            });
          }
        },
        err => { // TODO: create errors
          console.log("Fatal Error "+JSON.stringify(err));
        }
      );
  }
}

export function logoutUser(token) {
  return function (dispatch) {
    fetch(BASE_URL+"/ajax/logout", {
      method: 'GET',
      headers : {
        'token' : token
      }
    })
      .then(response => // Try to parse the response
        response.json().then(json => ({
          status: response.status,
          json
        })
      ))
      .then(
        ({status, json}) => {
          const user = {"token" : "", "username" : ""};
          localStorage.setItem("token", undefined);
        },
        err => { // TODO: create errors
          console.log("Fatal Error "+JSON.stringify(err));
        }
      );
  }
}
