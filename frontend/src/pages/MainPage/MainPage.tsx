import React from "react";
import { ThemeProvider } from '@material-ui/styles';
import { Typography, Grid } from "@material-ui/core";
import styles from "./MainPage.module.css";

import { getUsers } from "../../api";
import { Cards, Chart, UserPicker, TopBar } from "../../components";
import { User } from "../../types"
import theme from "../../theme"

class MainPage extends React.Component {
  state: { users: User[], selectedUser: string } = {
    users: [],
    selectedUser: "",
  };

  constructor(props: {}) {
    super(props);
    this.selectedUserChange = this.selectedUserChange.bind(this);
  }

  async componentDidMount() {
    const users = await getUsers();
    this.setState({ users });
  }

  async selectedUserChange(selectedUser: string) {
    this.setState({ selectedUser: selectedUser });
  }

  render() {
    const { users, selectedUser } = this.state;
    return (
      <ThemeProvider theme={theme}>
        <TopBar />
        <div className={styles.container}>
          <section className={styles.intro}>
            <Typography variant="h4" color="secondary">
              Bienvenue sur count stats !
            </Typography>
            <Typography color="textSecondary">
              count_stats (toujours à la recherche d'un meilleur nom) est un site relevant les statistiques d'activité d'un
              channel discord.
            </Typography>
          </section>
          <section className={styles.cards}>
            <Typography variant="h5" color="textSecondary">
              Podium
            </Typography>
            <Cards users={users} />
          </section>
          <UserPicker
            users={users}
            selectedUserChange={this.selectedUserChange}
          />
          <Chart selectedUser={selectedUser} />
        </div>
      </ThemeProvider>
    );
  }
}

export default MainPage;
