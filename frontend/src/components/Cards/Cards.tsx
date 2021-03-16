import React from "react";
import { Card, CardContent, Typography, Grid, Avatar } from "@material-ui/core";
import styles from "./Cards.module.css";
import CountUp from "react-countup";
import cx from "classnames";
import UserList from "../UserList/UserList";
import { UserCard } from "..";

const Cards = (props: any) => {
  console.log(props);
  if (!props.podium) {
    return <h1>loading...</h1>;
  }
  var {
    podium: { top1, top2, top3 },
    count,
    users,
  } = props;
  return (
    <div className={styles.container}>
      <Grid container spacing={3} justify="center">
        <UserCard
          user={top1}
          count={count}
          users={users}
          top={1}
          className={cx(styles.card, styles.top1)}
        />
        <UserCard
          user={top2}
          count={count}
          users={users}
          top={2}
          className={cx(styles.card, styles.top2)}
        />
        <UserCard
          user={top3}
          count={count}
          users={users}
          top={3}
          className={cx(styles.card, styles.top3)}
        />
      </Grid>
    </div>
  );
};

export default Cards;
