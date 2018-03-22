import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Register_comp from './components/index';
import {Provider} from 'react-redux';
import {createStore, applyMiddleware } from 'redux';
import rootReducer from './reducers/index';
import ReduxPromise from 'redux-promise';
import thunk from 'redux-thunk';
export const store = createStore(
    rootReducer,
    applyMiddleware(thunk)
);

// const createStoreWithMiddleware = applyMiddleware(ReduxPromise)(createStore);
ReactDOM.render(
    <Provider store={store} >
        <Register_comp />
    </Provider>
    
    ,document.getElementById('root'));

