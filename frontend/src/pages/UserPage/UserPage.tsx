
import React from "react";
import styles from "./UserPage.module.css";
import { User, Message, Inter } from "../../types"
import { Chart, UserCard } from "../../components"
import { getUsers, getUserMsg, getUser, getMsgInter, getHistory } from "../../api";
import { Card, CardContent, Typography, Grid, Avatar, Box } from "@material-ui/core";

class UserPage extends React.Component {
  state: { id: string, user: User | null, userMsg: Message[], highScore: { date: string, nb: number }, nbMsgs: number } = {
    id: (this.props as any).match.params.id as string, // HACK
    user: null,
    userMsg: [],
    highScore: {
      date: '',
      nb: 0,
    },
    nbMsgs: 0
  }

  async componentDidMount() {
    // TODO Optimize
    let userMsg: Message[] = [];
    let interMsg: Inter = [];
    const nbMsgs = (await getHistory())?.length;
    const user = await getUser(this.state.id);
    if (user) {
      userMsg = await getUserMsg({ id: this.state.id }) ?? [];
      interMsg = await getMsgInter({ id: this.state.id }) ?? [];
    }
    interMsg.sort(([a, messages1], [b, messages2]) => messages2.length - messages1.length)

    this.setState({ userMsg, user, highScore: { date: interMsg[0][0], nb: interMsg[0][1].length }, nbMsgs: nbMsgs ?? 0 });
  }


  render() {
    const { user, userMsg, highScore: { date, nb }, nbMsgs } = this.state;
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
            <section className={styles.stats}>
              <div className={styles.cards}>
                <Card className={styles.card} >
                  <CardContent>
                    <Grid
                      container
                      direction="column"
                      alignItems="center"
                      justify="center"
                    >
                      <Typography>
                        Most actif day
                      </Typography>
                      <Typography>
                        {date}
                      </Typography>
                      <Typography>
                        {nb} messages !
                      </Typography>
                    </Grid>
                  </CardContent>
                </Card>
                <Card className={styles.card} >
                  <CardContent>
                    <Grid
                      container
                      direction="column"
                      alignItems="center"
                      justify="center"
                    >
                      <Typography>
                        {Math.round(user.nb_msg / nbMsgs * 1000) / 10} %
                      </Typography>
                      <Typography>
                        of all messages
                      </Typography>
                    </Grid>
                  </CardContent>
                </Card>
                <Card className={styles.card} >
                  <CardContent>
                    <Grid
                      container
                      direction="column"
                      alignItems="center"
                      justify="center"
                    >
                      <Typography>
                        Last message sent
                      </Typography>
                      <Typography>
                        {userMsg[0].date.slice(0, 19).replace('T', ' ')}
                      </Typography>
                      <Typography>
                        First message sent
                      </Typography>
                      <Typography>
                        {userMsg[userMsg.length - 1].date.slice(0, 19).replace('T', ' ')}
                      </Typography>
                    </Grid>
                  </CardContent>
                </Card>
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
