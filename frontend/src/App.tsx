import React from "react";
import styles from "./app.module.css";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";

import { MainPage, ListPage, UserPage } from "./pages";
import { getCount, getUsers } from "./api";

class App extends React.Component {
  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/" component={MainPage} />
          <Route path="/list" component={ListPage} />
          <Route path="/user" component={UserPage} />
        </Switch>
      </Router>
    );
  }
}

export default App;
