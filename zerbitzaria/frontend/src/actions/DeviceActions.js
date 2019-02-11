import { GET_DEVICES } from './Types';

export function getDevices() {
  return function (dispatch) {
    dispatch({
      type : GET_DEVICES,
      payload : [{title: "test", id : 1, text : "test text"}]
    });
  }
}
