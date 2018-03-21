import React, {Component} from "react";
import { BrowserRouter , Route ,Link ,withRouter} from "react-router-dom";

export class Header extends Component {
    render(){
        return(
            <div>
            <Link to="/login">Login</Link>    
            <Link to="/board">Board</Link>
            <Link to="/user"> User</Link>
            </div>
        );
    }
}
export default withRouter(Header);