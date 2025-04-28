import { DetailedHTMLProps, HTMLAttributes, ReactNode } from "react";

export interface LoginFormProps extends DetailedHTMLProps<HTMLAttributes<HTMLFormElement>, HTMLFormElement> {
    icon?: 'pass' | 'log' ;
    text?: string;
    onLogin: (credentials: { login: string; password: string }) => void;
    error?: string;
}