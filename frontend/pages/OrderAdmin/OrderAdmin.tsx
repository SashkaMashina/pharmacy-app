import React, { JSX, useState } from "react";
import { Htag } from "@/components";
import { Button } from "@/components";
import { P } from "@/components";
import { Tag } from "@/components";
import { Layout, withLayout } from "@/layout/Layout";
import { LoginForm } from "@/components";
import {Research} from"@/components"
import {OrdersTable} from"@/components"
import { queryObjects } from "v8";
import styles from './OrderAdmin.module.css'

interface Order {
  id: number;
  customerName: string;
  phone: string;
  email: string;
  date: string;
  orderDetails: string;
  amount: number;
  status: 'new' | 'assembling' | 'ready' | 'completed' | 'cancelled';
}

const mockOrders: Order[] = [
  {
    id: 1,
    customerName: "Иванов Иван Иванович",
    phone: "+7 (900) 123-45-67",
    email: "ivanov@example.com",
    date: "2023-05-20",
    orderDetails: "Аспирин, Нурофен",
    amount: 1250.50,
    status: "new" // теперь TypeScript знает, что это допустимое значение
  },
  {
    id: 2,
    customerName: "Петрова Анна Сергеевна",
    phone: "+7 (901) 234-56-78",
    email: "petrova@example.com",
    date: "2023-05-19",
    orderDetails: "Лоратадин, Називин",
    amount: 870.00,
    status: "assembling" // тоже допустимое значение
  },
  {
    id: 3,
    customerName: "Петрова Анна Сергеевна",
    phone: "+7 (901) 234-56-78",
    email: "petrova@example.com",
    date: "2023-05-19",
    orderDetails: "Лоратадин, Називин",
    amount: 870.00,
    status: "assembling" // тоже допустимое значение
  },
  {
    id: 4,
    customerName: "Иванов Иван Иванович",
    phone: "+7 (900) 123-45-67",
    email: "ivanov@example.com",
    date: "2023-05-20",
    orderDetails: "Аспирин, Нурофен",
    amount: 1250.50,
    status: "new" // теперь TypeScript знает, что это допустимое значение
  },
  {
    id: 5,
    customerName: "Иванов Иван Иванович",
    phone: "+7 (900) 123-45-67",
    email: "ivanov@example.com",
    date: "2023-05-20",
    orderDetails: "Аспирин, Нурофен",
    amount: 1250.50,
    status: "new" // теперь TypeScript знает, что это допустимое значение
  },
  {
    id: 6,
    customerName: "Иванов Иван Иванович",
    phone: "+7 (900) 123-45-67",
    email: "ivanov@example.com",
    date: "2023-05-20",
    orderDetails: "Аспирин, Нурофен",
    amount: 1250.50,
    status: "new" // теперь TypeScript знает, что это допустимое значение
  },
    {
    id: 7,
    customerName: "Иванов Иван Иванович",
    phone: "+7 (900) 123-45-67",
    email: "ivanov@example.com",
    date: "2023-05-20",
    orderDetails: "Аспирин, Нурофен",
    amount: 1250.50,
    status: "new" // теперь TypeScript знает, что это допустимое значение
  },
];

function OrderAdmin(): JSX.Element {
  const [orders, setOrders] = useState(mockOrders);
  const [activeStatus, setActiveStatus] = useState<string | null>(null);
  
  const handleSearch = (query: string) => {
    console.log('Searching for:', query);
  };

    const handleStatusChange = (orderId: number, newStatus: string) => {
      console.log(`Order ${orderId} status changed to ${newStatus}`);
  };

    const filteredOrders = activeStatus 
    ? orders.filter(order => order.status === activeStatus)
    : orders;
  

  return (
    <>
    <div className={styles.container}>
      <div className={styles.searchBlock}>
        <Research size="s" icon="left" onSearch={handleSearch}>ПОИСК</Research>
        <Research size="s" icon="right" placeholder="ФИО покупателя" onSearch={handleSearch}>ПОИСК</Research>
        <Research size="s" icon="right" placeholder="Номер телефона" onSearch={handleSearch}>ПОИСК</Research>
        <Research size="s" icon="right" placeholder="Электронная почта" onSearch={handleSearch}>ПОИСК</Research>
      </div>
      <div className={styles.statusBlock}>
        <Button className={styles.statusButton} appearance="ghost">Новый</Button>
        <Button className={styles.statusButton} appearance="ghost">В процессе сборки</Button>
        <Button className={styles.statusButton} appearance="ghost">Готов к выдаче</Button>
        <Button className={styles.statusButton} appearance="ghost">Завершен</Button>
        <Button className={styles.statusButton} appearance="ghost">Отменен</Button>
      </div>
      <div className={styles.orderContainer}>
        <OrdersTable orders={mockOrders} onStatusChange={handleStatusChange}></OrdersTable>
      </div>
    </div>
    </>
  );
}

export default withLayout(OrderAdmin);
