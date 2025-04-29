import { JSX } from "react";
import { ButtonProps } from "./Button.props";
import React from "react";
import styles from'./Button.module.css'
import cn from 'classnames'
import { Span } from "next/dist/trace";

export const Button = ({ appearance, arrow = 'none',  children, className, ...props}: ButtonProps): JSX.Element => {
    return(
        <button
        className={cn(styles.button, className, {
            [styles.green]: appearance == 'green',
            [styles.ghost]: appearance == 'ghost',
        })}
        {...props}
        >
            {children}
            {arrow !== 'none' && <span className={cn(styles.arrow, {
                [styles.down]: arrow == 'down',
                [styles.right]: arrow == 'right'
            })}>
                <img src="/icons/ArrowRight.svg"></img>
                </span>}
        </button>
    )
};