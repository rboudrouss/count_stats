
import React from "react";
import { AppBar, Toolbar, Typography } from "@material-ui/core";

import styles from "./TopBar.module.css";

import { Link } from "react-router-dom";

const TopBar = () => {
    return (
        <AppBar position="static">
            <Toolbar variant="dense">
                <div className={styles.toolbar}>
                    <Link to="/" color="inherit">
                        <Typography variant="h6" color="inherit">
                            Count Stats
                        </Typography>
                    </Link>
                    <div className={styles.links}>
                        <Link to="/" color="inherit">
                            <Typography variant="h6">
                                Home
                            </Typography>
                        </Link>
                        <Link to="/list" color="inherit">
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
