import React from "react";
import { Card, CardContent, Typography, Grid, Avatar } from "@material-ui/core";
import styles from "./UserCard.module.css";
import CountUp from "react-countup";

const UserCard = (props: Props) => {
  if (!props.users) {
    return <h1>loading...</h1>;
  }
  var { count, users, user, top, className } = props;
  return (
    <div className={styles.container}>
      <Grid item component={Card} className={className}>
        <CardContent>
          <Avatar alt={users[user]?.name} src={users[user]?.avatar_url} />
          <Typography variant="h5">{users[user]?.name}</Typography>
          <Typography color="textSecondary">Top {top}</Typography>
          <Typography variant="body2">
            <CountUp
              start={0}
              end={count[user] ? count[user] : 0}
              duration={3}
            />{" "}
            messages !
          </Typography>
        </CardContent>
      </Grid>
    </div>
  );
};

export default UserCard;

type Props = {
  user: string;
  count: any;
  users: any;
  top: number;
  className?: any;
};
