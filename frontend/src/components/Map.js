import React from 'react';
import {withGoogleMap , GoogleMap , Marker ,InfoWindow } from 'react-google-maps';
import { connect } from 'react-redux';
import {lat_action} from '../actions/index';
import {lng_action} from '../actions/index';
class Map extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            lat:23.023657898587178,
            lng:72.57351636599606,
            isOpen:false
        }
    }
    onMarkerPositionChanged = (event) =>{
        console.log("lat===================", event.latLng.lat())
        console.log("lng===================", event.latLng.lng())
        this.setState({
            lat:event.latLng.lat(),
            lng:event.latLng.lng(),
            isOpen:true
        })
        // var lat_data = {
        //     lat:event.latLng.lat()
        // }
        // var lng_data = {
        //     lng:event.latLng.lng()
        // }
        // var data = {
        //     lat:event.latLng.lat(),
        //     lng:event.latLng.lng()
        // }
        // this.props.onLatLngChange(data)
        // this.props.lat_action(lat_data),
        // this.props.lng_action(lng_data)
    }
    handleToggle = () => {
        this.setState({
            isOpen: !false
        });
    }
    render() {
        const markers = this.props.markers || []
        return (
            <div>
                <GoogleMap
                    defaultZoom = {this.props.zoom}
                    defaultCenter = {this.props.center}
                >
                    
                        <Marker position={{lat : this.state.lat , lng:this.state.lng}} draggable={true} onDragEnd={this.onMarkerPositionChanged} onClick={this.handleToggle} >
                        {this.state.isOpen &&
                            <InfoWindow
                                    onCloseClick={this.handleToggle}
                                    >
                                <span>Latitude  : {this.state.lat} <br /> Longitude: {this.state.lng}</span>
                            </InfoWindow>
                        }

                        </Marker>
                    
                    
                </GoogleMap>
            </div>
        );
    }
}
function mapDispatchToProps(dispatch) {
    return {
        lat_action:lat_action,
        lng_action:lng_action
    }
}
const Map1 = connect(mapDispatchToProps)(Map)
export default withGoogleMap(Map1);