import React, { JSX } from "react";
import { Htag } from "@/components";
import { Button } from "@/components";
import { P } from "@/components";
import { Tag } from "@/components";
import { Layout, withLayout } from "@/layout/Layout";
import { LoginForm } from "@/components";

function Home(): JSX.Element {
  const handleLogin = (credentials: { login: string; password: string }) => {
    console.log('Данные для входа:', credentials); 
  };

  return (
    <>
      <Htag tag="h1">Текст</Htag>
      <Button appearance="primary" arrow="right">Кнопка</Button>
      <Button appearance="ghost">Вторая кнопка</Button>
      <P size="s">Маленький</P>
      <P size="m">Средний</P>
      <P size="l">Большой</P>
      <Tag color="green">Hello</Tag>
      <LoginForm onLogin={handleLogin} />
    </>
  );
}

export default withLayout(Home);
