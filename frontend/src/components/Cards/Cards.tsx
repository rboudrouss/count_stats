import React from "react";
import { Grid } from "@material-ui/core";
import styles from "./Cards.module.css";
import cx from "classnames";
import { UserCard } from "..";
import { User } from "../../types"

const Cards = (props: { users: User[] }) => {
  if (!props.users) {
    return <h1>loading...</h1>;
  }
  var {
    users
  } = props;
  return (
    <div className={styles.container}>
      <Grid container spacing={3} justify="space-evenly">
        <UserCard
          user={users[0]}
          className={cx(styles.card, styles.top1)}
        />
        <UserCard
          user={users[2]}
          className={cx(styles.card, styles.top3)}
        />
        <UserCard
          user={users[1]}
          className={cx(styles.card, styles.top2)}
        />
      </Grid>
    </div>
  );
};

export default Cards;
