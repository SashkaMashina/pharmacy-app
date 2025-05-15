import { JSX } from "react";
import styles from './OrderTable.module.css';
import { Button } from "../Button/Button";
import { P } from "../P/P";
import { Tag } from "../Tag/Tag";

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

interface OrdersTableProps {
  orders: Order[];
  onStatusChange: (orderId: number, newStatus: Order['status']) => void;
}


export const OrdersTable = ({ orders, onStatusChange }: OrdersTableProps): JSX.Element => {
  return (
    <div className={styles.tableContainer}>
      <table className={styles.ordersTable}>
        <thead>
          <tr className={styles.headerRow}> 
            <th>№ Заказа</th>
            <th>ФИО покупателя</th>
            <th>Номер телефона</th>
            <th>Электронная почта</th>
            <th>Дата</th>
            <th>Заказ</th>
            <th>Сумма</th>
            <th>Статус</th>
          </tr>
        </thead>
        <tbody>
          {orders.map((order) => (
            <tr key={order.id}>
              <td>{order.id}</td>
              <td>{order.customerName}</td>
              <td>
                <a href={`tel:${order.phone}`} className={styles.phoneLink}>
                  {order.phone}
                </a>
              </td>
              <td>
                <a href={`mailto:${order.email}`} className={styles.emailLink}>
                  {order.email}
                </a>
              </td>
              <td>{order.date}</td>
              <td>
                <Button 
                  appearance="ghost" 
                  onClick={() => console.log('Order details', order.id)}
                  className={styles.detailsButton}
                >
                  Просмотр
                </Button>
              </td>
              <td>{order.amount.toFixed(2)} ₽</td>
              <td>
                <Tag color="white">
                  {getStatusText(order.status)}
                </Tag>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

function getStatusText(status: Order['status']): string {
  switch (status) {
    case 'new': return 'Новый';
    case 'assembling': return 'В сборке';
    case 'ready': return 'Готов';
    case 'completed': return 'Завершен';
    case 'cancelled': return 'Отменен';
    default: return '';
  }
}