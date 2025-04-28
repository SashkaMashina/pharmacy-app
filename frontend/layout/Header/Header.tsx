import { JSX } from "react";
import styles from './Header.module.css'
import {HeaderProps} from './Header.props'
import React from "react";
import cn from "classnames";
import classNames from "classnames";


export const Header = ({ ...props}: HeaderProps): JSX.Element => {
    return(
        <>
            <div {...props}>Header</div>
        </>
    )
};