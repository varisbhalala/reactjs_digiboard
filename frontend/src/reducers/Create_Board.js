import {CREATE_BOARD} from '../actions/index';



export default function(state=[] , action){

    switch(action.type) {
        case CREATE_BOARD:{
            console.log('inside switch====', action.result)
            
            return action.result;
        }

        default:
            return state;
    }
}