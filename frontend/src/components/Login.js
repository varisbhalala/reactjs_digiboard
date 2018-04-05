import React from 'react';
import {Field , reduxForm} from 'redux-form';
import {login} from '../actions/index';
import RaisedButton from 'material-ui/RaisedButton';
import {connect} from 'react-redux';
import TextField from 'material-ui/TextField';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
const renderTextField = ({
    input,
    label,
    meta: {touched, error},
    ...custom
}) => (
    <TextField 
        hintText={label}
        floatingLabelText={label}
        errorText={touched && error}
        {...input}
        {...custom}
    />
)

export class Login extends React.Component {
    constructor(props) {
        super(props);
        this.state = { 
            username : "",
            password : ""
        }
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit = (event,values) => {
        event.preventDefault();
        console.log(values);
        var data = {
            username:this.username.value,
            password:this.password.value,
        }
        console.log(this.username.value);
        this.props.login(data);
        // return addUser(data);
        // fetch('http://localhost:8000/list/', {
        //     method:'POST',
        //     headers:{'Content-Type' : 'application/json'},
        //     body: data
        // })
    }
    render(){
        return(
        <div>
            <MuiThemeProvider muiTheme={getMuiTheme()}>
            <form onSubmit={this.handleSubmit}>
            <div>
            <Field 
                name="username"
                ref={(input) => {this.username = input;}}
                component={renderTextField}
                label="user name"
            />
            </div>
            <div>
            <Field 
                name="password"
                ref={(input) => {this.password = input;}}
                component={renderTextField}
                label="password"
                type="password"
            />
            </div>
            <RaisedButton 
            type="submit"
            label="Submit"
            />
            </form>
            </MuiThemeProvider>
            <div>
                
                {this.props.login_result}
            </div>
        </div>
        );
    }
}

const mapStateToProps = (state) => {

    return {
        
        login_result: state.login
    }
}
function mapDispatchToProps(dispatch){
    return {
        login :login
    }
}

const Login1 = connect(mapStateToProps,mapDispatchToProps)(Login);
export default reduxForm({
    form:'Login',
    
})(Login1);