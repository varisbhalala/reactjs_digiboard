import React from 'react';
import Register from '../containers/Register';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
class Register_comp extends React.Component {
    render(){
        return (
            <div>
                <MuiThemeProvider muiTheme={getMuiTheme()}>

                    <Register />
                </MuiThemeProvider>
            </div>
        );
    }
}
export default Register_comp