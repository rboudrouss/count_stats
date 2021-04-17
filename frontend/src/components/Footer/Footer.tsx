
import React from "react";
import { AppBar, Toolbar, Typography, Link } from "@material-ui/core";
import GitHubIcon from '@material-ui/icons/GitHub';
import PublicIcon from '@material-ui/icons/Public';
import styles from "./Footer.module.css";


const Footer = () => {
    return (
        <footer className={styles.footer}>
            <a href="mailto:rboudrouss@gmail.com" className="footer__link">rboudrouss@gmail.com</a>
            <ul className={styles.social_list}>
                <li className={styles.itmes}>
                    <a className="social-list__link" href="https://github.com/rboudrouss/count_stats" target="_blank">
                        <GitHubIcon color="inherit" />
                    </a>
                </li>
                <li className="social-list__item">
                    <a className="social-list__link" href="https://rboud.ml" target="_blank">
                        <PublicIcon color="inherit" />
                    </a>
                </li>
            </ul>
        </footer >
    )
}

export default Footer;