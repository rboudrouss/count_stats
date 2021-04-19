import React from "react";
import { getUsers } from "../../api";
import { Loading, UserList } from "../../components";
import { User } from "../../types"

import styles from "./ListPage.module.css";

class ListPage extends React.Component {
  state: { users: User[], loading: boolean } = {
    users: [],
    loading: true,
  };

  async componentDidMount() {
    const users = await getUsers();
    this.setState({ users, loading: false });
  }

  render() {
    const { users, loading } = this.state
    return (
      <div className={styles.container}>
        {
          loading
            ?
            <Loading loading={loading} />
            :
            <UserList users={users} />
        }
      </div>
    );
  }
}

export default ListPage;
