import axios from 'axios';
export const ADD_USER = 'add_user'

export function addUser(data){
    const request = axios.post('http://localhost:8000/list/', data);
    request.then(result => {
        console.log(result);
        return{
            type: ADD_USER,
            payload:result
        }
    });
}