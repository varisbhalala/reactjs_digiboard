import {GET_SLOT} from '../actions/index';

export default function(state=[] , action) {
    switch(action.type) {
        case GET_SLOT:{
            console.log("inside switch==============" , action.result)
            return action.result
        } 
        default:
            return state;
    }
}