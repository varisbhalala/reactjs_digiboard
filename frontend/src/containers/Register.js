import React from 'react';
import {Field , reduxForm} from 'redux-form';
import {addUser} from '../actions/index';
import FlatButton from 'material-ui/FlatButton';
import {connect} from 'react-redux';
import TextField from 'material-ui/TextField';
import {RadioButtonGroup , RadioButton} from 'material-ui/RadioButton';


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
const renderRadioGroup = ({input, ...rest}) => (
    <RadioButtonGroup
        {...input}
        {...rest}
        valueSelected={input.value}
        onChange={(event, value) => input.onChange(value)}
    />
)

function randomString(){
    var text = "";
    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

  for (var i = 0; i < 32; i++)
    text += possible.charAt(Math.floor(Math.random() * possible.length));

  return text;
}
export class Register extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            role: "",
            username: "",
            email: "",
            token: "",
            password: "",
            userData : ""
        }
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    
    handleSubmit = (event,values) => {
        event.preventDefault();
        console.log(values);
        var data = {
            role:this.role.value,
            username:this.username.value,
            email:this.email.value,
            token:randomString(),
            password:this.password.value,
        }
        console.log(this.username.value);
        this.props.addUser(data);
        // return addUser(data);
        // fetch('http://localhost:8000/list/', {
        //     method:'POST',
        //     headers:{'Content-Type' : 'application/json'},
        //     body: data
        // })
    }
    
    render(){
        // const {fields: {username,role,password,email,token}, handleSubmit} =this.props;
        return (
            <div>
            <form onSubmit={this.handleSubmit}>
                {/* <div>
                    <Field name="role" ref={(input) => {this.role = input;}} component="input" value={this.state.role} type="text" placeholder="role"/>
                </div>
                <div>
                    <Field name="username" ref={(input) => {this.username = input;}} component="input" type="text" placeholder="username"/>
                </div>
                <div>
                    <Field name="email" component="input" ref={(input) => {this.email = input;}} type="email" placeholder="email"/>
                </div>
                <div>
                    <Field name="password" component="input" ref={(input) => {this.password = input;}} type="password" placeholder="password"/>
                </div>
                <div>
                    <Field name="token" ref={(input) => {this.token = input;}} component="input" type="text" placeholder="token"/>
                </div>
                <div>
                    <button type="submit">submit </button>
                </div> */}
                <div>
            <Field 
                name='role'
                ref={(input) => {this.role = input;}}
                component={renderRadioGroup}>
                <RadioButton value="p" label="publisher" />
                <RadioButton value="a" label="advertiser" />
                </Field>
        </div>
        <div>
            <Field 
                name="email"
                ref={(input) => {this.email = input;}}
                component={renderTextField}
                label="email"
                type="email"
            />
        </div>
        <div>
            <Field 
                name="username"
                ref={(input) => {this.username = input;}}
                component={renderTextField}
                label="user name"
            />
        </div>
        {/* <div>
            <Field 
                name="token"
                ref={(input) => {this.token = input;}}
                component={renderTextField}
                label="token"
            />
        </div> */}
        <div>
            <Field 
                name="password"
                ref={(input) => {this.password = input;}}
                component={renderTextField}
                label="password"
                type="password"
            />
        </div>
        <div>
        {/* <button type="submit" >
          Submit
        </button> */}
       <FlatButton 
            type="submit"
            label="Submit"
        />
          
        </div>
        
            </form>
            <div>
                {console.log('result',this.props.userData[0])}
                { this.props.userData && this.props.userData.map( (user) => user.result)}
            </div>
            </div>                           
        );
    }
}

const mapStateToProps = (state) => {
    console.log("user result ==========>>>>" ,state.user[0]);    
    return {
        
        userData: state.user
    }
}
function mapDispatchToProps(dispatch){
    return {
        addUser :addUser
    }
}

const Register_1 = connect(mapStateToProps,mapDispatchToProps)(Register);
export default reduxForm({
    form:'Register',
    
})(Register_1);