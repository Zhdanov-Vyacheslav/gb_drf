import React from "react";
import axios from "axios";

import {BrowserRouter, Link, Route, Routes} from "react-router-dom";

import LoginForm from "./components/LoginForm";
import UserList from './components/UserList';
import ProjectList from './components/ProjectList';
import NoteList from './components/NoteList';
import Menu from "./components/Menu";
import Footer from "./components/Footer";

class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
        'login':[],
        'token':'',
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
  logOut(){
      localStorage.setItem("token",'')
      this.setState({"token":""}, this.getData)
  }

  obtainAuthToken(login, password){
      axios
          .post('http://localhost:8000/api-auth-token/', {"username": login, "password": password})
          .then(response  =>{
              const token = response.data.token
              localStorage.setItem("token", token)
              this.setState({"token":token},this.getData)
          })
          .catch(error => console.log(error))
  }

  isAuth(){
      return !! this.state.token
  }

  componentDidMount(){
      let token = localStorage.getItem("token")
      this.setState({"token":token}, this.getData)
  }

  getHeaders(){
      if (this.isAuth()) {
          return {"Authorization": "Token "+ this.state.token}
      }
      return {}
  }

  getData() {
      let headers = this.getHeaders()
      axios
        .get('http://localhost:8000/api/users/', {headers})
        .then(response => {
            const users = response.data.results
                this.setState(
                    {
                        'users': users
                    }
                )
        })
        .catch(error => {
            console.log(error)
            this.setState({"users":[]})
        })
      axios
        .get('http://localhost:8000/api/projects/', {headers})
        .then(response => {
            const projects = response.data.results
                this.setState(
                    {
                        'projects': projects
                    }
                )
        })
        .catch(error => {
            console.log(error)
            this.setState({"projects":[]})
        })
      axios
        .get('http://localhost:8000/api/notes/', {headers})
        .then(response => {
            const notes = response.data.results
                this.setState(
                    {
                        'notes': notes
                    }
                )
        })
        .catch(error => {
            console.log(error)
            this.setState({"notes":[]})
        })
      axios
        .get('http://localhost:8000/api/login/')
        .then(response => {
            const login = response.data.results
                this.setState(
                    {
                        'login': login
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
                 <nav>
                     <Menu menu = {this.state.menu} />
                     <li>{this.isAuth() ? <button onClick={()=>{this.logOut()}}> Logout </button> : <Link to='/login'>Login</Link>}</li>
                 </nav>
                 <Routes>
                     <Route exact path='/users' element={<UserList users = {this.state.users} />} />
                     <Route exact path='/projects' element={<ProjectList projects={this.state.projects} />} />
                     <Route exact path='/notes' element={<NoteList notes={this.state.notes} />} />
                     <Route exact path='/login' element={<LoginForm obtainAuthToken={(login, password) => this.obtainAuthToken(login, password)} />} />
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
