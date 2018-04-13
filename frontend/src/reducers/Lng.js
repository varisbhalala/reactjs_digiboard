import {LNG} from '../actions/index';



export default function(state=[] , action){

    switch(action.type) {
        case LNG:{
            console.log('inside switch====', action.data)
            
            return action.data;
        }

        default:
            return state;
    }
}