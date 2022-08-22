import React from "react";
import axios from "axios";

import {BrowserRouter, Route, Routes} from "react-router-dom";

import UserList from './components/UserList';
import ProjectList from './components/ProjectList';
import NoteList from './components/NoteList';
import Menu from "./components/Menu";
import Footer from "./components/Footer";

class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
        'users': [],
        'projects':[],
        'notes':[],
        'menu': [
            {'href': '/', 'name':'Home'},
            {'href': '/users', 'name': 'Users'},
            {'href': '/projects', 'name': 'Projects'},
            {'href': '/notes', 'name': 'Notes'},
        ]
    }
  }

  componentDidMount() {
    axios
        .get('http://localhost:8000/api/users/')
        .then(response => {
            const users = response.data.results
                this.setState(
                    {
                        'users': users
                    }
                )
        })
        .catch(error => console.log(error))
      axios
        .get('http://localhost:8000/api/projects/')
        .then(response => {
            const projects = response.data.results
                this.setState(
                    {
                        'projects': projects
                    }
                )
        })
        .catch(error => console.log(error))
      axios
        .get('http://localhost:8000/api/notes/')
        .then(response => {
            const notes = response.data.results
                this.setState(
                    {
                        'notes': notes
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
             <BrowserRouter>
                 <Menu menu = {this.state.menu} />
                 <Routes>
                     <Route exact path='/users' element={<UserList users = {this.state.users} />} />
                     <Route exact path='/projects' element={<ProjectList projects={this.state.projects} />} />
                     <Route exact path='/notes' element={<NoteList notes={this.state.notes} />} />
                 </Routes>
             </BrowserRouter>
         </div>
         </body>
         <Footer />
         </html>
     )
  }
}

export default App;
