import { GET_USER, LOGIN_USER } from './Types';

export function getUser() {
  return function (dispatch) {
    // Send token, get user or ""
    dispatch({
      type : GET_USER,
      payload : {
        token : "",
        username : ""
      }
    });
  }
}

export function loginUser(postData) {
  return function (dispatch) {
    // Send login details, get token
  }
}
