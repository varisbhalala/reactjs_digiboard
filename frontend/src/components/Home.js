import React from 'react';
import {Link} from 'react-router-dom'
export default class Home extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            role : "",
            publisher : false,
            advertiser : false
        }
    }
    componentWillMount(){
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
            console.log('id json------' , json.role),
            this.setState({'publisher_id' : json.role})
            if( json.role == 'p') {
                this.setState({
                    publisher : true , advertiser : false
                })
            }
            if( json.role == 'a') {
                this.setState({
                    publisher : false , advertiser : true
                })
            }
        })
    }
    render(){
        return (
            <div>
                { this.state.publisher && 
                    <div>
                        <p>Welcome publisher </p>
                        <Link to="create_board/" > Create Board </Link>
                        <Link to="create_slot/" > Create Slot </Link>
                    </div>
                }
                {this.state.advertiser &&
                    <div>
                        <p>Welcome Advertiser </p>
                        <Link to="search_board/" > Search Board </Link>
                    </div>    
                }
            </div>
        );
    }
}