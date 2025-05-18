// index.tsx
import React, { JSX } from "react";
import { Button, P, Research, Medicine } from "@/components";
import { Layout, withLayout } from "@/layout/Layout";
import styles from './index.module.css';

function Home(): JSX.Element {
    const handleSearch = (query: string) => {
        console.log('Searching for:', query);
    };
    
    const medicines = [
        { name: "Аспирин", price: 100 },
        { name: "Парацетамол", price: 80 },
        { name: "Ибупрофен", price: 120 },
        { name: "Анальгин", price: 90 },
    ];

    return(
        <div className={styles.wrapper}>
            <div className={styles.findContainer}>
                <Research size="m" className={styles.find} icon="right" placeholder="Поиск товара" onSearch={handleSearch}>
                    ПОИСК
                </Research>
                <Button appearance="green">Форма обратной связи</Button>
            </div>
            
            <P size="x" color="black" className={styles.title}>Каталог</P>
            <div className={styles.mainContent}>
                <div className={styles.sidebar}>
                    <div className={styles.filters}>
                        <div className={styles.filterOptions}>
                            <span className={styles.filterItem}>Категории</span>
                            <span className={styles.filterItem}>Отпуск из аптеки</span>
                            <span className={styles.filterItem}>Сортировать по цене</span>
                            <Button className={styles.filterButton} appearance="green">
                                Сбросить фильтры
                            </Button>
                        </div>
                    </div>
                </div>
                
                <div className={styles.products}>
                    <div className={styles.medicinesList}>
                        {medicines.map((medicine, index) => (
                            <Medicine key={index} name={medicine.name} price={medicine.price} />
                        ))}
                    </div>
                </div>
            </div>
        </div>
    )
}

export default withLayout(Home);