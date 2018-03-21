import React, {Component} from 'react';


export default class UserList extends Component {
    state = {
        list :[]
      };
      async componentDidMount(){
        try{
          const res = await fetch('http://localhost:8000/list/',{mode :'cors'});
          
          
          const list = await res.json();
          
          this.setState({
            list
          });
        }catch(e){
          console.log(e);
        }
      }
      render(){
          return (
                <div>
                    {this.state.list.map(item => (
                        <div key={item.id}>
                       
                        
                        
                        <h4>username: {item.username} </h4>
                        <h4>email: {item.email} </h4>
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