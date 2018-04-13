import {LOGIN_MODAL} from '../actions/index';



export default function(state=[] , action){

    switch(action.type) {
        case LOGIN_MODAL:{
            console.log('inside switch====', action.result)
            
            return action.result;
        }

        default:
            return state;
    }
}