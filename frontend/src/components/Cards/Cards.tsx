import styles from "./Cards.module.css";
import cx from "classnames";
import { UserCard } from "..";
import { User } from "../../types"

const Cards = (props: { users: User[] }) => {
  if (!props.users) {
    return <h1>loading...</h1>;
  }
  var {
    users
  } = props;
  return (
    <div className={styles.container}>
      <UserCard
        user={users[2]}
        className={cx(styles.card, styles.top3)}
      />
      <UserCard
        user={users[0]}
        className={cx(styles.card, styles.top1)}
      />
      <UserCard
        user={users[1]}
        className={cx(styles.card, styles.top2)}
      />
    </div>
  );
};

export default Cards;
