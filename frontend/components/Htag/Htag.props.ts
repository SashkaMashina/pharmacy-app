import { ButtonHTMLAttributes, DetailedHTMLProps, HTMLAttributes, ReactNode } from "react";

export interface HtagProps extends DetailedHTMLProps<HTMLAttributes<HTMLHeadElement>, HTMLHeadElement>  {
    tag: 'h1' | 'h2' | 'h3';
    children: ReactNode;
}