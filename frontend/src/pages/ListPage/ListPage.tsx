import React from "react";
import { getUsers } from "../../api";
import { UserList } from "../../components";

import styles from "./ListPage.module.css";

class ListPage extends React.Component {
  state = {
    users: {},
    count: {},
    podium: {},
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

// TODO TYPES
type Props = {
  count: any;
  podium: any;
  users: any;
};

type State = {
  count: any;
  podium: any;
  users: any;
  selectedUser: string;
};
