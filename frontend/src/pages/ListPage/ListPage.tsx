import React from "react";
import { getCount, getUsers } from "../../api";
import { UserList } from "../../components";

import styles from "./ListPage.module.css";

class ListPage extends React.Component {
  state = {
    users: {},
    count: {},
    podium: {},
  };

  async componentDidMount() {
    const { podium, count } = await getCount();
    const users = await getUsers();
    this.setState({ podium, count, users });
    console.log(users);
  }

  render() {
    const {count, users, podium } = this.state
    return <div className={styles.container}>
      <UserList count={count} users={users} podium={podium}/>
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
