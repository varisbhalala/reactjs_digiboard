import {ADD_USER} from '../actions/action';


export default function(state=[] , action){
    switch(action.type) {
        case ADD_USER : {
            return [action.payload.data, ...state];
        }
    }
}