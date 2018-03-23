import React from 'react';
import {Link} from 'react-router-dom';

export class Header extends React.Component {
    
    render() {
        return (
            <Link to="/register" > Register </Link>
            
        );
    }
}