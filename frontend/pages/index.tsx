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
      <LoginForm onLogin={handleLogin} />
    </>
  );
}

export default withLayout(Home);
