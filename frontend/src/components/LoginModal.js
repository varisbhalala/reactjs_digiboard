import React from 'react';
import Dialog from 'material-ui/Dialog';
import FlatButton from 'material-ui/FlatButton';
import RaisedButton from 'material-ui/RaisedButton';
import { connect } from 'react-redux';

/**
 * A modal dialog can only be closed by selecting one of the actions.
 */
export class LoginModal extends React.Component {
  state = {
    open: false,
  };

  handleOpen = () => {
    this.setState({open: true});
  };

  handleClose = () => {
    this.setState({open: false});
  };
  
  render() {
    const actions = [
      <FlatButton
        label="Cancel"
        primary={true}
        onClick={this.handleClose}
      />,
      <FlatButton
        label="Submit"
        primary={true}
        disabled={true}
        onClick={this.handleClose}
      />,
    ];

    return (
      <div>
        <RaisedButton label="Modal Dialog" onClick={this.handleOpen} />
        <Dialog
          title="Dialog With Actions"
          actions={actions}
          modal={true}
          open={this.state.open}
        >
          Only actions can close this dialog.
        </Dialog>
        { this.state.open = this.props.login_modal.map((res) => res.open ) }
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  console.log("state change ======================" , state.login_modal)
  
  return {
      login_modal : state.login_modal
      
  }
}


const Login_1 = connect(mapStateToProps ,)(LoginModal);
export default Login_1;