
import React from "react";

import styles from "./UserPage.module.css";

class UserPage extends React.Component <Props,State> {
  constructor(props: Props) {
    super(props);
  }

  render() {
    return <h1>UsersPage</h1>;
  }
}

export default UserPage;
// TODO TYPES
type Props = {
  count:any,
  podium:any,
  users:any,
}

type State = {
  count:any,
  podium:any,
  users:any,
  selectedUser:string
}
