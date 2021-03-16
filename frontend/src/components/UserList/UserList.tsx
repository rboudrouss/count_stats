import React from "react";
import styles from "./UserList.module.css";
import CountUp from "react-countup";

import UserCard from "../UserCard/UserCard";

const UserList = (props: Props) => {
  if (!props.users) {
    return <h1>loading...</h1>;
  }
  var { count, users, podium } = props;
  return (
    <div className={styles.container}>
      {Object.keys(podium).map((top: any, i: number) => (
        <UserCard
          key={i}
          user={podium[top]}
          top={top} // FIXME
          count={count}
          users={users}
          className={styles.card}
        />
      ))}
    </div>
  );
};

export default UserList;

type Props = {
  count: any;
  users: any;
  podium: any;
};
