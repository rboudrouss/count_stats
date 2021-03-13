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
    selectedUser: "",
  };
  
  constructor(props: any) {
    super(props);
    this.selectedUserChange = this.selectedUserChange.bind(this);
  }

  async componentDidMount() {
    const { podium, count } = await getCount();
    const users = await getUsers();
    this.setState({ podium, count, users });
    console.log(users);
  }

  async selectedUserChange(selectedUser: string) {
    this.setState({ selectedUser: selectedUser });
  }

  render() {
    const { podium, count, users, selectedUser } = this.state;
    return (
      <div className={styles.container}>
        <Cards podium={podium} count={count} users={users} />
        <UserPicker
          users={users}
          selectedUserChange={this.selectedUserChange}
        />
        <Chart selectedUser={selectedUser}/>
      </div>
    );
  }
}

export default App;
