import React from "react";
import styles from "./app.module.css";
import { ThemeProvider } from "@material-ui/styles";
import theme from "./theme";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import { MainPage, ListPage, UserPage } from "./pages";
import { TopBar, Footer } from "./components";

class App extends React.Component {
  render() {
    return (
      <ThemeProvider theme={theme}>
        <Router>
          <TopBar />
          <Switch>
            <Route exact path="/">
              <MainPage />
            </Route>
            <Route path="/list">
              <ListPage />
            </Route>
            <Route path="/user/:id">
              <UserPage />
            </Route>
          </Switch>
          <Footer />
        </Router>
      </ThemeProvider>
    );
  }
}

export default App;
