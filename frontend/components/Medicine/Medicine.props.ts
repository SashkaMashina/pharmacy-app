import { DetailedHTMLProps, HTMLAttributes, ReactNode } from "react";

export interface MedicineProps extends DetailedHTMLProps<HTMLAttributes<HTMLDivElement>, HTMLDivElement> {
    name: string;
    price: number;
}