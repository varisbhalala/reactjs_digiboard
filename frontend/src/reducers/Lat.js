import {LAT} from '../actions/index';



export default function(state=[] , action){
    console.log("reducer")
    switch(action.type) {
        case LAT:{
            console.log('inside switch====', action.data)
            
            return action.data;
        }

        default:
            return state;
    }
}