import React from 'react';
import {connect} from 'react-redux';
import RaisedButton from 'material-ui/RaisedButton'; 
import SelectField from 'material-ui/SelectField';
import MenuItem from 'material-ui/MenuItem';
import TextField from 'material-ui/TextField';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import {Field , reduxForm} from 'redux-form';
import {city_list} from '../actions/index';
import {create_board_action} from '../actions/index';
import Set_Auth_Token from '../actions/Set_Auth_Token';
import Map from './Map';
import '../css/map.css'
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
export class Create_Board extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            state_list_fetch:[],
            value:null,
            value1:null,
            lat:"",
            lng:"",
            street:"",
            area:"",
            city:"",
            state:"",
            LatLng:"",
            role:"",
            user:"",
            publisher_id:"",
            city_disabled:true,
            city_disabled_text:"Plese select state first"
        }
        this.handleChange = this.handleChange.bind(this);
        this.handleChangeCity = this.handleChangeCity.bind(this);
       
    }
    handleChange = (event,value,index) => {
        event.preventDefault();
        value = value+1
        console.log("value===",value)
        console.log("index==", index)
        this.setState({index,state_name:index});
        this.setState({city_disabled:false})
        this.setState({city_disabled_text:"Select City"})
        
        var data = {
            state_index : value
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
   
    componentWillMount(){
        // const user1 = this.props.mail.map( (mail) => mail.user.id)
        // console.log("id=====---------" , user1);
       console.log("token=============" , localStorage.jwtToken)
        fetch("http://localhost:8000/id_api/" ,{
            headers: {
                Authorization : 'Bearer ' + localStorage.jwtToken
            }
        })
        .then((response) => {
            console.log('response id============' , response)
            return response.json()
        })
        .then((json) => {
            console.log('id json------' , json.publisher_id),
            this.setState({'publisher_id' : json.publisher_id})
        })
        // this.props.state_list()
        fetch("http://localhost:8000/state/")
        .then( (response) => {
            return response.json()
        })
        .then( (json) => {
            console.log("state--------" , json)
            this.setState({state_list_fetch: json})
        })
    }
    handleLatLngChange = (latlngValue) => {
        console.log("value===" , latlngValue)
        this.setState({
            LatLng : latlngValue
        })
        console.log("state" , this.state.LatLng)
    }
    handleSubmit = (event,values) => {
        event.preventDefault();
        
        var data = {
            
            lat:this.lat.value,
            lng:this.lng.value,
            street:this.street.value,
            area:this.area.value,
            city:this.state.value1,
            state:this.state.index,
            publisher:this.state.publisher_id
        }
        console.log("submit----------------" ,this.props.profile.map( (res) => res.publisher_id) )
        this.props.create_board_action(data);
        // return addUser(data);
        // fetch('http://localhost:8000/list/', {
        //     method:'POST',
        //     headers:{'Content-Type' : 'application/json'},
        //     body: data
        // })
    }
    render(props) {
        return (
            <div>
                {/* <GoogleMap 
                    defaultZoom={11}
                    defaultCenter={{lat: 22.205 , lng:37.55}}
                >
                {props.isMarkerShown=true && <Marker position={{lat: 22.20565456 , lng:37.5566577}} />}
                </GoogleMap> */}
                <div className="map">
                <Map
                    center={{lat : 23.023657898587178 , lng:72.57351636599606}} 
                    zoom={13}
                    
                    onLatLngChange={this.handleLatLngChange}
                    containerElement={ <div style = {{height: 100 + '%'}} />} 
                    mapElement={<div style = {{height: 100 + '%'}} /> } 
                />
                </div>
                <MuiThemeProvider muiTheme={getMuiTheme()}>
                    <form onSubmit={this.handleSubmit}>
                    <div>
                        <Field 
                            name="lat"
                            ref={(input) => {this.lat = input;}}
                            component={renderTextField}
                            label="Latitude"
                            type="text"
                            

                        />
                    </div>
                    <div>
                        <Field 
                            name="lng"
                            ref={(input) => {this.lng = input;}}
                            component={renderTextField}
                            label="Longitude"
                            type="text"
                            
                        />
                    </div>
                    <div>
                        <Field 
                            name="street"
                            ref={(input) => {this.street = input;}}
                            component={renderTextField}
                            label="Street"
                            type="text"
                        />
                    </div>
                    <div>
                        <Field 
                            name="area"
                            ref={(input) => {this.area = input;}}
                            component={renderTextField}
                            label="Area"
                            type="text"
                        />
                    </div>
                    <div>
                        <SelectField
                            value={this.state.index}
                            ref={(input) => {this.state_list_input = input;}}
                            name="state_list_input"
                             
                            // onChange={this.handleChange}
                            floatingLabelText="Select State"
                            onChange={this.handleChange}
                            floatingLabelStyle={{color: 'blue'}}
                            >
                            {this.state.state_list_fetch.map((state_list) => <MenuItem key={state_list.id} value={state_list.name} primaryText={state_list.name} />)}
                            {/* {this.state.state_list_fetch.map((state_list_fetch) => state_list_fetch.name)} */}
                        </SelectField>
                    </div>

                    <div>
                        <SelectField
                            disabled={this.state.city_disabled}
                            value={this.state.value1}
                            ref={(input) => {this.city_list_input = input;}}
                            name="city_list_input"
                            floatingLabelText={this.state.city_disabled_text}
                            onChange={this.handleChangeCity.bind(this)}
                            floatingLabelStyle={{color: 'blue'}}
                            >
                            {console.log("city value===" , this.state.index)}
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
                { this.props.createBoard}
            </div>
        );
    }
}
const mapStateToProps = (state) => {
    return {
        profile : state.profile,
        city:state.city_list,
        // lat_data:lat,
        // lng_data:lng
        mail:state.mail,
        createBoard: state.createBoard
    }

}
function mapDispatchToProps(dispatch){
    return {
        city_list:city_list,
        create_board_action:create_board_action
    }
}
const Create_Board1 = connect(mapStateToProps,mapDispatchToProps)(Create_Board);
// const mapStateToProps = (state) => {
//     return {
//         profile : state.profile
//     }
// }
export default reduxForm({
    form:"react-board"
})(Create_Board1);