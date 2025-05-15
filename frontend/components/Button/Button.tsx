import { JSX } from "react";
import { ButtonProps } from "./Button.props";
import React from "react";
import styles from'./Button.module.css'
import cn from 'classnames'
import { Span } from "next/dist/trace";

export const Button = ({ appearance, icon = 'none',  children, className, ...props}: ButtonProps): JSX.Element => {
    return(
        <button
        className={cn(styles.button, className, {
            [styles.green]: appearance == 'green',
            [styles.ghost]: appearance == 'ghost',
        })}
        {...props}
        >
            {children}
            {icon !== 'none' && <span className={cn(styles.icon, {
                [styles.search]: icon == 'search'
            })}>
                <img src="/icons/icon-wrapper.svg"></img>
                </span>}
        </button>
    )
};