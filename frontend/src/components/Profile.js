import React from 'react';


export class Profile extends React.Component {
    componentWillMount(){
        this.setState({
            user: this.props.user
        })
    }
    render() {
        return (
            <div>
                <h1> Profile </h1>
                <h2> {console.log("asdasdasdasd======",this.state)}</h2>
            </div>
            
        );
    }
}
export default Profile;