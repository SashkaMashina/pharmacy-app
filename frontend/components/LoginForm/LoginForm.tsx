import { JSX, useState } from 'react';
import styles from './LoginForm.module.css';
import { LoginFormProps } from './LoginForm.props';
import cn from 'classnames';
import { P } from '../P/P';
import { Button } from '../Button/Button';
import Image from 'next/image';

export const LoginForm = ({
  onLogin,
  error,
  icon, 
  text,
  className,
  ...props
}: LoginFormProps): JSX.Element => {
  const [login, setLogin] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onLogin({ login, password });
  };

  return (
    <form
      onSubmit={handleSubmit}
      className={cn(styles.form, className)}
      {...props}
    >
      <P size="l" className={styles.title}>Вход в систему</P>

      <div className={styles.inputGroup}>
        <div className={styles.inputContainer}>
            <div className={styles.iconWrapper}>
                <Image
                src="/icons/log.svg"
                alt="Логин"
                width={20}
                height={20}
                className={styles.icon}
                />
            </div>
            <input
            id="login"
            type="text"
            placeholder='Логин'
            value={login}
            onChange={(e) => setLogin(e.target.value)}
            className={styles.input}
            required
            />
        </div>
      </div>

      <div className={styles.inputGroup}>
        <div className={styles.inputContainer}>
        <div className={styles.iconWrapper}>
                <Image
                src="/icons/pass.svg"
                alt="Логин"
                width={20}
                height={20}
                className={styles.icon}
                />
            </div>  
            <input
            id="password"
            type="password"
            value={password}
            placeholder='Пароль'
            onChange={(e) => setPassword(e.target.value)}
            className={styles.input}
            required
            />
        </div>
      </div>

      {error && <P size="s" className={styles.error}>{error}</P>}

      <Button 
        appearance="green" 
        type="submit" 
        className={styles.button}
      >
        Войти
      </Button>
    </form>
  );
};