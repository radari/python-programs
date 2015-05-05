#!/usr/bin/env python3.4

import tkinter as tk
    
top = tk.Tk()
# width x height + x_offset + y_offset:
top.geometry("170x200+30+30") 
     
helloLabel = tk.Label(top, text='Hello World!')
helloLabel.place(x = 20, y = 30, width=120, height=25)

quitButton = tk.Button(top, text='QUIT', command=top.quit, bg='#6897BB', fg='white')
quitButton.place(x = 20, y = 80, width=120, height=25)

top.mainloop()
