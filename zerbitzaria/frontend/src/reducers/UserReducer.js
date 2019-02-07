import { GET_USER, LOGIN_USER, LOGOUT_USER} from '../actions/Types';

const initialState ={
  user : {
    token : "",
    usename : ""
  }
}

export default function(state = initialState, action){
  switch (action.type) {
    case GET_USER:
      return {
        ...state,
        user : action.payload
      }
    case LOGIN_USER:
      return {
        ...state,
        user : action.payload
      }
    case LOGOUT_USER:
      return{
        ...state,
        user : action.payload
      }
    default:
      return state;
  }
}
