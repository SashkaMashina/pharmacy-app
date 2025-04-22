import React from "react";
import { Htag } from "@/components";
import { Button } from "@/components";

export default function Home() {
  return (
    <>
    <Htag tag="h1">Текст</Htag>
    <Button appearance="primary" arrow="right">Кнопка</Button>
    <Button appearance="ghost">Вторая кнопка</Button>
    </>
  );
}
