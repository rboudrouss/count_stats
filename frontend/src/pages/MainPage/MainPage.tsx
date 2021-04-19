import React from "react";
import { Typography } from "@material-ui/core";
import styles from "./MainPage.module.css";

import { getUsers } from "../../api";
import { Cards, Chart, UserPicker, Loading } from "../../components";
import { User } from "../../types"

class MainPage extends React.Component {
  state: { users: User[], selectedUser: string, loading: boolean } = {
    users: [],
    selectedUser: "",
    loading: true
  };

  constructor(props: {}) {
    super(props);
    this.selectedUserChange = this.selectedUserChange.bind(this);
  }

  async componentDidMount() {
    const users = await getUsers();
    this.setState({ users, loading: false });
  }

  async selectedUserChange(selectedUser: string) {
    this.setState({ selectedUser: selectedUser });
  }

  render() {
    const { users, selectedUser, loading } = this.state;
    return (
      <>
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
          {loading
            ?
            <section className={styles.loading}>
              <Loading loading={loading} />
            </section>
            :
            <>
              <section className={styles.cards}>
                <Typography variant="h5" color="textSecondary">
                  Podium
                </Typography>
                <Cards users={users} />
              </section>
              <section className={styles.chart}>
                <UserPicker
                  users={users}
                  selectedUserChange={this.selectedUserChange}
                />
                <Chart selectedUser={selectedUser} />
              </section>
            </>
          }
        </div>
      </>
    );
  }
}

export default MainPage;
