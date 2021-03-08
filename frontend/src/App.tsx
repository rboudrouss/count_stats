import React from "react";
// import './App.css';
import styles from "./app.module.css";

import { getCount, getUsers } from "./api";
import { Cards, Chart, UserPicker } from "./components";

class App extends React.Component {
  state = {
    count: {},
    podium: {},
    users: {},
  };

  async componentDidMount() {
    const { podium, count } = await getCount();
    const users = await getUsers();
    this.setState({ podium, count, users });
  }

  render() {
    const { podium, count, users } = this.state;
    return (
      <div className={styles.container}>
        <Cards podium={podium} count={count} users={users} />
        <Chart />
        <UserPicker />
      </div>
    );
  }
}

export default App;
