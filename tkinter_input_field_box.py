from tkinter import *

root = Tk()
root.title("My first GUI")
root.geometry("1200x1000")
# entry box 
entry_e = Entry(root, width=50)
entry_e.pack()
# add something in the entry box
entry_e.insert(0, "Enter your name: ")
# function that will enable the button to get the entry writing
def my_click():
    hello = "Hello " + entry_e.get()
    name_label = Label(root, text= hello)
    name_label.pack()
    
# command will action my function my_click when button is press.
my_button = Button(root, text="Enter your name", command=my_click)
my_button.pack()

root.mainloop()




