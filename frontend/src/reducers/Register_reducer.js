import {ADD_USER} from '../actions/index';



export default function(state=[] , action){

    switch(action.type) {
        case ADD_USER:{
            console.log('inside switch====', action.result)
            
            return [action.result , ...state];
        }

        default:
            return state;
    }
}