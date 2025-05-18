import { DetailedHTMLProps, HTMLAttributes } from "react";

export interface ResearchProps 
  extends DetailedHTMLProps<HTMLAttributes<HTMLFormElement>, HTMLFormElement> {
  onSearch: (query: string) => void;
  error?: string;
  placeholder?: string;
  icon?: "right" | "left";
  size: "s" | "m";
}