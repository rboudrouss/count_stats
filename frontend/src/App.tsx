import React from "react";
import styles from "./app.module.css";
import { ThemeProvider } from '@material-ui/styles';
import theme from "./theme"
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";

import { MainPage, ListPage, UserPage } from "./pages";
import { TopBar } from "./components";

class App extends React.Component {
  render() {
    return (
      <ThemeProvider theme={theme}>
        <TopBar />
        <Router>
          <Switch>
            <Route exact path="/" component={MainPage} />
            <Route path="/list" component={ListPage} />
            <Route path="/user/:id" component={UserPage} />
          </Switch>
        </Router>
      </ThemeProvider>
    );
  }
}

export default App;
