import React from 'react';
import SelectField from 'material-ui/SelectField';
import MenuItem from 'material-ui/MenuItem';
import {city_list} from '../actions/index';
import { connect } from 'react-redux';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import {search_board_action} from '../actions/index';
import StripeCheckout from 'react-stripe-checkout';
import {get_slot_action} from '../actions/index';
export class Search_Board extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            city_disabled:true,
            board_disabled:true,
            slot_disabled:true,
            city_disabled_text:"Plese select state first",
            board_disabled_text:"Please select state first",
            slot_disabled_text:"Please select state first",
            state_list_fetch:[],
            value:null,
            value1:null,
            board_value:null,
            slot_value:null,
            amount:""
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
        this.setState({
            city_disabled_text:"Select City",
            board_disabled_text:"Please Select City First",
            slot_disabled_text:"Please Select City First"
        })
        
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
        
        this.setState({
            value1:index,
            board_disabled:false,
            board_disabled_text:"Select Board",
            slot_disabled_text:"Please Select Board First"
        });
        var data={
            city : index,
            state : this.state.state_name
        }
        console.log("data-------------",data)
        this.props.search_board_action(data)
    }
    onToken = (token) => {
        console.log("payment token------" , token)
        fetch("http://localhost:8000/payment_api/" , {
            method:"POST",
            headers : {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body : JSON.stringify({
                price : 3000,
                total_amount : 3000,
                token : token,
                advertiser : 8,
                publisher : 11 ,
                slot : 8

            })
        })
        .then( (response) => {
            console.log(response)
            return response.json()
        })
        .then( (json) => {
            console.log("state--------" , json)
            
        })
      }
    handleChangeBoard = (event,board_value , index) => {
        board_value = board_value + 1;
        console.log("value board----" , index)
        console.log("index board----" , index)
        this.setState({
            board_value : index ,
            slot_disabled : false,
            slot_disabled_text : "Select Slot"
        })
        var data = {
            board_id : index
        }
        this.props.get_slot_action(data);
    }
    handleChangeSlot = (event , slot_value , index) => {
        slot_value = slot_value +1;
        console.log("slot value--------" , slot_value)
        console.log("slot index--------" , index)
        this.setState({
            slot_value : index
        })
    }
    render(){
        return (
            <div>
                <h1> Search Board </h1>
                <MuiThemeProvider muiTheme={getMuiTheme()} >
                <div>
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
                        <SelectField
                            disabled={this.state.board_disabled}
                            value={this.state.board_value}
                            ref={(input) => {this.board_list_input = input;}}
                            name="board_list_input"
                            floatingLabelText={this.state.board_disabled_text}
                            onChange={this.handleChangeBoard.bind(this)}
                            floatingLabelStyle={{color: 'blue'}}
                            >
                            {console.log("city value===" , this.state.index)}
                            {this.props.search_board.map((res) => <MenuItem key={res.id} value={res.id} primaryText={res.street} />)}
                            
                        </SelectField>
                    </div>
                    <div>
                        <SelectField
                            disabled={this.state.slot_disabled}
                            value={this.state.slot_value}
                            ref={(input) => {this.slot_list_input = input;}}
                            name="slot_list_input"
                            floatingLabelText={this.state.slot_disabled_text}
                            onChange={this.handleChangeSlot.bind(this)}
                            floatingLabelStyle={{color: 'blue'}}
                            >
                            {console.log("city value===" , this.state.index)}
                            { this.props.get_slot.map((res) => <MenuItem key={res.id} value={res.id} primaryText={res.from_field} />)}
                            
                        </SelectField>
                    </div>
                    </div>
                </MuiThemeProvider>
                <StripeCheckout
                    name="DigiBoard"
                    discription="Book Slot"
                    email="digiboard2030@gmail.com"
                    token={this.onToken}
                    panelLabel="Pay Money"
                    
                    amount={3000}
                    currency="INR"
                    stripeKey="pk_test_enNicNlRowtFPMduyPyeyeGw"
                    />
                
                    
{/*                        
                       <ul><li> {this.props.search_board.map( (res) => res.lat)}      </li></ul> */}
                    
                
            </div>
        );
    }
}

const mapStateToProps = (state) => {
    return {
        city:state.city_list,
        search_board : state.searchBoard,
        get_slot : state.getSlot
    }
}
const mapDispatchToProps =(dispatch) => {
    return {
        city_list : city_list,
        search_board_action : search_board_action,
        get_slot_action : get_slot_action
    }
}
export default connect(mapStateToProps , mapDispatchToProps)(Search_Board);