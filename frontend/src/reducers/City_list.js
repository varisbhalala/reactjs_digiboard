import {CITY_LIST} from '../actions/index';



export default function(state=[] , action){

    switch(action.type) {
        case CITY_LIST:{
            console.log('inside switch====', action.result)
            
            return action.result;
        }

        default:
            return state;
    }
}