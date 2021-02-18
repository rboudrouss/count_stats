import React from "react";
// import './App.css';
import styles from "./app.module.css";

import { count, users, history, podium, last_update} from "./api/";
import { Cards, Chart, UserPicker } from "./components";

class App extends React.Component {
  state = {
    count,
    users,
    history,
    last_update,
    podium
  }

  render() {
    const {podium, users, last_update} = this.state
    return (
      <div className={styles.container}>
        <Cards podium={podium} users={users} lastUpdate={last_update}/>
        <Chart />
        <UserPicker />
      </div>
    );
  }
}

export default App;
