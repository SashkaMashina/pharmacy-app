import { JSX, useState } from 'react';
import styles from './LoginForm.module.css';
import { LoginFormProps } from './LoginForm.props';
import cn from 'classnames';
import { P } from '../P/P';
import { Button } from '../Button/Button';

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
        <input
          id="login"
          type="text"
          value={login}
          onChange={(e) => setLogin(e.target.value)}
          className={styles.input}
          required
        />
      </div>

      <div className={styles.inputGroup}>
        <input
          id="password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className={styles.input}
          required
        />
      </div>

      {error && <P size="s" className={styles.error}>{error}</P>}

      <Button 
        appearance="primary" 
        type="submit" 
        className={styles.button}
      >
        Войти
      </Button>
    </form>
  );
};