import { JSX } from "react";
import styles from './Header.module.css'
import {FooterProps} from './Footer.props'
import React from "react";
import cn from "classnames";
import classNames from "classnames";


export const Footer = ({ ...props}: FooterProps): JSX.Element => {
    return(
        <>
            <div {...props}>Footer</div>
        </>
    )
};