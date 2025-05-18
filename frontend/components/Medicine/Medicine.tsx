import React, { JSX } from "react";
import { Button } from "@/components";
import { P } from "@/components";
import styles from './Medicine.module.css';
import {MedicineProps} from './Medicine.props'
import cn from "classnames";
import classNames from "classnames";


export const Medicine = ({ name, price, ...props}: MedicineProps): JSX.Element => {
    return(
        <div className={cn(styles.card)}>
            <P size="s" color="black" className={styles.name}>{name}</P>
            <P size="s" color="black" className={styles.price}>Цена: {price} ₽</P>
            <Button appearance="green" className={styles.button}>Забронировать</Button>
        </div>       
    )
};