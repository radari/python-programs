#!/usr/bin/env python3.4

import tkinter

# Initialize top with title and size
top = tkinter.Tk()
top.title("Hello GUI")
top.minsize(300,200)
top.maxsize(800,600)

helloLabel = tkinter.Label(top, text='Hello World!')
helloLabel.pack()

quitButton = tkinter.Button(top, text='QUIT', command=top.quit, bg='blue', fg='white')
quitButton.pack(side='right', padx=10, pady=10)

tkinter.mainloop()
