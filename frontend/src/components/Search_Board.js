import React from 'react';
import SelectField from 'material-ui/SelectField';
import MenuItem from 'material-ui/MenuItem';
import {city_list} from '../actions/index';
import { connect } from 'react-redux';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
export class Search_Board extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            city_disabled:true,
            city_disabled_text:"Plese select state first",
            state_list_fetch:[],
            value:null,
            value1:null,
        }
    }
    componentWillMount(){
        fetch("http://localhost:8000/state/")
        .then( (response) => {
            return response.json()
        })
        .then( (json) => {
            console.log("state--------" , json)
            this.setState({state_list_fetch: json})
        })
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
    render(){
        return (
            <div>
                <h1> Search Board </h1>
                <MuiThemeProvider muiTheme={getMuiTheme()} >
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
                </MuiThemeProvider>
            </div>
        );
    }
}

const mapStateToProps = (state) => {
    return {
        city:state.city_list,
    }
}
const mapDispatchToProps =(dispatch) => {
    return {
        city_list : city_list
    }
}
export default connect(mapStateToProps , mapDispatchToProps)(Search_Board);