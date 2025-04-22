import { JSX } from "react";
import styles from './P.module.css'
import {PProps} from './P.props'
import React from "react";
import cn from "classnames";
import classNames from "classnames";


export const P = ({ size, children, className, ...props}: PProps): JSX.Element => {
    return(
        <p
        className={cn(styles.p, className, {
            [styles.s]: size == 's',
            [styles.m]: size == 'm',
            [styles.m]: size == 'l',
        })}
        {...props}
        >
            {children}
        </p>
    )
};