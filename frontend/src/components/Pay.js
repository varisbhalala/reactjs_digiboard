import React from 'react'
import {StripeProvider} from 'react-stripe-elements';
import MyStoreCheckout from './MyStoreCheckout'
import StripeCheckout from 'react-stripe-checkout';
// export default class Pay extends React.Component {
//     render(){
//         return (
//             <div>
//                 {/* <StripeProvider apiKey="pk_test_enNicNlRowtFPMduyPyeyeGw">
//                     <MyStoreCheckout />
//                 </StripeProvider> */}
//             </div>
        
//         )
//     }
// }

export default class TakeMoney extends React.Component {
    onToken = (token) => {
      fetch('/save-stripe-token', {
        method: 'POST',
        body: JSON.stringify(token),
      }).then(response => {
        response.json().then(data => {
          alert(`We are in business, ${data.email}`);
        });
      });
    }
   
    // ...
   
    render() {
      return (
        // ...
        <StripeCheckout
          token={this.onToken}
          amount={3000}
          currency="INR"
          stripeKey="pk_test_enNicNlRowtFPMduyPyeyeGw"
        />
      )
    }
  }
  