import tkinter
# Initialize main windows with title and size
top = tkinter.Tk()
top.title("Hello GUI")
top.minsize(200,30)
# Label widget
helloLabel = tkinter.Label(top, text = "Hello World!")
helloLabel.pack()
# Start and open the window
top.mainloop()
