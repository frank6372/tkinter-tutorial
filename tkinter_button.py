from tkinter import *

root = Tk()
root.title("My first GUI")
root.geometry("1200x1000")
def my_click():
    my_label = Label(root, text="Wow!!! I click a button!")
    my_label.pack()
# things i put in this button as example:
#can call the function my_click i did when clicking the button
# i add front color background color
# added padding size
myButton = Button(root, text="Click me!", padx=50, pady=30, command=my_click, fg="red", bg="blue") # can also add state disable
myButton.pack()
root.mainloop()

