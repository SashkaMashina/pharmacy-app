import React, { JSX } from "react";
import { Htag } from "@/components";
import { Button } from "@/components";
import { P } from "@/components";
import { Tag } from "@/components";
import { Layout, withLayout } from "@/layout/Layout";

function Home(): JSX.Element {
  return (
    <>
      <Htag tag="h1">Текст</Htag>
      <Button appearance="primary" arrow="right">Кнопка</Button>
      <Button appearance="ghost">Вторая кнопка</Button>
      <P size="s">Маленький</P>
      <P size="m">Средний</P>
      <P size="l">Большой</P>
      <Tag color="green">Hello</Tag>
    </>
  );
}

export default withLayout(Home);
