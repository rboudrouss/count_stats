import React from "react";
import { Card, CardContent, Typography, Grid, Avatar } from "@material-ui/core";
import styles from "./UserCard.module.css";
import CountUp from "react-countup";
import { User } from "../../types"

const UserCard = (props: { user: User, className: string }) => {
  if (!props.user) {
    return <h1>loading...</h1>;
  }
  var { user, className } = props;
  return (
    <div className={styles.container}>
      <Grid item component={Card} className={className}>
        <CardContent>
          <Avatar alt={user?.name} src={user?.avatar_url} />
          <Typography variant="h5">{user?.name}</Typography>
          <Typography color="textSecondary">Top {user?.top}</Typography>
          <Typography variant="body2">
            <CountUp
              start={0}
              end={user?.nb_msg ?? 0}
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
