import React from "react";
import {
  Card,
  CardContent,
  Typography,
  Grid,
  // StylesProvider,
} from "@material-ui/core";
import styles from "./Cards.module.css";

const Cards = (props: any) => {
  console.log(props);
  return (
    <div className={styles.container}>
      <Grid container spacing={3} justify="center">
        <Grid item component={Card}>
          <CardContent>
            <Typography color="textSecondary">Top 1</Typography>
            <Typography variant="h5">Name</Typography>
            <Typography variant="body2">DATA messages</Typography>
            <Typography color="textSecondary">DATE</Typography>
          </CardContent>
        </Grid>
      </Grid>
      <Grid container spacing={3} justify="center">
        <Grid item component={Card}>
          <CardContent>
            <Typography color="textSecondary">Top 2</Typography>
            <Typography variant="h5">Name</Typography>
            <Typography variant="body2">DATA messages</Typography>
            <Typography color="textSecondary">DATE</Typography>
          </CardContent>
        </Grid>
      </Grid>
      <Grid container spacing={3} justify="center">
        <Grid item component={Card}>
          <CardContent>
            <Typography color="textSecondary">Top 3</Typography>
            <Typography variant="h5">Name</Typography>
            <Typography variant="body2">DATA messages</Typography>
            <Typography color="textSecondary">DATE</Typography>
          </CardContent>
        </Grid>
      </Grid>
    </div>
  );
};

export default Cards;
