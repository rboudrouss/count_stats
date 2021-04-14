import React from "react";
import styles from "./UserList.module.css";

import { User } from "../../types"
import UserCard from "../UserCard/UserCard";

const UserList = (props: { users: User[] }) => {
  if (!props.users) {
    return <h1>loading...</h1>;
  }
  var { users } = props;
  return (
    <div className={styles.container}>
      {users.map((user: User, i: number) =>
        <UserCard
          key={i}
          user={user}
          className={styles.card}
        />
      )}
    </div>
  );
};

export default UserList;
