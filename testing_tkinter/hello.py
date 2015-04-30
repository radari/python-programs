import tkinter
# Initialize main windows with title and size
mainwindow = tkinter.Tk()
mainwindow.title("Hello GUI")
mainwindow.minsize(200,30)
# Label widget
helloLabel = tkinter.Label(mainwindow, text = "Hello World!")
helloLabel.pack()
# Start and open the window
mainwindow.mainloop()
