import {combineReducers} from 'redux';
import { reducer as formReducer} from 'redux-form';
import UserReducer from './Reducer'
const rootReducer = combineReducers({
    form: formReducer,
    user: UserReducer
});
export default rootReducer;