import axios from 'axios';
import {store} from '../index';


export const ADD_USER = 'add_user';



export function addUser_status(result){
    // console.log("adduser====",result)
    return {
        type :ADD_USER,
        result
    }
}


export function addUser(data) {
    console.log(data);
    axios.post("http://localhost:8000/list/", data)
    
    .then(result => {
        // console.log("result====", result.data);
        // return {
        //     type:ADD_USER,
        //     payload: result
        // }
        store.dispatch(addUser_status(result.data));
        
    });
}