import { JSX, useState } from 'react';
import styles from './Research.module.css';
import { ResearchProps } from './Research.props';
import cn from 'classnames';
import { P } from '../P/P';
import { Button } from '../Button/Button';
import Image from 'next/image';

export const Research = ({
  onSearch,
  error,
  className,
  placeholder,
  icon,
  ...props
}: ResearchProps): JSX.Element => {
  const [searchQuery, setSearchQuery] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSearch(searchQuery);
  };

  return (
    <form
      onSubmit={handleSubmit}
      className={cn(styles.form, className)}
      {...props}
    >
      <div className={styles.searchContainer}>
        <div className={styles.inputWrapper}>
          <input
            id="search"
            type="text"
            placeholder={placeholder}
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className={styles.input}
            required
          />
          <Button
            className={cn(styles.icon, className, {
                [styles.searchButton]: icon == 'right',
                [styles.calendarButton]: icon == 'left',
            })} 
            appearance="ghost" 
            type="submit" 
          >
            {icon === "right" ? (
            <Image
                src="/icons/icon-wrapper.svg"
                alt="Поиск"
                width={20}
                height={20}
            />
            ) : "Период"}
          </Button>
        </div>
      </div>

      {error && <P size="s" className={styles.error}>{error}</P>}
    </form>
  );
};