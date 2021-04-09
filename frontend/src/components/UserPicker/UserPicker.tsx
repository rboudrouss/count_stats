import { NativeSelect, FormControl } from "@material-ui/core";

import styles from "./UserPicker.module.css";

const UserPicker = (props: any) => {
  const users = props.users ? props.users : {};
  const selectedUserChange: any = props.selectedUserChange;

  return (
    <FormControl className={styles.formControl}>
      <NativeSelect
        defaultValue=""
        onChange={(e) => {
          selectedUserChange(e.target.value);
        }}
      >
        <option value="">Global</option>
        {Object.values(users).map((user: any, i: number) => (
          <option key={i} value={user?.user_id}>
            {user?.name}
          </option>
        ))}
      </NativeSelect>
    </FormControl>
  );
};

export default UserPicker;
