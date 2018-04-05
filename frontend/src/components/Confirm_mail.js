import React from 'react';
import {Link} from 'react-router-dom';
import {confirmMail} from '../actions/index';
import {connect} from 'react-redux';

export class Confirm_mail extends React.Component {
    componentWillMount(){
        const {match} = this.props
        const key = match.params.key
        console.log(">>>>>>>>>>>>>>>>>",key);
        this.props.confirmMail({key:key})
    }
    render() {
        // console.log("this props==",this.props)
       
        
        return (
            <div>
                
                {console.log('result',this.props.mail[0])}
                { this.props.mail && this.props.mail.map( (mail) => mail.result)}
                    <br />
                    <br />
                <div >{this.props.mail ? <Link to="/profile">Profile</Link> : null}  </div>
            </div>
        );
    }
} 
const mapStateToProps = (state) => {
    return {
        mail:state.mail
    }
}
function mapDispatchToProps(dispatch) {
    return {
        confirmMail : confirmMail
    }
}


export default connect(mapStateToProps,mapDispatchToProps)(Confirm_mail);