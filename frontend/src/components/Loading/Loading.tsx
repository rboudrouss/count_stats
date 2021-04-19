import ClipLoader from "react-spinners/ClipLoader";
import theme from "../../theme"
import styles from "./Loading.module.css"
import { Typography } from "@material-ui/core";

const Loading = ({ loading }: { loading: boolean }) => {
    const color: string = theme.palette.secondary.main;
    return (
        <div className={styles.container}>
            <ClipLoader color={color} loading={loading} size={50} />
            <Typography variant="h5" className={styles.text} >
                Loading
            </Typography>
        </div>);
}

export default Loading;