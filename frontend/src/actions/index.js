import axios from 'axios';
import {store} from '../index';
import Set_Auth_Token from './Set_Auth_Token'
// import jwt_decode from 'jwt-decode';
export const ADD_USER = 'add_user';
export const CONFIRM_MAIL = 'confirm_mail';
export const CITY_LIST = 'city_list';
export const ADD_PROFILE = 'add_profile';
export const LOGIN_USER = 'login'

// var jwt = require('jwt-simple');
var jwt = require('jsonwebtoken');
export function addUser_status(result){
    // console.log("adduser====",result)
    return {
        type :ADD_USER,
        result
    }
}


export function addUser(data) {
    console.log(data);
    var data_encoded = jwt.sign(data , 'varis5519' , {expiresIn : 60 * 60})
    console.log("encoded==========================>>>>>>",data_encoded)
    axios.post("http://localhost:8000/list/", data) 
    
    .then(result => {
        // console.log("result====", result.data);
        // return {
        //     type:ADD_USER,
        //     payload: result
        // } 
        // console.log("result data" , result.data);
        // const jwt = result.data.result;
        // localStorage.setItem('jwtToken' , jwt);
        // setAuthToken(localStorage.jwtToken);
        // const data = jwt_decode(localStorage.jwtToken);
        // var payload = result.data
        // var secret_key = 'varis5519'
        // var token = jwt.encode(payload , secret_key , 'HS256')
        // console.log("token===================>",token)
        // var decoded = jwt.decode(token , secret_key , false,'HS256')
        // console.log("decoded==================>",decoded)
        // var token = jwt.sign(result.data , 'varis5519' , { expiresIn: 60 * 60 })
        // console.log("token===================>",token)
        store.dispatch(addUser_status(result.data));
        
    });
}
export function login_status(result) {
    return { 
        type: LOGIN_USER,
        result
    }
}
export function login(data) {
    console.log(data);
    
    console.log("token===================>",data)
    axios.post("http://localhost:8000/login_api/" , data)
    .then(result => {
        console.log("token]]]]]]]]0" ,result.data.token )
        // var decoded = jwt.decode(result);
        localStorage.setItem('jwtToken' , result.data.token);
        console.log("local storage---------" , localStorage.getItem('jwtToken'))
        console.log("result=?>>>>>>>>>>>>>>>>>>>>>>" , result.data.result)
        store.dispatch(login_status(result.data.result));
    })
}
export function addProfile_status(result) {
    return {
        type : ADD_PROFILE,
        result
    }
}
export function addProfile_action(data) {
    console.log("profile data", data.get("image"))
    axios.post("http://localhost:8000/profile_submit/",data, {
        headers: {
            'Content-Type' : 'multipart/form-data'
        }
    })
    .then(result => {
        console.log("profile result ======>>>>>" , result.data);
        store.dispatch(addProfile_status(result.data));
    })
    .catch(err => {
        console.log('err', err);
    })
}
export function confirmMail_status(result) {
    return{
        type:CONFIRM_MAIL,
        result
    }
}

export function confirmMail(data){
    console.log("confirm Mail====>>>>>>>>>>>>>>>>>>" , data.key);
    axios.get("http://localhost:8000/confirmMail/",{
        params: {
            key: data.key
        }
    })

    .then(result => {
        console.log(result);
        store.dispatch(confirmMail_status(result.data));
    })
}
export function city_list_result(result){
    return {
        type:CITY_LIST,
        result
    }
}
export function city_list(data){
    console.log("state_index======",data.state_index);
    axios.get("http://localhost:8000/cities/",{
        params:{
            state_index: data.state_index
        }
    })
    .then(result => {
        console.log("city action=========",result.data);
        store.dispatch(city_list_result(result.data));
    })
}
