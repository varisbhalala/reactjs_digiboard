import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import {BrowserRouter, Switch , Route, Link} from 'react-router-dom';
import Register_comp from './components/index';
import {Provider} from 'react-redux';
import {createStore, applyMiddleware } from 'redux';
import rootReducer from './reducers/index';
import ReduxPromise from 'redux-promise';
import thunk from 'redux-thunk';
import Confirm_mail from './components/Confirm_mail'
export const store = createStore(
    rootReducer,
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__(),
    applyMiddleware(thunk)
);

// const createStoreWithMiddleware = applyMiddleware(ReduxPromise)(createStore);
ReactDOM.render(
    <Provider store={store} >
        <BrowserRouter>
            <Switch>
                <Route path="/register" component={Register_comp} />
                <Route path="/confirm_mail" component={Confirm_mail} />
            </Switch>
        </BrowserRouter>
    </Provider>
    
    ,document.getElementById('root'));

