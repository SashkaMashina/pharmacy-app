import { JSX } from "react";
import styles from './P.module.css'
import {PProps} from './P.props'
import React from "react";
import cn from "classnames";
import classNames from "classnames";


export const P = ({ size, children, className, color = 'black', ...props}: PProps): JSX.Element => {
    return(
        <p
        className={cn(styles.p, className, {
            [styles.s]: size == 's',
            [styles.m]: size == 'm',
            [styles.m]: size == 'l',
            [styles.black]: color == 'black',
            [styles.white]: color == 'white',
            [styles.green]: color == 'green'
        })}
        {...props}
        >
            {children}
        </p>
    )
};