import React from 'react';
import {withRouter} from 'react-router-dom';
export class Confirm_mail_withoutKey extends React.Component {
    render() {
        console.log("this props==",this.props)
        const {match} = this.props
        const key = match.params.key
        return (
            <div>
                <h1>Invalid Request </h1>
                <h3> Go to your mail id and check for url to confirm your mail id </h3>
            </div>
        );
    }
} 

export default Confirm_mail_withoutKey;