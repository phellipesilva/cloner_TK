#!/usr/bin/env python3
#-*-coding: utf-8-*-
from tkinter import *
from tkinter import messagebox
import urllib.request
tk = Tk()
tk.title("ClonerTK v1.0 by: Felipe Silva")
tk.geometry("500x125+250+250")
def getht():
  htm = urllib.request.urlopen(link.get())
  with open(newName.get(), "wb") as wrt:
    wrt.write(htm.read())
  messagebox.showinfo("Aviso","Arquivo baixado!")
Label(tk, text="Digite o link abaixo").pack()
link = Entry(tk)
link.pack()
Label(tk, text="Digite um novo nome abaixo").pack()
newName = Entry(tk)
newName.pack()
Button(tk, text="Baixar", command=getht).pack()
tk.mainloop()
