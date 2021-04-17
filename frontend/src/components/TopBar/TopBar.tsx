
import React from "react";
import { AppBar, Toolbar, Typography, Link } from "@material-ui/core";
import styles from "./TopBar.module.css";

const TopBar = () => {
    return (
        <AppBar position="static">
            <Toolbar variant="dense">
                <div className={styles.toolbar}>
                    <Typography variant="h6" color="inherit">
                        Count Stats
                    </Typography>
                    <div className={styles.links}>
                        <Link href="/" color="inherit">
                            <Typography variant="h6">
                                Home
                            </Typography>
                        </Link>
                        <Link href="/list" color="inherit">
                            <Typography variant="h6">
                                List
                            </Typography>
                        </Link>
                    </div>
                </div>
            </Toolbar>
        </AppBar>
    )
}

export default TopBar;
