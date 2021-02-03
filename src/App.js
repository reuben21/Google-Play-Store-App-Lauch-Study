import React, {Component} from "react";
import Navbar from "./Components/Navbar/Navbar";
import {BrowserRouter, Redirect, Route, Switch} from "react-router-dom";
import Questions from "./Components/Questions/Questions";
import Questions1 from "./Components/Questions/Question1/Question1";
import Questions2 from "./Components/Questions/Question2/Question2";

class App extends Component {


  render() {
    return (
        <BrowserRouter>
          <React.Fragment>
            <Navbar />
            <Switch>
              <Redirect from="/" to="/Questions" exact/>
              <Route path="/questions" component={Questions}/>
                <Route path="/question1" component={Questions1}/>
                <Route path="/question2" component={Questions2}/>
            </Switch>
          </React.Fragment>

        </BrowserRouter>
    );
  }

}




export default App;
