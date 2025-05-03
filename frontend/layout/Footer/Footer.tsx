import { JSX } from "react";
import styles from './Footer.module.css'
import {FooterProps} from './Footer.props'
import React from "react";
import cn from "classnames";
import classNames from "classnames";
import { Htag, P, Tag } from "@/components";


export const Footer = ({ 
    companyLinks = {
        title: "О компании",
        links: ["О нас", "Контакты", "Новости", "Акции"]
      },
      catalogLinks = {
        title: "Каталог",
        links: [
          "Антибиотики",
          "Обезболивающие",
          "Витамины",
          "Антисептики",
          "Противоаллергические"
        ]
      },
      paymentMethods = {
        title: "Способы оплаты",
        methods: [
          "Наличная и безналичная",
          "Оплата в аптеке при получении заказа"
        ],
        cards: ["VISA", "МИР"]
      },
    ...props}: FooterProps): JSX.Element => {
    return(
        <>
            <footer className={styles.footer}>
            <div className={styles.container}>

                <div className={styles.section}>
                    <Htag className={styles.sectionTitle} tag="h3">{companyLinks.title}</Htag>
                    <ul className={styles.linkList}>
                        {companyLinks.links.map((link, index) => (
                        <li key={index} className={styles.linkItem}>
                            <Tag color="green" href="#" className={styles.link}>{link}</Tag>
                        </li>
                        ))}
                    </ul>
                </div>


                <div className={styles.section}>
                    <Htag className={styles.sectionTitle} tag="h3">{catalogLinks.title}</Htag>
                    <ul className={styles.linkList}>
                        {catalogLinks.links.map((link, index) => (
                        <li key={index} className={styles.linkItem}>
                            <Tag color="green" href="#" className={styles.link}>{link}</Tag>
                        </li>
                        ))}
                    </ul>
                </div>


                <div className={styles.section}>
                    <Htag className={styles.sectionTitle} tag="h3">{paymentMethods.title}</Htag>
                    <ul className={styles.linkList}>
                        {paymentMethods.methods.map((method, index) => (
                        <li key={index} className={styles.linkItem}>
                            <P color='green' className={styles.link} size="m">{method}</P>
                        </li>
                        ))}
                    </ul>
                    <div className={styles.paymentMethods}>
                        {paymentMethods.cards.map((card, index) => (
                        <span key={index} className={styles.paymentCard}>{card}</span>
                        ))}
                    </div>
                </div>
            </div>
            </footer>
        </>
    )
};