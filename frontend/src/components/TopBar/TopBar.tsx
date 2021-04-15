
import React from "react";
import { AppBar, Toolbar, IconButton, Typography } from "@material-ui/core";
import styles from "./TopBar.module.css";
import MenuIcon from '@material-ui/icons/Menu';

const TopBar = () => {
    return (
        <AppBar position="static">
            <Toolbar variant="dense">
                <IconButton edge="start" className={styles.menuButton} color="inherit" aria-label="menu">
                    <MenuIcon />
                </IconButton>
                <Typography variant="h6" color="inherit">
                    Count Stats
                </Typography>
            </Toolbar>
        </AppBar>
    )
}

export default TopBar;
