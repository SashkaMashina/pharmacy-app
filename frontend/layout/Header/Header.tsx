import { JSX } from "react";
import styles from './Header.module.css'
import {HeaderProps} from './Header.props'
import React from "react";
import cn from "classnames";
import classNames from "classnames";
import { Tag } from "@/components";
import Image from 'next/image';


export const Header = ({phone = "+79085648971", address = "ул. Кирова, д. 27", time = "8.00 - 19.00", ...props}: HeaderProps): JSX.Element => {
    return(
        <>
        <header className={styles.header}>
            <div className={styles.leftGroup}>
                <div className={styles.navItem}>
                    <Image 
                        src="/icons/Vector.svg" 
                        alt="Адрес"
                        width={16}
                        height={16}
                        className={styles.icon}
                    />
                    <span>{address}</span>
                </div>
                
                <div className={styles.navItem}>
                    <Image 
                        src="/icons/Phone.svg" 
                        alt="Телефон"
                        width={16}
                        height={16}
                        className={styles.icon}
                    />
                    <span>{phone}</span>
                </div>
                
                <div className={styles.navItem}>
                    <Image 
                        src="/icons/ClockCircle.svg" 
                        alt="Часы работы"
                        width={16}
                        height={16}
                        className={styles.icon}
                    />
                    <span>{time}</span>
                </div>
                
                <div className={styles.navItem}>
                    <Image 
                        src="/icons/Notification.svg" 
                        alt="Новости"
                        width={16}
                        height={16}
                        className={styles.icon}
                    />
                    <Tag href="/news" className={styles.link} color="white">Новости и акции</Tag>
                </div>
            </div>
        
            <div className={cn(styles.navItem, styles.login)}>
                <Image 
                src="/icons/Icon.svg" 
                alt="Вход в систему"
                width={16}
                height={16}
                className={styles.icon}
                />
                <Tag href="/login" className={styles.link} color="white">Вход в систему</Tag>
            </div>
        </header>
        </>
    )
};