import React from "react";
import { Card, CardContent, Typography, Grid, Avatar, Box } from "@material-ui/core";
import styles from "./UserCard.module.css";
import CountUp from "react-countup";
import { User } from "../../types"
import { Link } from "react-router-dom";

const UserCard = (props: { user: User, className?: string }) => {
  if (!props.user) {
    return <h1>loading...</h1>;
  }
  var { user, className } = props;
  return (
    <Link to={"user/" + user.user_id}>
      <div className={styles.container}>

        <Grid item component={Card} className={className ?? ""}>
          <CardContent>
            <Box mb={1}>
              <Typography color="textSecondary">Top {user?.top}</Typography>
            </Box>
            <Avatar alt={user.name} src={user.avatar_url} />
            <Typography variant="body2">
              avec{" "}
              <CountUp
                start={0}
                end={user.nb_msg ?? 0}
                duration={3}
              />{" "}
              messages !
            </Typography>
            <Box mt={2}>
              <Typography variant="h5">{user?.name}</Typography>
            </Box>
          </CardContent>
        </Grid>
      </div>
    </Link>
  );
};
export default UserCard;
