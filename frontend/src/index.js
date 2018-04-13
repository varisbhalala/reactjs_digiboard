import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import {Router, Switch , Route} from 'react-router-dom';
import Register_comp from './components/index';
import {Provider} from 'react-redux';
import {createStore, applyMiddleware } from 'redux';
import rootReducer from './reducers/index';
import thunk from 'redux-thunk';
import Profile from './components/Profile'
import Confirm_mail from './components/Confirm_mail'
import Login from './components/Login'
import Confirm_mail_withoutKey from './components/Confirm_mail_withoutKey'
import Create_Board from './components/Create_Board'
import Create_Slot from './components/Create_Slot'
import history from './history'
import Home from './components/Home'
import Search_Board from './components/Search_Board'
export const store = createStore(
    rootReducer,
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__(),
    applyMiddleware(thunk)
);



// const createStoreWithMiddleware = applyMiddleware(ReduxPromise)(createStore);
ReactDOM.render(
    <Provider store={store} >
        <Router history={history}>
            <Switch>
                <Route path="/register" component={Register_comp} />
                <Route path="/confirmMail/:key" component={Confirm_mail} />
                <Route path="/confirmMail/" component={Confirm_mail_withoutKey} />
                <Route path="/profile" component={Profile} />
                <Route path="/login" component={Login} />
                <Route path="/create_board" component={Create_Board} />
                <Route path="/create_slot" component={Create_Slot} />
                <Route path="/home" component={Home} />
                <Route path="/search_board" component={Search_Board} />
            </Switch>
        </Router>
    </Provider>
    
    ,document.getElementById('root'));

