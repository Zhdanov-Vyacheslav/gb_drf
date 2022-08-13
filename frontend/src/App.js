import React from "react";

import axios from "axios";

import UserList from './components/UserList';
import Menu from "./components/Menu";
import Footer from "./components/Footer";

class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
        'users': [],
        'menu': [
            {'href': 'http://localhost:3000', 'name':'Home'},
            {'href': 'http://localhost:3000', 'name': '1'},
            {'href': 'http://localhost:3000', 'name': '2'},
            {'href': 'http://localhost:3000', 'name': '3'},
        ]
    }
  }

  componentDidMount() {
    axios
        .get('http://localhost:8000/api/users/')
        .then(response => {
            const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
        })
        .catch(error => console.log(error))
  }

    render() {
     return(
         <html>
         <body>
         <div>
             <Menu menu={this.state.menu} />
             <UserList users = {this.state.users} />
         </div>
         </body>
         <Footer />
         </html>
     )
  }
}

export default App;
