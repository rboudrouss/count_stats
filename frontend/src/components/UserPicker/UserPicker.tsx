import { NativeSelect, FormControl } from "@material-ui/core";
import { User } from "../../types"

import styles from "./UserPicker.module.css";

const UserPicker = (props: {
  users: User[],
  selectedUserChange: (selectedUser: string) => Promise<void>
}) => {
  const users: User[] = props.users ?? [];
  const selectedUserChange = props.selectedUserChange;

  return (
    <FormControl className={styles.formControl}>
      <NativeSelect
        defaultValue=""
        onChange={(e) => {
          selectedUserChange(e.target.value);
        }}
      >
        <option value="">Global</option>
        {users.map((user: User, i: number) => (
          <option key={i} value={user?.user_id}>
            {user?.name}
          </option>
        ))}
      </NativeSelect>
    </FormControl>
  );
};

export default UserPicker;
