import React from "react";
import {
  Card,
  CardContent,
  Typography,
  Grid,
  Avatar,
} from "@material-ui/core";
import styles from "./Cards.module.css";
import CountUp from "react-countup";
import cx from "classnames";

const Cards = (props: any) => {
  console.log(props);
  // TODO when no data
  const {
    podium: { top1, top2, top3 },
    count,
    users,
  } = props;
  if (!top1) {
    return <h1>loading...</h1>;
  }
  return (
    <div className={styles.container}>
      <Grid container spacing={3} justify="center">
        <Grid
          item
          component={Card}
          xs={12}
          md={4}
          className={cx(styles.card, styles.top1)}
        >
          <CardContent>
            <Avatar alt={users[top1]?.name} src={users[top1]?.avatar_url} />
            <Typography variant="h5">{users[top1]?.name}</Typography>
            <Typography color="textSecondary">Top 1</Typography>
            <Typography variant="body2">
              <CountUp start={0} end={count[top1]} duration={3} /> messages !
            </Typography>
          </CardContent>
        </Grid>
        <Grid
          item
          component={Card}
          xs={12}
          md={4}
          className={cx(styles.card, styles.top2)}
        >
          <CardContent>
            <Avatar alt={users[top2]?.name} src={users[top2]?.avatar_url} />
            <Typography variant="h5">{users[top2]?.name}</Typography>
            <Typography color="textSecondary">Top 2</Typography>
            <Typography variant="body2">
              <CountUp start={0} end={count[top2]} duration={3} /> messages !
            </Typography>
          </CardContent>
        </Grid>
        <Grid
          item
          component={Card}
          xs={12}
          md={4}
          className={cx(styles.card, styles.top3)}
        >
          <CardContent>
            <Avatar alt={users[top3]?.name} src={users[top3]?.avatar_url} />
            <Typography variant="h5">{users[top3]?.name}</Typography>
            <Typography color="textSecondary">Top 3</Typography>
            <Typography variant="body2">
              <CountUp start={0} end={count[top3]} duration={3} /> messages !
            </Typography>
          </CardContent>
        </Grid>
      </Grid>
    </div>
  );
};

export default Cards;
