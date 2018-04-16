import {combineReducers} from 'redux';
import {reducer as formReducer} from 'redux-form';
import userReducer from './Register_reducer';
import mailReducer from './Mail_reducer';
import cityListReducer from './City_list';
import login_modalReducer from './Login_Modal';
import profileReducer from './Add_Profile';
import loginReducer from './Login';
import latReducer from './Lat';
import createBoardReducer from './Create_Board';
import createSlotReducer from './Create_Slot';
import searchBoardReducer from './Search_board';
import getSlotReducer from './Get_Slot';
import lngReducer from './Lng';
const rootReducer = combineReducers({
    form:formReducer,
    user:userReducer,
    login_modal : login_modalReducer,
    mail:mailReducer,
    city_list:cityListReducer,
    profile: profileReducer,
    login:loginReducer,
    lat:latReducer,
    lng:lngReducer,
    createBoard:createBoardReducer,
    createSlot:createSlotReducer,
    searchBoard:searchBoardReducer,
    getSlot:getSlotReducer
});

export default rootReducer;
 
