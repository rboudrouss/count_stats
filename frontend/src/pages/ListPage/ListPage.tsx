import React from "react";
import { getUsers } from "../../api";
import { UserList } from "../../components";
import { User } from "../../types"

import styles from "./ListPage.module.css";

class ListPage extends React.Component {
  state: { users: User[] } = {
    users: [],
  };

  async componentDidMount() {
    const users = await getUsers();
    this.setState({ users });
  }

  render() {
    const { users } = this.state
    return <div className={styles.container}>
      <UserList users={users} />
    </div>;
  }
}

export default ListPage;
