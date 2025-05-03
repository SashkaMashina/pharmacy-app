import { DetailedHTMLProps, HTMLAttributes, ReactNode } from "react";

export interface FooterProps extends DetailedHTMLProps<HTMLAttributes<HTMLDivElement>, HTMLDivElement> {
    companyLinks?: {
        title: string;
        links: string[];
      };
      catalogLinks?: {
        title: string;
        links: string[];
      };
      paymentMethods?: {
        title: string;
        methods: string[];
        cards: string[];
      };
}