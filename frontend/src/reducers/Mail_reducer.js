import {CONFIRM_MAIL} from '../actions/index';



export default function(state=[] , action){

    switch(action.type) {
        case CONFIRM_MAIL:{
            console.log('inside switch====', action.result)
            
            return [action.result , ...state];
        }

        default:
            return state;
    }
}