import React from 'react';
import {Field , reduxForm} from 'redux-form'
import TextField from 'material-ui/TextField'
import {RadioButton , RadioButtonGroup} from 'material-ui/RadioButton';
import {addUser} from '../actions/action';
import { connect } from 'react-redux';




const validate = values => {
    const errors = {}
    const requiredFields = [
      'role',
      'username',
      'email',
      'password',
      'token'
    ]
    requiredFields.forEach(field => {
      if (!values[field]) {
        errors[field] = 'Required'
      }
    })
    if (
      values.email &&
      !/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(values.email)
    ) {
      errors.email = 'Invalid email address'
    }
    return errors
}

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

export class Login extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            role : "",
            username : "",
            email : "",
            token : ""
        }
    }
    
    render(){
        const {  pristine ,reset , submitting} = this.props
        this.handleSubmit = (event) => {
            var data = {
                
                role: this.props.role,
                username: this.props.username,
                email: this.props.email,
                token: this.props.token
            }
            console.log(this.props.role);
            this.props.addUser(data);
        }
        return (
        <form onSubmit={this.handleSubmit}>
        
        <div>
            <Field 
                name='role'
                component={renderRadioGroup}>
                <RadioButton value="publisher" label="publisher" />
                <RadioButton value="advertiser" label="advertiser" />
                </Field>
        </div>
        <div>
            <Field 
                name="email"
                component={renderTextField}
                label="email"
                type="email"
            />
        </div>
        <div>
            <Field 
                name="username"
                component={renderTextField}
                label="user name"
            />
        </div>
        <div>
            <Field 
                name="token"
                component={renderTextField}
                label="token"
            />
        </div>
        <div>
            <Field 
                name="password"
                component={renderTextField}
                label="password"
                type="password"
            />
        </div>
        <div>
        <button type="submit" >
          Submit
        </button>
        <button type="button" disabled={pristine || submitting} onClick={reset}>
          Clear Values
        </button>
        </div>
        
        </form>
    );
}
}
const mapStateToProps = (state) => {
    return {
        user : state.user
    }
}
function mapDispatchToProps(dispatch) {
    return{
        addUser : addUser
    }
}
export default connect(mapStateToProps,mapDispatchToProps)(Login);
