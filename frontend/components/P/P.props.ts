import { DetailedHTMLProps, HTMLAttributes, ReactNode } from "react";

export interface PProps extends DetailedHTMLProps<HTMLAttributes<HTMLParagraphElement>, HTMLParagraphElement> {
    size: 's' | 'm' | 'l' | 'x';
    children: ReactNode;
    color?: 'black' | 'white' | 'green';
}