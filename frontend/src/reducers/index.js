import {combineReducers} from 'redux';
import {reducer as formReducer} from 'redux-form';
import userReducer from './Register_reducer';
import mailReducer from './Mail_reducer';
import cityListReducer from './City_list';
import profileReducer from './Add_Profile';
import loginReducer from './Login';
const rootReducer = combineReducers({
    form:formReducer,
    user:userReducer,
    mail:mailReducer,
    city_list:cityListReducer,
    profile: profileReducer,
    login:loginReducer
});

export default rootReducer;
 
