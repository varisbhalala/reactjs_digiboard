import {combineReducers} from 'redux';
import {reducer as formReducer} from 'redux-form';
import userReducer from './Register_reducer';
import mailReducer from './Mail_reducer';

const rootReducer = combineReducers({
    form:formReducer,
    user:userReducer,
    mail:mailReducer
});

export default rootReducer;
 
