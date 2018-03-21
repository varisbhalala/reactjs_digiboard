import React, { Component } from 'react';
// import logo from './logo.svg';
import {GoogleApiWrapper , Map ,Marker} from 'google-maps-react'
import { relative } from 'path';
import '../App.css';
// const get_board_api = [
//   {
//       "id": 24,
//       "lat": "23.02697559",
//       "lng": "72.56047010",
//       "street": "law",
//       "area": "amba",
//       "city": "Ahmedabad",
//       "state": "Gujarat",
//       "created_at": "2018-03-07T11:15:55.476747Z",
//       "updated_at": "2018-03-07T11:15:55.476764Z",
//       "publisher": 5
//   },
//   {
//       "id": 25,
//       "lat": "23.01402032",
//       "lng": "72.56270170",
//       "street": "paldi",
//       "area": "paldi",
//       "city": "Ahmedabad",
//       "state": "Gujarat",
//       "created_at": "2018-03-07T11:15:55.446017Z",
//       "updated_at": "2018-03-07T11:15:55.446035Z",
//       "publisher": 5
//   }
// ]

  

class Board extends Component {
  // constructor(props){
  //   super(props);
  //   this.state = {get_board_api};
  // }
 
  state = {
    get_board_api :[]
  };
  async componentDidMount(){
    try{
      const res = await fetch('http://localhost:8000/get_board_api/',{mode :'cors'});
      
      
      const get_board_api = await res.json();
      
      this.setState({
        get_board_api
      });
    }catch(e){  
      console.log(e);
    }
  }
  render() {
    
    return (
      <div className="App">
        <h1> available boards </h1>
        {this.state.get_board_api.map(item => (
            <div key={item.id}>
              {/* <div className="map">
              <Map google={this.props.google} className="map" 
                initialCenter={{lat:item.lat , lng:item.lng}}
                zoom={14}>
                <Marker 
                  position={{lat:item.lat , lng:item.lng}}
                />
              </Map>
              </div> */}
            
              <h2>id: {item.id} </h2>
              <h4>lat: {item.lat} </h4>
              <h4>lng: {item.lng} </h4>
              <h4> street {item.street} </h4>
              <h4>Area: {item.area} </h4>
              <h4>city: {item.city} </h4>
              <h4>State: {item.state} </h4>
              <h4>Created_at: {item.created_at} </h4>
              <br />
              <br />
              <br />
              <br />
              <br />
              </div>
        ))}
      </div>
    );
  }
}

export default GoogleApiWrapper({
  apiKey: ("AIzaSyDbUZ6g-PoDIoeFQ9yp21ZzmpnwpXuaJ4I")
})(Board)