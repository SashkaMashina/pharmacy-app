import { JSX } from "react";
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
            <Header/>
            <div>
                {children}
            </div>
            <Footer/>
        </>
    )
};