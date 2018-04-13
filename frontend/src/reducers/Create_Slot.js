import {CREATE_SLOT} from '../actions/index';



export default function(state=[] , action){

    switch(action.type) {
        case CREATE_SLOT:{
            console.log('inside switch====', action.result)
            
            return action.result;
        }

        default:
            return state;
    }
}