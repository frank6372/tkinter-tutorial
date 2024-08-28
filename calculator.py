from tkinter import *
# Initialize the main window
root = Tk()
root.title("My first GUI")

root.title("Simple Calculator")
# Create an entry widget for displaying input and output
e = Entry(root,width=29, borderwidth=2)
# Function to handle button clicks for numbers
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
# Function to clear the entry widget
def button_clear():
    e.delete(0, END)
   # Function button to handle the addition operation 
def button_add():
    first_number = e.get() # Get the first number from the entry widget
    global f_num # Declare f_num as a global variable
    f_num = int(first_number) # Convert the first number into integer
    e.delete(0, END) # Clear the entry widget
# Function to handle the equal button click
def button_equal():
    second_number = e.get() # Get the second number from the entry widget
    e.delete(0, END) # Clear the entry widget
    e.insert(0, f_num + int(second_number))# Perform the addition and display result  

e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# define button with their respective labels and command
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=108, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=86, pady=20, command=button_clear)


# Place button on the grid
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

# Run the main loop 
root.mainloop()