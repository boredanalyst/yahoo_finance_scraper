import tkinter as tk
import pandas as pd
import numpy as np
import yfinance as yf
import tkinter.messagebox as msg

## Setting up the functions and variables.

def getTimePeriods():
    symbol = ent_symbol.get()

    if symbol == "":
        msg.showerror("Invalid symbol","Please provide the a valid symbol.")
    else:
        tkr = yf.Ticker(symbol)
        hist = tkr.history("1mo")
        hist.to_csv("YahooFinanceFile.csv")
        btn_extract.config(text="hello")

def getTimePeriod():
    symbol = ent_symbol.get()

    if symbol == "":
        msg.showerror("No symbol found.","Please provide a valid symbol.")
    else:
        tkr = yf.Ticker(symbol)
        hist = tkr.history("1mo")
        hist.to_csv("YahooFinanceFile.csv")
        ent_symbol.delete(0,"end")
        msg.showinfo("Success","File downloaded. Please find csv file in the directory of this program.")

## Setting up the GUI

root = tk.Tk()
root.title("YF Scraper")
root.geometry("280x235")

## Setting up the header.
lbl_header = tk.Label(root,text="Yahoo Finance Scraper",font=("Arial",12,"bold"))
lbl_header.pack()

lbl_subhead = tk.Label(root,text="Made with Python and Tkinter",font=("Arial",8,"italic"))
lbl_subhead.pack()

## Setting up the input fields.

frm_input = tk.Frame(root,background="lightgray",relief=tk.GROOVE,borderwidth=2)
frm_input.pack()

lbl_ins = tk.Label(frm_input,wraplength=230,justify="left",text="Provide the relevant information below and click the 'Extract' buttton to start the process",font=("Arial",10))
lbl_ins.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky="w")

lbl_symbol = tk.Label(frm_input,text="Symbol",font=("Arial",10))
lbl_symbol.grid(row=1,column=0,padx=5,pady=5,sticky="w")

ent_symbol = tk.Entry(frm_input)
ent_symbol.grid(row=1,column=1,padx=5,pady=5,sticky="w")

btn_extract = tk.Button(frm_input,text="Extract",width=30,command=getTimePeriod)
btn_extract.grid(row=2,column=0,columnspan=2,padx=5,pady=10,sticky="w")

root.mainloop()