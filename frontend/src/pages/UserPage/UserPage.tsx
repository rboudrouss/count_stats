
import React from "react";
import styles from "./UserPage.module.css";
import { User, Message } from "../../types"
import { Chart, UserCard } from "../../components"
import { getUsers, getUserMsg, getUser } from "../../api";
import { Card, CardContent, Typography, Grid, Avatar, Box } from "@material-ui/core";

class UserPage extends React.Component {
  state: { id: string, user: User | null, userMsg: Message[] } = {
    id: (this.props as any).match.params.id as string, // HACK
    user: null,
    userMsg: [],
  }

  async componentDidMount() {
    let userMsg: Message[] = [];
    let user = await getUser(this.state.id);
    if (user) {
      userMsg = await getUserMsg({ id: this.state.id }) ?? [];
    }

    this.setState({ userMsg, user });
  }


  render() {
    const { user, userMsg } = this.state;
    return (
      <div className={styles.container}>
        {
          user ? <>
            <section className={styles.presentation}>
              <div className={styles.mainp}>
                <Avatar alt={user.name} src={user.avatar_url} className={styles.avatar} />
                <Typography className={styles.name} color="inherit" variant="h5">
                  {user.name}#{user.discriminator}
                </Typography>
              </div>
            </section>
            <section className={styles.chart}>
              <Chart selectedUser={user.user_id} />
            </section>
          </> : <>
            <section className={styles.presentation}>
              <Typography className={styles.name} color="inherit" variant="h5">
                User Not Found
              </Typography>
            </section>

          </>
        }
      </div>
    );
  }
}

export default UserPage;
