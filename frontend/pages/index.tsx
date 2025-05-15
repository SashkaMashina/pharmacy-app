import React, { JSX } from "react";
import { Htag } from "@/components";
import { Button } from "@/components";
import { P } from "@/components";
import { Tag } from "@/components";
import { Layout, withLayout } from "@/layout/Layout";
import { LoginForm } from "@/components";
import {Research} from"@/components"
import { queryObjects } from "v8";
import styles from './index.module.css'

function Home(): JSX.Element {
  const handleSearch = (query: string) => {
    console.log('Searching for:', query);
  };
  return (
    <>
    <div className={styles.container}>
      <div className={styles.searchBlock}>
        <Research icon="left" onSearch={handleSearch}>ПОИСК</Research>
        <Research icon="right" placeholder="ФИО покупателя" onSearch={handleSearch}>ПОИСК</Research>
        <Research icon="right" placeholder="Номер телефона" onSearch={handleSearch}>ПОИСК</Research>
        <Research icon="right" placeholder="Электронная почта" onSearch={handleSearch}>ПОИСК</Research>
      </div>
      <div className={styles.statusBlock}>
        <Button className={styles.statusButton} appearance="ghost">Новый</Button>
        <Button className={styles.statusButton} appearance="ghost">В процессе сборки</Button>
        <Button className={styles.statusButton} appearance="ghost">Готов к выдаче</Button>
        <Button className={styles.statusButton} appearance="ghost">Завершен</Button>
        <Button className={styles.statusButton} appearance="ghost">Отменен</Button>
      </div>
    </div>
    </>
  );
}

export default withLayout(Home);
