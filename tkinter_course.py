from tkinter import *
# main information required 
root = Tk()
root.title("My first GUI")
root.geometry("1200x1000")
# Creating a label widget
myLAbel1 = Label(root, text = "Hello World!")
myLAbel2 = Label(root, text = "My name is Frank!")
# insert label on the grid:
myLAbel1.grid(row=0, column=0)
myLAbel2.grid(row=1, column=0)

root.mainloop()

