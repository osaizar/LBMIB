import { GET_DEVICES } from '../actions/Types';

const initialState ={
  devices : []
}

export default function(state = initialState, action){
  switch (action.type) {
    case GET_DEVICES:
      return {
        ...state,
        devices : action.payload
      }
    default:
      return state;
  }
}
