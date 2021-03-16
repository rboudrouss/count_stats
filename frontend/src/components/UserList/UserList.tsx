import React from "react";
import styles from "./UserList.module.css";
import CountUp from "react-countup";

import UserCard from "../UserCard/UserCard";

const UserList = (props: Props) => {
  console.log(props);
  if (!props.users) {
    return <h1>loading...</h1>;
  }
  var { count, users, podium } = props;
  return (
    <div className={styles.container}>
      {Object.values(podium).map((user: any, i: number) => (
        <UserCard user={user} top={i + 1} count={count} users={users} />
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
