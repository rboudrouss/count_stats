import React from "react";
import styles from "./MainPage.module.css";

import { getUsers } from "../../api";
import { Cards, Chart, UserPicker } from "../../components";
import { User } from "../../types"

class MainPage extends React.Component {
  state: { users: User[], selectedUser: string } = {
    users: [],
    selectedUser: "",
  };

  constructor(props: {}) {
    super(props);
    this.selectedUserChange = this.selectedUserChange.bind(this);
  }

  async componentDidMount() {
    const users = await getUsers();
    this.setState({ users });
  }

  async selectedUserChange(selectedUser: string) {
    this.setState({ selectedUser: selectedUser });
  }

  render() {
    const { users, selectedUser } = this.state;
    return (
      <div className={styles.container}>
        <Cards users={users} />
        <UserPicker
          users={users}
          selectedUserChange={this.selectedUserChange}
        />
        <Chart selectedUser={selectedUser} />
      </div>
    );
  }
}

export default MainPage;
