
import React from "react";
import styles from "./UserPage.module.css";
import { TopBar } from "../../components"
import { User } from "../../types"
import { getUsers } from "../../api";

class UserPage extends React.Component {
  state: { id: string, users: User[] } = {
    id: (this.props as any).match.params.id as string, // HACK
    users: []
  }

  async componentDidMount() {
    const users = await getUsers();
    this.setState({ users });
  }

  constructor(props: {}) {
    super(props);
  }


  render() {
    const { users, id } = this.state;
    var exits = false;
    for (const user of users) {
      if (user.user_id === id) {
        exits = true;
      }
    }
    return (
      <div className={styles.container}>
        <TopBar />
      </div>
    );
  }
}

export default UserPage;
