import React from 'react';
import {connect} from 'react-redux';
import RaisedButton from 'material-ui/RaisedButton';
import {Field , reduxForm, Form} from 'redux-form';   
import TextField from 'material-ui/TextField';
import SelectField from 'material-ui/SelectField';
import MenuItem from 'material-ui/MenuItem';
import TimePicker from 'material-ui/TimePicker';
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
export class Create_Slot extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            value24_from:"",
            value24_to:"",
            discable_to:true,
            discable_to_text:"Plese select from first",
            board_list:"",
            is_DataFetched: false
        }
        // fetch("http://localhost:8000/id_api/" ,{
        //     headers: {
        //         Authorization : 'Bearer ' + localStorage.jwtToken
        //     }
        // })
        // .then((response) => {
        //     console.log('response id============' , response)
        //     return response.json()
        // })
        // .then((json) => {
        //     console.log('id json------' , json.publisher_id),
        //     this.setState({'publisher_id' : json.publisher_id})
        //     var payload = {
        //         "publisher_id" : json.publisher_id
        //     }    
        //     var data = new FormData()
        //     data.append('publisher_id' , json.publisher_id)
        //     fetch("http://localhost:8000/get_board_api/" , {
        //         method: "POST",
        //         body : data,
        //     })
        //     .then((response) => {
        //         console.log("board" , response)
        //         return response.json()
        //     })
        //     .then((json) => {
        //         console.log("boards--------" , json)
        //         this.setState({
        //             board_list : json , 
        //             is_DataFetched:true
        //         })
        //     })
        // })
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
            var payload = {
                "publisher_id" : json.publisher_id
            }    
            var data = new FormData()
            data.append('publisher_id' , json.publisher_id)
            fetch("http://localhost:8000/get_board_api/" , {
                method: "POST",
                body : data,
            })
            .then((response) => {
                console.log("board" , response)
                return response.json()
            })
            .then((json) => {
                console.log("boards--------" , json)
                this.setState({board_list : json})
            })
        })
        

        
    }
    handleChange_from = (event , date) => {
        this.setState({value24_from : date})
        this.setState({discable_to : false})
        this.setState({discable_to_text:"To"})

        console.log("from date--------------" , date.getTime() )
    }
    handleChange_to = (event , date) => {
        this.setState({value24_to : date})
        console.log("to date----------------" , date.getTime())
    }
    handleSubmit = (event,data) => {
        event.preventDefault()
        var from = (this.state.value24_from.getHours() * 60 * 60) + (this.state.value24_from.getMinutes() * 60)
        var to = (this.state.value24_to.getHours() * 60 * 60) + (this.state.value24_to.getMinutes() * 60)
        console.log("from time--------------------------" , (this.state.value24_from.getHours() * 60 * 60) + (this.state.value24_from.getMinutes() * 60) );
        // console.log("from to--------------------------" , ( (this.state.value24_to.getTime() - this.state.value24_from.getTime()) / 1000 ));
        console.log("from to--------------------------" , ( to - from ));
        var data = {
            _from : this.state.value24_from.getHours() + ":" + this.state.value24_from.getMinutes(),
            to : this.state.value24_to.getHours() + ":" + this.state.value24_to.getMinutes(),
            slot_price : this.slot_price.value
        }
    }
    render(){
        // if(!this.state.isDataFetched) return null;
        return (
            <div>
                <MuiThemeProvider muiThemr={getMuiTheme()} >
                <form onSubmit={this.handleSubmit}>
                    { this.state.board_list &&
                    <div>
                        <SelectField
                            value={this.state.index}
                            ref={(input) => {this.board_select = input;}}
                            name="board_select"
                             
                            // onChange={this.handleChange}
                            floatingLabelText="Select Board"
                            onChange={this.handleChange}
                            floatingLabelStyle={{color: 'silver'}}
                            >
                            {this.state.board_list.map((board) => <MenuItem key={board.id} value={board.area} primaryText={board.area} />)}
                            {/* {this.state.state_list_fetch.map((state_list_fetch) => state_list_fetch.name)} */}
                        </SelectField>
                    </div> }
                    <div>
                        <TimePicker 
                            name="_from"
                            format="24hr"
                            minutesStep={15}
                            hintText="From"
                            value={this.state.value24}
                            onChange={this.handleChange_from}
                        />
                    </div>
                    <div>
                        <TimePicker
                            disabled={this.state.discable_to} 
                            name="to"
                            format="24hr"
                            minutesStep={15}
                            hintText={this.state.discable_to_text}
                            value={this.state.value24}
                            onChange={this.handleChange_to}
                        />
                    </div>
                    <div>
                        <Field 
                            name="slot_price"
                            ref={(input) => {this.slot_price = input;}}
                            component={renderTextField}
                            label="Slot Price"
                            type="number"
                        />
                    </div>
                    <div>
                        <RaisedButton 
                            type="submit"
                            label="Submit"
                        />
                    </div>
                    </form>
                </MuiThemeProvider>
            </div>
        );
    }
}
const mapStateToProps = (state) => {
    return {

    }
}
function mapDispatchToProps(dispatch){
    return {

    }
}
const Create_Slot1 = connect(mapStateToProps , mapDispatchToProps )(Create_Slot);
export default reduxForm({
    form:"create_slot"
})(Create_Slot1);