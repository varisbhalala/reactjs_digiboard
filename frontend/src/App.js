import React, { Component } from 'react';
// import logo from './logo.svg';
import {GoogleApiWrapper , Map ,Marker} from 'google-maps-react'
import { relative } from 'path';
import Board from './components/Board'
import UserList from './components/UserList';
import Register from './components/Register';
import  { Header } from './components/Header';
import { BrowserRouter ,Switch , Route ,Link} from "react-router-dom";
class App extends Component {

  render() {
    
    return (
      <div className="App">
     
      <BrowserRouter>
      <div>
      <Header />
      
        <Switch>
        <Route path='/login' component={Register} />
        <Route path='/board' component={Board} />
        <Route path='/user' component={UserList} />
        </Switch>
        </div>
        </BrowserRouter>

      </div>
    );
  }
}

export default App;