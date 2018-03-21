import React from 'react';
import ReactDOM from 'react-dom';
import { Provider} from 'react-redux';
import {Values} from 'redux-form-website-template';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
// import store from './store';
import showResults from './showResults';
import Login from './Login';
import { create } from 'domain';
import rootReducer from '../Reducers/Central_reducer';
import thunk from 'redux-thunk';
import {createStore} from 'redux';
import {applyMiddleware} from 'redux';


export const store = createStore(
    rootReducer,
    applyMiddleware(thunk)
);


export class Register extends React.Component {
    render () {
        return (
            <Provider store={store}>
                <MuiThemeProvider muiTheme={getMuiTheme()}>
                    <div style={{padding: 15}}>
                        <h2> Register </h2>
                        <Login onSubmit={showResults} />
                        <Values form='Login' />
                    </div>
                </MuiThemeProvider>
            </Provider> 
        );
    }
}
export default Register;