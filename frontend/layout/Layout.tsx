import { Component, FunctionComponent, JSX } from "react";
import styles from './Layout.module.css'
import {LayoutProps} from './Layout.props'
import React from "react";
import cn from "classnames";
import classNames from "classnames";
import { Header } from "./Header/Header";
import { Footer } from "./Footer/Footer";


export const Layout = ({children}: LayoutProps): JSX.Element => {
    return(
        <>
        <div className={styles.layout}>
            <Header/>
                <div className={styles.content}>
                    {children}
                </div>
            <Footer/>
        </div>
        </>
    )
};


export const withLayout = <T extends Record<string, unknown>>(Component: FunctionComponent<T>) => {
    return function withLayoutComponent(props: T): JSX.Element {
        return (
            <Layout>
                <Component {...props} />
            </Layout>
        )
    }
}