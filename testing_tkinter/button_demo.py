#!/usr/bin/env python3.4

from tkinter import *

top = Tk()

def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

B = Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()
