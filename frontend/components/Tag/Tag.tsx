import { JSX } from "react";
import styles from './Tag.module.css'
import {TagProps} from './Tag.props'
import React from "react";
import cn from "classnames";
import classNames from "classnames";


export const Tag = ({ children, color = 'white', href, className, ...props}: TagProps): JSX.Element => {
    return(
        <div 
        className={cn(styles.tag, className, {
            [styles.green]: color == 'green',
            [styles.white]: color == 'white'
        })}
        {...props}
        >
            {
                href
                ? <a href={href}>{children}</a>
                : <>{children}</>
            }
        </div>
    )
};