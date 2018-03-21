import { createStore, combineReducers ,applyMiddleware} from 'redux';
import { reducer as reduxFormReducer } from 'redux-form';
import React from 'react';
import {thunkMiddleWare} from 'redux-thunk'
const reducer = combineReducers({
  form: reduxFormReducer, // mounted under "form"
});
const store = (window.devToolsExtension
  ? window.devToolsExtension()(createStore)
  : createStore)(reducer);  


export default store;
