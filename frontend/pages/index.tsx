import React from "react";
import { Htag } from "@/components";
import { Button } from "@/components";
import { P } from "@/components";
import { Tag } from "@/components";
import { Layout } from "@/layout/Layout";

export default function Home() {
  return (
    <>
    <Layout>
      <Htag tag="h1">Текст</Htag>
      <Button appearance="primary" arrow="right">Кнопка</Button>
      <Button appearance="ghost">Вторая кнопка</Button>
      <P size="s">Маленький</P>
      <P size="m">Средний</P>
      <P size="l">Большой</P>
      <Tag color="green">Hello</Tag>
      </Layout>
    </>
  );
}
