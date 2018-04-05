import React from 'react';
import {connect} from 'react-redux';
import TextField from 'material-ui/TextField';
import {Field , reduxForm} from 'redux-form';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import RaisedButton from 'material-ui/RaisedButton'; 
import SelectField from 'material-ui/SelectField';
import MenuItem from 'material-ui/MenuItem';
import {city_list} from '../actions/index';
import {addProfile_action} from '../actions/index';
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

export class Profile extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            state_list_fetch: [],
            value:null,
            value1:null,
            name:"",
            contact:"",
            avatar:"",
            company_name:"",
            company_address: "",
            city:"",
            state:"",
            role:"",
            user:""
        }
        this.handleChange = this.handleChange.bind(this);
        this.handleChangeCity = this.handleChangeCity.bind(this);
        // this.handleClick = this.handleClick.bind(this);
    }
    
    componentDidMount(){
        // this.props.state_list()
        fetch("http://localhost:8000/state")
        .then( (response) => {
            return response.json()
        })
        .then( (json) => {
            this.setState({state_list_fetch: json})
        })
        
    }
    handleChange = (event,value,index) => {
        event.preventDefault();
        value = value+1
        
        this.setState({value,state_name:value});
        console.log("value===",{value})
        console.log("index==", index)
        var data = {
            state_index : index
        }
        this.props.city_list(data);
    }
    handleChangeCity = (event,value1,index) => {
        // event.preventDefault();
        
        value1 = value1+1
        console.log("value city===",{value1})
        console.log("city index" , index)
        
        this.setState({value1:index});
    }
    fileSelectHendler = (event) => {
        event.preventDefault()
        console.log(event.target.files[0]);
        this.setState({
            selectedFile : event.target.files[0]
        })
    }
    handleSubmit = (event, value) => {
        event.preventDefault()
        const fd = new FormData();
        fd.set('avatar' , this.state.selectedFile , this.state.selectedFile.name); 
        const role1 = this.props.mail.map( (mail) => mail.user.role)
        const user1 = this.props.mail.map( (mail) => mail.user.id)
        fd.set('name',this.name.value);
        fd.set('contact',this.contact_no.value);
        fd.set('company_name',this.company_name.value);
        fd.set('company_address' , this.company_address.value);
        fd.set('city' , this.state.value1);
        fd.set('state' , this.state.value);
        fd.set('role' , role1);
        fd.set('user' , user1);

        // var data = {
        //     name:this.name.value,
        //     contact:this.contact_no.value,
        //     avatar:this.state.selectedFile,
        //     company_name:this.company_name.value,
        //     company_address: this.company_address.value,
        //     city:this.state.value1,
        //     state:this.state.state_name,
        //     role:role1[0],
        //     user:user1[0]
        // }
        this.props.addProfile_action(fd);
    }
    render() {
        return (
            <div>
                <h1> Profile </h1>
                {/* { this.state.state_list_fetch.map((state_list_fetch) => state_list_fetch.name)} */}
                <h2> {console.log("asdasdasdasd======",this.props.mail.map( (mail) => mail.user.role))}</h2>
                <h3>Role: {this.props.mail.map((mail) => mail.user.role)}</h3>
                <MuiThemeProvider muiTheme={getMuiTheme()}>
                <form onSubmit={this.handleSubmit}>
                    <div>
                        <Field 
                            name="name"
                            ref={(input) => {this.name = input;}}
                            component={renderTextField}
                            label="Name"
                            type="text"
                        />
                    </div>
                    <div>
                        <Field 
                            name="contact_no"
                            ref={(input) => {this.contact_no = input;}}
                            component={renderTextField}
                            label="Contact Number"
                            type="number"
                        />
                    </div>
                    {/* <div>
                        <Field 
                            name="avatar"
                            ref={(input) => {this.name = input;}}
                            component={renderTextField}
                            label="Profile Image"
                            type="file"
                        />
                    </div> */}
                    <br />
                    <br />
                    <div>
                        <RaisedButton 
                            type="file"
                            name="avatar"
                            
                            
                            component={renderTextField}
                            
                            >
                            <input type="file" ref={(input) => {this.avatar = input;}} name="avatar" onChange={this.fileSelectHendler} />
                        </RaisedButton>
                    </div>
                  <br />
                  <br />
                  <br />
                    <div>
                        <Field 
                            name="company_name"
                            ref={(input) => {this.company_name = input;}}
                            component={renderTextField}
                            label="Company_name"
                        />
                    </div>
                    <div>
                        <Field 
                            name="company_address"
                            ref={(input) => {this.company_address = input;}}
                            component={renderTextField}
                            label="Address"
                        />
                    </div>
                    {/* <div>
                        <Field 
                            name="city"
                            ref={(input) => {this.name = input;}}
                            component={renderTextField}
                            label="City"
                        />
                    </div>
                    <div>
                        <Field 
                            name="state"
                            ref={(input) => {this.name = input;}}
                            component={renderTextField}
                            label="State"
                        />
                    </div> */}
                    <div>
                        <SelectField
                            value={this.state.value}
                            ref={(input) => {this.state_list_input = input;}}
                            name="state_list_input"
                            const 
                            // onChange={this.handleChange}
                            floatingLabelText="Select State"
                            onChange={this.handleChange}
                            floatingLabelStyle={{color: 'blue'}}
                            >
                            {this.state.state_list_fetch.map((state_list_fetch) => <MenuItem key={state_list_fetch.id} value={state_list_fetch.id} primaryText={state_list_fetch.name} />)}
                            {/* {this.state.state_list_fetch.map((state_list_fetch) => state_list_fetch.name)} */}
                        </SelectField>
                    </div>

                    <div>
                        <SelectField
                            value={this.state.value1}
                            ref={(input) => {this.city_list_input = input;}}
                            name="city_list_input"
                            floatingLabelText="Select city"
                            onChange={this.handleChangeCity.bind(this)}
                            floatingLabelStyle={{color: 'blue'}}
                            >
                            {console.log("city value===" , this.state.value1)}
                            {this.props.city.map((city) => <MenuItem key={city.id} value={city.name} primaryText={city.name} />)}
                           
                        </SelectField>
                    </div>
                    <div>
                        <RaisedButton 
                            type="submit"
                            label="Submit"
                        />
                    </div>
                </form>
                    
                </MuiThemeProvider>
                { this.props.profile && this.props.profile.map( (res) => res.result)}
            </div>
            
        );
    }
}

const mapStateToProps = (state) => {
    return {
        mail:state.mail,
        city:state.city_list,
        profile : state.profile
    }
}
function mapDispatchToProps(dispatch){
    return {
        city_list:city_list,
        addProfile_action : addProfile_action
    }
}
// export default connect(mapStateToProps,null)(Profile);
const Profile_1 = connect(mapStateToProps,mapDispatchToProps)(Profile);
export default reduxForm({
    form:'Profile',
    
})(Profile_1);