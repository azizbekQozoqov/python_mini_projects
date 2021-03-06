import sys
from tkinter import *
from tkinter.messagebox import showinfo, showwarning, showerror, askquestion,askokcancel

# Creating window
root = Tk()
root.title("Calculator app")
root.minsize(310, 440)
root.maxsize(40, 30)
if sys.platform == "linux":
    root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='/home/developer/Documents/projects/python_mini_projects/calculator/icon.png'))


# input
e = Entry(root, width=35, borderwidth=3)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_add(number):
    try:
        current = e.get()
        e.delete(0, END)
        e.insert(0, current+ str(number))
    except:
        showwarning("Warn", "Please enter right expression!")

def clear():
    e.delete(0, END)

def add():
    try:

        first_number = e.get()
        global f_num
        global math
        math = "addition"
        f_num = int(first_number)
        e.delete(0, END)
    except:
        showwarning("Warn", "Please enter right expression!")

def equal():
    try:
        second_number = e.get()
        e.delete(0, END)

        if math == "addition":
            e.insert(0, f_num + int(second_number))
        if math == "subtracktion":
            e.insert(0, f_num - int(second_number))
        if math == "multiplication":
            e.insert(0, f_num * int(second_number))
        if math == "divison":
            e.insert(0, f_num / int(second_number))
    except:
        showwarning("Warn", "Please enter right expression!")

def subtrackt():
    try:

        first_number = e.get()
        global f_num
        global math
        math = "subtracktion"
        f_num = int(first_number)
        e.delete(0, END)
    except:
        showwarning("Warn", "Please enter right expression!")

def multiply():
    try:
        first_number = e.get()
        global f_num
        global math
        math = "multiplication"
        f_num = int(first_number)
        e.delete(0, END)
    except:
        showwarning("Warn", "Please enter right expression!")

def divide():
    try:

        first_number = e.get()
        global f_num
        global math
        math = "divison"
        f_num = int(first_number)
        e.delete(0, END)
    except:
        showwarning("Warn", "Please enter right expression!")

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_add(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_add(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_add(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_add(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_add(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_add(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_add(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_add(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_add(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_add(0))
button_adder = Button(root, text="+", padx=39, pady=20, command=lambda: add())
button_equal = Button(root, text="=", padx=91, pady=20, command=lambda: equal())
button_clear = Button(root, text="Clear", padx=79, pady=20, command=lambda: clear())

button_subtrackt = Button(root, text="-", padx=41, pady=20, command=lambda: subtrackt())
button_multiply = Button(root, text="*", padx=39, pady=20, command=lambda: multiply())
button_divide = Button(root, text="/", padx=41, pady=20, command=lambda: divide())

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row= 4, column=1, columnspan=2)
button_adder.grid(row= 5, column=0)
button_equal.grid(row= 5, column=1, columnspan=2)

button_subtrackt.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)


# loop
root.mainloop()