import React from "react";
import styles from "./UserList.module.css";
import CountUp from "react-countup";

import UserCard from "../UserCard/UserCard";

const UserList = (props: Props) => {
  if (!props.users) {
    return <h1>loading...</h1>;
  }
  var { users } = props;
  return (
    <div className={styles.container}>
      {users.map((user: any, i: number) => {
        <UserCard
          key={i}
          user={user.name}
          top={user.top} // FIXME
          className={styles.card}
        />

      })}
    </div>
  );
};

export default UserList;

type Props = {
  users: any;
};
