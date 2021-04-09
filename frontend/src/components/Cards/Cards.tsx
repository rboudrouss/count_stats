import React from "react";
import { Card, CardContent, Typography, Grid, Avatar } from "@material-ui/core";
import styles from "./Cards.module.css";
import CountUp from "react-countup";
import cx from "classnames";
import UserList from "../UserList/UserList";
import { UserCard } from "..";

const Cards = (props: any) => {
  if (!props.users) {
    return <h1>loading...</h1>;
  }
  var {
    users,
  } = props;
  return (
    <div className={styles.container}>
      <Grid container spacing={3} justify="center">
        <UserCard
          user={users[0]}
          top={1}
          className={cx(styles.card, styles.top1)}
        />
        <UserCard
          user={users[1]}
          top={2}
          className={cx(styles.card, styles.top2)}
        />
        <UserCard
          user={users[2]}
          top={3}
          className={cx(styles.card, styles.top3)}
        />
      </Grid>
    </div>
  );
};

export default Cards;
