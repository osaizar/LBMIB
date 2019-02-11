import { combineReducers } from 'redux';
import postReducer from './PostReducer';
import userReducer from './UserReducer';
import deviceReducer from './DeviceReducer';

export default combineReducers({
  posts : postReducer,
  user : userReducer,
  devices : deviceReducer
});
